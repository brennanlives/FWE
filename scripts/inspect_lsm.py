#!/usr/bin/env python3
from tifffile import TiffFile
# Path to your raw LSM stack
path = 'data/imaging_raw/zebrafish_confocal_gastrulation.lsm'
with TiffFile(path) as tif:
    # Number of time points
    frames = tif.series[0].shape[0]
    print(f"Number of time points (frames): {frames}")

  # Try LSM metadata field for time interval (note the spelling in this file)
    ti = tif.lsm_metadata.get('TimeIntervall') or tif.lsm_metadata.get('TimeInterval')
    print(f"LSM metadata TimeIntervall (seconds per frame): {ti}")
cd ~/projects/FWE_morphogenesis
mkdir -p scripts

cat > scripts/inspect_lsm.py << 'EOF'
#!/usr/bin/env python3
from tifffile import TiffFile

# Path to your raw LSM stack
path = 'data/imaging_raw/zebrafish_confocal_gastrulation.lsm'

with TiffFile(path) as tif:
    # Number of time points
    frames = tif.series[0].shape[0]
    print(f"Number of time points (frames): {frames}")

    # Try LSM metadata field for time interval (note the spelling in this file)
    ti = tif.lsm_metadata.get('TimeIntervall') or tif.lsm_metadata.get('TimeInterval')
    print(f"LSM metadata TimeIntervall (seconds per frame): {ti}")

    # If explicit time stamps are present, infer dt
    stamps = tif.lsm_metadata.get('TimeStamps', None)
    if stamps:
        # TimeStamps are given in seconds
        dt = stamps[1] - stamps[0]
        print(f"First two TimeStamps: {stamps[0]}, {stamps[1]} → Δt = {dt} s")
    else:
        print("No TimeStamps array found in LSM metadata.")

    # Fallback: check ImageJ (OME) metadata
    ij = tif.imagej_metadata
    if ij and 'spacing' in ij:
        print(f"ImageJ metadata spacing (s): {ij['spacing']}")
    elif ij:
        print("ImageJ metadata present but no 'spacing' field.")

    # If we still lack dt, alert
    if ti is None and not stamps and not (ij and 'spacing' in ij):
        print("Warning: could not find frame interval automatically.")
