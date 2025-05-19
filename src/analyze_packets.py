"""
Analyze zero crossings of G(s) = R(s) - C(s).

Input
-----
csv_path : str
    Path to a spectrum file with columns: scale, R, C, eta

Output
------
Prints a table:
index,  s*,  rho,  eta_packet,  kappa

  s*           zero crossing (mid-scale, same units as scale)
  rho          s*_{i+1} / s*_{i}
  eta_packet   I/E over packet (bits / J)
  kappa        log-space curvature of G at s*
"""
import numpy as np, pandas as pd
from scipy.interpolate import interp1d
from scipy.signal import savgol_filter
from pathlib import Path
import sys

def find_zeros(x, y):
    """Return mid-point location of sign changes in y."""
    sign = np.sign(y)
    idx = np.where(np.diff(sign))[0]
    zeros = []
    for i in idx:
        # linear interpolation between points i and i+1
        x0, x1 = x[i], x[i+1]
        y0, y1 = y[i], y[i+1]
        zeros.append(float(x0 - y0 * (x1 - x0) / (y1 - y0)))
    return np.array(zeros)

def packet_integral(x, y):
    """∫ y dlogx over [x0,x1]."""
    logx = np.log(x)
    return np.trapz(y, logx)

def main(csv_path):
    df = pd.read_csv(csv_path)
    x   = df["scale"].values
    R   = df["R"].values
    C   = df["C"].values
    eta = df["eta"].values
    G   = R - C

    zeros = find_zeros(x, G)
    if len(zeros) < 2:
        print("Fewer than two zero crossings → packet analysis skipped")
        return

    # smooth G in log-space to estimate curvature
    logx = np.log(x)
    Gs   = savgol_filter(G, 7, 3)
    G2   = np.gradient(np.gradient(Gs, logx), logx)  # 2nd derivative

    print("idx\t s*\t rho\t eta_packet\t kappa")
    for i, s_star in enumerate(zeros):
        # packet bounds
        if i == 0:
            left = x.min()
        else:
            left = zeros[i-1]
        if i == len(zeros)-1:
            right = x.max()
        else:
            right = zeros[i+1]

        # integrals within packet
        mask = (x >= left) & (x <= right)
        I_packet  = packet_integral(x[mask], (R + C)[mask])  # I = R + C
        E_packet  = packet_integral(x[mask], eta[mask]) / np.mean(eta[mask])
        eta_pkt   = I_packet / E_packet if E_packet else np.nan

        # curvature at zero (interpolate from pre-computed G2)
        kappa = np.interp(np.log(s_star), logx, G2)

        rho = zeros[i+1] / s_star if i < len(zeros)-1 else np.nan
        print(f"{i}\t {s_star:.3g}\t {rho:.3g}\t {eta_pkt:.3g}\t {kappa:.3g}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyze_packets.py <spectrum.csv>")
        sys.exit(1)
    main(sys.argv[1])