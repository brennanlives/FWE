#!/usr/bin/env python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Load the GPU efficiency raw table
df = pd.read_csv('data/gpu_efficiency.csv')  # octave_min, entropy, delta_E

# 2. Compute η = H / ΔE
df['eta'] = df['entropy'] / df['delta_E']

# 3. Compute ΔS sign
df['delta_H'] = df['entropy'].diff().fillna(0)
df['DS_sign'] = np.sign(df['delta_H'])

# 4. Save processed table
df.to_csv('data/gpu_efficiency_processed.csv', index=False)

# 5. Plot log–log η(ℓ)
plt.figure()
plt.loglog(df['octave_min'], df['eta'], marker='o')
for x, y, s in zip(df['octave_min'], df['eta'], df['DS_sign']):
    plt.text(x, y, '+' if s>0 else '–' if s<0 else '0')
plt.xlabel('Scale l (min)')
plt.ylabel('η (bits · J⁻¹)')
plt.title('GPU FWE Spectrum')
plt.grid(True, which='both', ls='--')
plt.savefig('data/gpu_eta_spectrum.png', dpi=300)
print('✓  Saved data/gpu_efficiency_processed.csv and data/gpu_eta_spectrum.png')
