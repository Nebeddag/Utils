import random
import glob, os
import errno

init_dir = '/media/cundo/HardDisk_01/Datasets/cleaning_data/ForReport/train'
export_dir = '/media/cundo/HardDisk_01/Datasets/cleaning_data/ForReport/test'

export_fraction = 0.2

for (dirpath, dirnames, filenames) in os.walk(init_dir):

    files = [dirpath + '/' + fn for fn in filenames]
    newdir = dirpath.replace(init_dir,export_dir)

    if len(files) == 0:
        continue

    if not os.path.exists(newdir):
        os.makedirs(newdir)
    fs_cnt = int(len(files) * export_fraction)
    moving_files = random.sample(files, fs_cnt)
    for f in moving_files:
        f_new = f.replace(init_dir, export_dir)
        os.rename(f, f_new)
    

