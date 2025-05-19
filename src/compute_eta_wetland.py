"""Compute η-spectrum for AmeriFlux US-Los wetland (half-hourly CSV)."""
from __future__ import annotations
import pandas as pd
from eta_core import eta_spectrum

RAW = "data/ameriflux/US-Los/AMF_US-Los_BIF_20230331.xlsx", sheet_name=0"
OUT = "results/eta_wetland.csv"

def main() -> None:
    # 1 ─ read the file, ignoring comment lines that start with “#”
    df = pd.read_csv(RAW, comment="#")

    # 2 ─ build a datetime index from TIMESTAMP_START (yyyymmddHHMM)
    df["time"] = pd.to_datetime(df["TIMESTAMP_START"], format="%Y%m%d%H%M")
    df = df.set_index("time")

    # 3 ─ select sensible-heat and NEE columns that *exist*
    H_col   = "H_1_1_1"                 # sensible-heat flux (W m⁻²)
    NEE_col = "NEE_PI_F"                # gap-filled NEE (µmol CO₂ m⁻² s⁻¹)
    if H_col not in df.columns or NEE_col not in df.columns:
        raise ValueError("Expected H_1_1_1 or NEE_PI_F not found in US-Los file")

    energy_in = df[H_col]
    structure = -df[NEE_col]            # uptake → positive

    eta = eta_spectrum(energy_in, structure)
    eta.to_csv(OUT, index=False)
    print(f"η-spectrum written to {OUT}")

if __name__ == "__main__":
    main()
