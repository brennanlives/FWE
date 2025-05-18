#!/usr/bin/env python3
import os
import numpy as np
import pandas as pd
from skimage.io import imread
from skimage.filters.rank import entropy
from skimage.morphology import disk

# Directory containing the octave frames
FRAMES_DIR = 'data/imaging_processed/octave_frames'
OUTPUT_CSV = 'data/entropy_by_octave.csv'

# Define the eight octave scales (in minutes)
octaves = [1, 2, 4, 8, 16, 32, 64, 302]  # replace 302 if you recompute total_minutes

results = []
for fname in sorted(os.listdir(FRAMES_DIR)):
    if not fname.endswith('.tif'): 
        continue
    # Extract ℓ (minutes) from filename, e.g. 'frame_8min.tif' → 8
    ℓ = float(fname.split('_')[1].rstrip('min.tif'))
    img = imread(os.path.join(FRAMES_DIR, fname))
    # Compute texture‐entropy (mean over the image)
    H = entropy(img, disk(3)).mean()
    results.append({'octave_min': ℓ, 'entropy': H})

# Aggregate (one row per octave) and save
df = pd.DataFrame(results).sort_values('octave_min')
df.to_csv(OUTPUT_CSV, index=False)
print(f"Saved entropy per octave to {OUTPUT_CSV}")
