#!/usr/bin/env python3
"""
Compute single-scale η for MLPerf Inference v5.0 Closed-Power runs
using data/raw/inference_v5_full.csv
"""
import pandas as pd

# 1. load CSV, skipping the first “Table – …” label row
df = pd.read_csv('data/raw/inference_v5_full.csv', skiprows=1)

# 2. tidy column names
df.columns = df.columns.str.strip()

# 3. separate throughput rows (Tokens/s, Samples/s, Queries/s, …) and power rows (Watts)
thr = df[df['Units'].str.contains(r'/s', na=False)]
pwr = df[df['Units'] == 'Watts']

# 4. align on System × Scenario × Model
key_cols = ['System Name (click + for details)', 'Scenario', 'Model MLC']
thr = thr.set_index(key_cols)
pwr = pwr.set_index(key_cols)

# 5. inner-join the matched pairs
merged = thr[['Result']].join(
    pwr[['Result']],
    how='inner',
    lsuffix='_thr',
    rsuffix='_watts'
)

# 6. η = (bits per unit × throughput) / power
BITS_PER_UNIT = 384 * 32        # 384 tokens × 32 bits
merged['eta'] = (BITS_PER_UNIT * merged['Result_thr']) / merged['Result_watts']

# 7. save
out = merged.reset_index()[key_cols + ['eta']]
out.to_csv('data/processed/edge_eta_single_scale.csv', index=False)
print('✓  wrote data/processed/edge_eta_single_scale.csv')