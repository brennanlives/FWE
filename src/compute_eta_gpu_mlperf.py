import sys, pathlib, pandas as pd

inf_path, pwr_path, out_path = map(pathlib.Path, sys.argv[1:4])
inf = pd.read_csv(inf_path, low_memory=False)
pwr = pd.read_csv(pwr_path, low_memory=False)

key = ["Public ID", "Scenario", "SystemName", "Model"]

inf = inf[inf["Model"].str.fullmatch(r"(?i)bert-99\.9", na=False)]
pwr = pwr[pwr["Model"].str.fullmatch(r"(?i)bert-99\.9", na=False)]

merged = pd.merge(inf, pwr[key + ["avg_power_w"]], on=key, how="inner")
bits = 384 * 32            # one BERT token = 384×32 bits
merged["scale"] = merged["Result"]          # tokens · s⁻¹
merged["eta"]   = bits * merged["Result"] / merged["avg_power_w"]

out = merged[["scale", "eta"]].dropna().sort_values("scale")
if out.empty:
    sys.exit("No matching rows with power data found.")
out.to_csv(out_path, index=False)
print(f"η spectrum → {out_path}   rows={len(out)}")
