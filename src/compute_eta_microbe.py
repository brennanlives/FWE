#!/usr/bin/env python3
import sys, numpy as np, pandas as pd
from eta_core import eta_spectrum   # already in repo

if len(sys.argv) == 3:
    in_csv, out_csv = sys.argv[1:]
elif len(sys.argv) == 1:
    in_csv  = "data/ltee/ltee_fitness_full.csv"
    out_csv = "results/eta_microbe.csv"
else:
    sys.exit("usage: python3 src/compute_eta_microbe.py <in.csv> <out.csv>")

print(f"reading  {in_csv}")
df = pd.read_csv(in_csv)

# fitness column name in the LTEE file
structure = pd.Series(df["Fitness"].values, name="structure")
energy    = pd.Series(np.ones(len(structure)),    name="energy")   # placeholder

scale, eta = eta_spectrum(structure, energy)
pd.DataFrame({"scale": scale, "eta": eta}).to_csv(out_csv, index=False)
print(f"saved    {out_csv}")
