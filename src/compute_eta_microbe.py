"""Compute η-spectrum for the LTEE fitness trajectory (Dryad CSV).

Input   : data/ltee/ltee_fitness_full.csv
          Header begins:
          Generation,Red.Pop,White.Pop,…,D.1,**Fitness**,Complete,…

Output  : results/eta_microbe.csv  — columns  scale, eta
"""
from __future__ import annotations
import pandas as pd
import numpy as np
from eta_core import eta_spectrum            # helper already in src/

# -------------------------------------------------------------------------
RAW = "data/ltee/ltee_fitness_full.csv"
OUT = "results/eta_microbe.csv"
# -------------------------------------------------------------------------


def main() -> None:
    df = pd.read_csv(RAW)

    # Energy proxy — cumulative generations (one glucose pulse per gen)
    energy_in = df["Generation"]

    # Structure proxy — observed relative fitness
    structure = df["Fitness"]                # ← correct column name

    eta = eta_spectrum(energy_in, structure)

    # --------------------------------------------------------------
    # Compute recursion (R) and compression (C) alongside efficiency
    # --------------------------------------------------------------
    # Incremental energy: assume 1 J per generation
    ΔE = np.gradient(energy_in.values.astype(float))            # J

    # Incremental entropy change: finite‑difference on fitness
    ΔH = np.gradient(structure.values.astype(float))            # bits

    R_vals = np.maximum(0.0,  ΔH) / ΔE                          # bits · J⁻¹
    C_vals = np.maximum(0.0, -ΔH) / ΔE                          # bits · J⁻¹

    # Build the output DataFrame expected by downstream diagnostics
    df_out = pd.DataFrame({
        "scale": eta["scale"],
        "R":     R_vals,
        "C":     C_vals,
        "eta":   eta["eta"]
    })
    df_out.to_csv(OUT, index=False)
    print(f"η-spectrum written to {OUT}")


if __name__ == "__main__":
    main()
