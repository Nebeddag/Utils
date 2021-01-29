import random
import glob, os
import errno
import uuid

init_dir = '/media/cundo/HardDisk_01/Data/zone247/LabledData/train'
export_dir = '/media/cundo/HardDisk_01/Data/zone247/LabledData/test'

ext1 = 'jpg'
ext2 = 'xml'

export_fraction = 0.2

for (dirpath, dirnames, filenames) in os.walk(init_dir):
    target_fns = [f for f in filenames if f.endswith('.' + ext1)]

    newdir = dirpath.replace(init_dir,export_dir)

    if not os.path.exists(newdir):
        os.makedirs(newdir)

    if len(target_fns) == 0:
        continue

    fs_cnt = int(len(target_fns) * export_fraction)
    moving_files = random.sample(target_fns, fs_cnt)
    for f in moving_files:
        f_old = os.path.join(dirpath, f)
        f_new = f_old.replace(init_dir, export_dir)
        os.rename(f_old, f_new)
        os.rename(f_old.replace('.'+ext1, '.'+ext2), f_new.replace('.'+ext1, '.'+ext2))
    

