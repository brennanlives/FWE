#!/usr/bin/env python3
import sys, numpy as np, pandas as pd

# ---------- where to read / write ----------
if len(sys.argv) == 3:
    in_csv, out_csv = sys.argv[1:]
elif len(sys.argv) == 1:
    in_csv  = "data/ltee/ltee_fitness_full.csv"
    out_csv = "results/eta_microbe.csv"
else:
    sys.exit("usage: compute_eta_microbe.py <in.csv> <out.csv>")

print("reading", in_csv)
df = pd.read_csv(in_csv)

n = len(df)                  # one scale per row in the file
scale = np.arange(1, n+1)    # 1, 2, …, n
eta   = 1 / scale            # placeholder: monotonically smaller η

pd.DataFrame({"scale": scale, "eta": eta}).to_csv(out_csv, index=False)
print("saved  ", out_csv)
