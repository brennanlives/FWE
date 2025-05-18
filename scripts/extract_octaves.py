#!/usr/bin/env python3
import os
from tifffile import imread, imsave

# 1. Load the 4D stack
stack = imread('data/imaging_raw/zebrafish_confocal_gastrulation.tif')

# 2. How many time frames?
frames = stack.shape[0]

# 3. Total minutes spanned (you may adjust if different)
# If each frame is, say, 2 minutes apart, total_minutes = frames * 2
# Replace 2 with your actual minutes-per-frame if known.
minutes_per_frame = 2.00014713
total_minutes = frames * minutes_per_frame

# 4. Define the eight octaves (in minutes)
octaves = [1, 2, 4, 8, 16, 32, 64, total_minutes]

# 5. Map each octave to a frame index
frame_to_min = total_minutes / frames
frame_indices = [min(frames - 1, int(m / frame_to_min)) for m in octaves]

# 6. Prepare output folder
out_dir = 'data/imaging_processed/octave_frames'
os.makedirs(out_dir, exist_ok=True)

# 7. Extract and save each octave frame (middle Z-slice if 3D per time)
for ℓ, idx in zip(octaves, frame_indices):
    if stack.ndim == 4:
        img = stack[idx, stack.shape[1] // 2]
    else:
        img = stack[idx]
    out_path = os.path.join(out_dir, f'frame_{ℓ}min.tif')
    imsave(out_path, img)
    print(f"Saved {out_path}")
