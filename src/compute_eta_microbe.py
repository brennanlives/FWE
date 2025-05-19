#!/usr/bin/env python3
import sys, pandas as pd, numpy as np
from eta_core import eta_spectrum         # already in repo

# ---------- argument handling ----------
if len(sys.argv) == 3:
    in_csv, out_csv = sys.argv[1:]
elif len(sys.argv) == 1:
    in_csv  = "data/ltee/ltee_fitness_full.csv"
    out_csv = "results/eta_microbe.csv"
else:
    sys.exit("usage: python3 src/compute_eta_microbe.py <in.csv> <out.csv>")

print(f"reading  {in_csv}")
df = pd.read_csv(in_csv)
structure = pd.Series(df["Fitness"].values)
s_len = len(structure)
s      = np.arange(1, s_len+1)
eta     = 1/s      # placeholder

s, eta = eta_spectrum(structure, energy)
pd.DataFrame({"scale": s, "eta": eta}).to_csv(out_csv, index=False)
print(f"saved    {out_csv}")
