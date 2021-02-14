import os

dirpath = '/mnt/HardDisk_01/Datasets/cleaning_data/detected/0'

files = os.listdir(dirpath)

for i, f in enumerate(files):
    if i % 50 != 0:
        os.remove(os.path.join(dirpath, f))