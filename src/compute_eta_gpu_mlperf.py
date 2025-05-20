import sys, pathlib, pandas as pd, numpy as np

src, dst = map(pathlib.Path, sys.argv[1:3])
df = pd.read_csv(src, low_memory=False)

df["perf_units"] = df["perf_units"].fillna("")
df_perf  = df[df["perf_units"].str.contains("samples/s|tokens/s", case=False, regex=True)].copy()
df_power = df[df["perf_units"]=="W"].copy()

key = ["Public ID", "Scenario", "Benchmark", "SystemName"]  # join key
merged = pd.merge(df_perf, df_power, on=key, suffixes=("_perf","_pow"))

merged = merged[merged["Benchmark"].str.lower().eq("bert-99.9")]

bits_per_item = 384 * 32
merged["scale"] = merged["perf_result_perf"]          # tokens·s⁻¹
merged["eta"]   = bits_per_item * merged["perf_result_perf"] / merged["perf_result_pow"]

out = merged[["scale", "eta"]].sort_values("scale")
if out.empty:
    sys.exit("No (scale, eta) rows found – check filter criteria.")

out.to_csv(dst, index=False)
print(f"η spectrum written to {dst}  (rows={len(out)})")
