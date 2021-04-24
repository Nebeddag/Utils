import os

dir_path = '/mnt/Data/Datasets/cleaning/detected_mb_384_ch12/0'
fraction = 2

files = os.listdir(dir_path)

for i, f in enumerate(files):
    if i % fraction != 0:
        os.remove(os.path.join(dir_path, f))