#!/usr/bin/env python3
import pandas as pd, numpy as np, matplotlib.pyplot as plt
ent = pd.read_csv('data/entropy_by_octave.csv')
ene = pd.read_csv('data/energy_by_octave.csv')
df  = ent.merge(ene, on='octave_min').sort_values('octave_min')
df['eta'] = df['entropy'] / df['delta_E']
df['delta_H'] = df['entropy'].diff().fillna(0)
df['DS_sign'] = np.where(df['delta_H'] > 0, 1, -1)
df.to_csv('data/efficiency_by_octave.csv', index=False)
print('Saved data/efficiency_by_octave.csv')
plt.loglog(df['octave_min'], df['eta'], marker='o')
for x,y,s in zip(df['octave_min'], df['eta'], df['DS_sign']):
    plt.text(x, y, '+' if s>0 else '–')
plt.xlabel('Scale ℓ (min)'); plt.ylabel('η (bits/J)')
plt.title('FWE Spectrum'); plt.grid(True, which='both', ls='--')
plt.savefig('data/eta_spectrum.png', dpi=300)
