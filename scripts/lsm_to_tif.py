from tifffile import imread, imsave
stack = imread('data/imaging_raw/zebrafish_confocal_gastrulation.lsm')
imsave('data/imaging_raw/zebrafish_confocal_gastrulation.tif', stack)
print("Conversion complete: data/imaging_raw/zebrafish_confocal_gastrulation.tif")
