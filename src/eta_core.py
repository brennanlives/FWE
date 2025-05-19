"""
eta_core.py – minimal helper for Fractal-Weighted Efficiency examples.
Provides eta_spectrum(energy_in, structure_out) → DataFrame[scale, eta].

For now η is a simple signal-to-signal ratio across logarithmic
window sizes; swap in your full mutual-information version later.
"""
from __future__ import annotations
import numpy as np
import pandas as pd


def _windowed_mean(series: pd.Series, window: int) -> pd.Series:
    """Rolling mean with window size `window`, aligned to the right edge."""
    return series.rolling(window, min_periods=window).mean()


def eta_spectrum(
    energy_in: pd.Series,
    structure_out: pd.Series,
    min_exp: int = 2,
    max_exp: int = 8,
) -> pd.DataFrame:
    """
    Compute a toy η-spectrum on dyadic window sizes 2**k, k = min_exp … max_exp.

    Parameters
    ----------
    energy_in      : pd.Series — input-energy time-series (same length as output)
    structure_out  : pd.Series — output-structure time-series
    min_exp, max_exp : int     — smallest and largest window exponents

    Returns
    -------
    pd.DataFrame with columns  'scale' (window length)  and  'eta'
    """
    if len(energy_in) != len(structure_out):
        raise ValueError("energy_in and structure_out must be the same length")

    scales, etas = [], []
    for k in range(min_exp, max_exp + 1):
        w = 2 ** k
        e_mean = _windowed_mean(energy_in, w)
        s_mean = _windowed_mean(structure_out, w)
        e_mean = e_mean.replace(0, np.nan)
        ratio  = (s_mean / e_mean).dropna()
        if ratio.empty:
            continue
        scales.append(w)
        etas.append(ratio.mean())          # crude aggregate

    return pd.DataFrame({"scale": scales, "eta": etas})
