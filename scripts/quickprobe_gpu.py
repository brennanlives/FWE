#!/usr/bin/env python3
"""
Compute entropy–energy spectrum for an MLPerf GPU trace
and write data/gpu_efficiency.csv
"""
import json
import pandas as pd
import numpy as np
from skimage.filters.rank import entropy
from skimage.morphology import disk
with open('data/gpu_power.json') as f:
    js = json.load(f)
df = pd.DataFrame(js['power_samples'])  # expects fields timestamp_ms, power_w, throughput
octaves = np.array([
    1, 2, 4, 8, 16, 32, 64,
    df['timestamp_ms'].max() / 60000.0
])

H = []
for l in octaves:
    cutoff = int(l * 60 * 1000)
    window = df.loc[df['timestamp_ms'] < cutoff, 'throughput'].astype(np.uint16)
    H.append(entropy(window, disk(3)).mean())
E = []
for l in octaves:
    cutoff = int(l * 60 * 1000)
    P = df.loc[df['timestamp_ms'] < cutoff, 'power_w']
    E.append(P.mean() * l)
out = pd.DataFrame({
    'octave_min': octaves,
    'entropy':     H,
    'delta_E':     E
})
out.to_csv('data/gpu_efficiency.csv', index=False)
print("✓  wrote data/gpu_efficiency.csv")
