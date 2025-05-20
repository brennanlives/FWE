import sys, pandas as pd, pathlib
src, dst = map(pathlib.Path, sys.argv[1:3])
df = pd.read_csv(src, low_memory=False)

model_col = "Model"
perf_col  = "Result_perf"   # throughput
power_col = "Result_power"  # average power W

df = df[df[model_col].str.lower().eq("bert-99.9")].copy()
bits = 384 * 32
df["scale"] = df[perf_col]
df["eta"]   = bits * df[perf_col] / df[power_col]

out = df[["scale","eta"]].sort_values("scale")
if out.empty:
    sys.exit("No BERT-99.9 rows found in raw_data.csv")

out.to_csv(dst, index=False)
print(f"η spectrum written to {dst}  (rows = {len(out)})")
