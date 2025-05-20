import sys, pathlib, pandas as pd

src, dst = map(pathlib.Path, sys.argv[1:3])
df = pd.read_csv(src, low_memory=False)          # raw_data.csv

# ── isolate the rows we need ─────────────────────────────────────────────
is_bert   = df["Model"].str.contains("bert", case=False, na=False)
is_power  = df["perf_units"].str.strip().eq("W")
is_rate   = df["perf_units"].str.contains(r"/s",  na=False)   # tokens/s or samples/s

perf  = df[is_bert & is_rate ].copy()            # throughput rows
power = df[is_bert & is_power].copy()            # average-power rows

key = ["Public ID", "Scenario", "SystemName", "Model"]        # join key
merged = pd.merge(perf, power, on=key, suffixes=("_perf", "_pow"))

# ── compute η  (bits · J⁻¹) ─────────────────────────────────────────────
bits = 384 * 32                                  # one BERT token = 384×32 bits
merged["scale"] = merged["perf_result_perf"]     # tokens s⁻¹
merged["eta"]   = bits * merged["perf_result_perf"] / merged["perf_result_pow"]

out = merged[["scale", "eta"]].sort_values("scale")
out.to_csv(dst, index=False)
print(f"η spectrum written to {dst}  (rows = {len(out)})")
