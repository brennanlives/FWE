#!/usr/bin/env python3
import sys, numpy as np, pandas as pd
def compute_eta(fit):
    c = fit.value_counts().values
    p = c / c.sum()
    H = -np.sum(p * np.log2(p + 1e-12))
    return np.full(len(fit), np.exp2(H) / len(c))
if len(sys.argv) != 3:
    print("usage: python3 src/compute_eta_microbe.py <in.csv> <out.csv>"); sys.exit(1)
infile, outfile = sys.argv[1:]
df = pd.read_csv(infile)
eta = compute_eta(df["Fitness"])
pd.DataFrame({"scale": np.arange(len(eta)) + 1, "eta": eta}).to_csv(outfile, index=False)
print("saved", outfile)
