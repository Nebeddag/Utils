import random
import os

init_dir = '/mnt/Data/Datasets/cleaning/detected_mb_496_all'
out_dir = '/mnt/Data/Datasets/cleaning/detected_mb_496_ch04'
substr = '_CH04_'


for (dirpath, dirnames, filenames) in os.walk(init_dir):
    fnames_left = filenames.copy()
    random.shuffle(fnames_left)

    newdir = dirpath.replace(init_dir, out_dir)
    if not os.path.exists(newdir):
        os.makedirs(newdir)

    if len(filenames) == 0:
        continue

    for f in filenames:
        if substr in f:
            f_old = os.path.join(dirpath, f)
            f_new = f_old.replace(init_dir, out_dir)
            os.rename(f_old, f_new)
    
print('done')