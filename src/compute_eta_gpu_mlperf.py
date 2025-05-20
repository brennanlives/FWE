import sys, pandas as pd, pathlib
src, dst = map(pathlib.Path, sys.argv[1:3])
df = pd.read_csv(src, low_memory=False)

# file already has one row per run with these canonical columns
perf_col  = "throughput"      # tokens/s or samples/s
power_col = "avg_power_w"     # W
model_col = "benchmark"       # e.g. bert-99.9

df = df[df[model_col].str.lower().eq("bert-99.9")].copy()
bits = 384*32
df["scale"] = df[perf_col]
df["eta"]   = bits * df[perf_col] / df[power_col]

out = df[["scale","eta"]].sort_values("scale")
if out.empty:
    sys.exit("No matching BERT-99.9 rows – confirm column names with head -n 1.")

out.to_csv(dst, index=False)
print(f"η spectrum written to {dst}  (rows={len(out)})")
