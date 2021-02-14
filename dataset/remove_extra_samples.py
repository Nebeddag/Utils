import os

dir_path = '/mnt/Data/Datasets/cleaning/0475-1_02/per_t'
fraction = 5

files = os.listdir(dir_path)

for i, f in enumerate(files):
    if i % fraction != 0:
        os.remove(os.path.join(dir_path, f))