import random
import glob, os
import errno
import uuid

init_dir = '/media/cundo/HardDisk_01/Datasets/cleaning_data/ForReport/train'
export_dir = '/media/cundo/HardDisk_01/Datasets/cleaning_data/ForReport/test'

export_fraction = 0.2
randomize_names = True

for (dirpath, dirnames, filenames) in os.walk(init_dir):
    newdir = dirpath.replace(init_dir,export_dir)

    if not os.path.exists(newdir):
        os.makedirs(newdir)

    if len(filenames) == 0:
        continue

    if randomize_names:
        filenames_randomized = []
        for f in filenames:
            nf = f"{uuid.uuid4().hex}.{f.split('.')[-1]}"
            filenames_randomized.append(nf)
            f_old = os.path.join(dirpath, f)
            f_new = f_old.replace(f, nf)
            os.rename(f_old, f_new)
        filenames = filenames_randomized

    fs_cnt = int(len(filenames) * export_fraction)
    moving_files = random.sample(filenames, fs_cnt)
    for f in moving_files:
        f_old = os.path.join(dirpath, f)
        f_new = f_old.replace(init_dir, export_dir)
        os.rename(f_old, f_new)
    

