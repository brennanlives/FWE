#!/usr/bin/env python3
"""
compute_eta_gpu.py  <inference_full.csv> <out.csv>

Reads the MLPerf “Full Data” sheet, pairs every Tokens/s (throughput)
row with its matching Watts row (same System Name & Scenario),
then computes η = (bits_per_token · throughput) / power.

Bits per BERT-99.9 token: 384×32 = 12288 bits.
"""

import sys, pandas as pd, numpy as np

if len(sys.argv) != 3:
    sys.exit("usage: compute_eta_gpu.py <mlperf_full.csv> <out.csv>")

in_csv, out_csv = sys.argv[1:]
bits_per_token = 384 * 32      # = 12288

df   = pd.read_csv(in_csv, skiprows=1, engine="python")
want = df["Model MLC"] == "BERT-99.9"
df   = df[want]

# keep only Tokens/s and Watts rows
tok  = df[df["Units"].str.contains("/s")]
watt = df[df["Units"].str.contains("W")]
key  = ["Public ID", "System Name (click + for details)", "Scenario"]

tok  = tok.set_index(key)["Result at System Name"].astype(float)
watt = watt.set_index(key)["Result at System Name"].astype(float)

paired = tok.to_frame("throughput").join(watt.to_frame("power"))
paired = paired.dropna()                 # keep only rows where both exist
paired["eta"] = bits_per_token * paired["throughput"] / paired["power"]

# write scale = rank (1,2,…) so analyzer works
paired = paired.sort_values("eta", ascending=False)
paired.reset_index(drop=True, inplace=True)
paired["scale"] = np.arange(1, len(paired)+1)

paired[["scale", "eta"]].to_csv(out_csv, index=False)
print("wrote", out_csv)
