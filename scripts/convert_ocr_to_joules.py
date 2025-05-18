#!/usr/bin/env python3
import pandas as pd
df = pd.read_csv('data/o2_raw.csv')
df['minutes_post_fertilization'] = df['hours_post_fert'] * 60
df['joules'] = df['ocr_pmol_per_min'] * 1e-12 * 470_000  # 470 kJ per mol O2
df[['minutes_post_fertilization','joules']].to_csv('data/o2_curves.csv', index=False)
print('Saved data/o2_curves.csv')
