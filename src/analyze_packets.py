#!/usr/bin/env python3
"""
Minimal diagnostic that works with either format:
   scale, eta
or scale, eta, R, C

If R/C missing, it computes sign(∂η/∂log s) as a proxy.
"""

import sys, numpy as np, pandas as pd

def main(path):
    df = pd.read_csv(path)

    s   = df["scale"].values
    eta = df["eta"].values

    if {"R","C"}.issubset(df.columns):
        R = df["R"].values
        C = df["C"].values
        note = "R/C present"
    else:
        slope = np.gradient(np.log(eta), np.log(s))
        R = np.maximum( 0, slope)
        C = np.maximum( 0,-slope)
        note = "fallback from slope sign"

    out = pd.DataFrame({"scale":s, "eta":eta, "R":R, "C":C})
    print(f"{path} — {note}\n", out.to_string(index=False))

if __name__ == "__main__":
    if len(sys.argv)!=2:
        sys.exit("usage: analyze_packets.py <eta.csv>")
    main(sys.argv[1])
