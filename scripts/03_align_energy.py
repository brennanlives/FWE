#!/usr/bin/env python3
import numpy as np, pandas as pd

ent = pd.read_csv("data/entropy_by_octave.csv")
octaves = ent["octave_min"].astype(float).tolist()           # ensure float list

o2 = pd.read_csv("data/o2_curves.csv")
power_series = o2.set_index("minutes_post_fertilization")["joules"]  # J min⁻¹
power_interp = np.interp(octaves, power_series.index, power_series.values)

energy = power_interp * np.asarray(octaves, dtype=float)     # J over the window

pd.DataFrame({"octave_min": octaves, "delta_E": energy}).to_csv(
    "data/energy_by_octave.csv", index=False)
print("✓  Saved data/energy_by_octave.csv (window-scaled)")
