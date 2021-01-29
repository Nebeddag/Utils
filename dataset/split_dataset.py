import random
import glob, os
import errno
import uuid

init_dir = '/home/cundo/Work/Cleaning/TLT_Share/classifier_dataset/train'

export_cfgs = []
export_cfgs.append(('/home/cundo/Work/Cleaning/TLT_Share/classifier_dataset/val', 0.15))
export_cfgs.append(('/home/cundo/Work/Cleaning/TLT_Share/classifier_dataset/test', 0.15))

for (dirpath, dirnames, filenames) in os.walk(init_dir):
    fnames_left = filenames.copy()
    random.shuffle(fnames_left)

    for export_dir, export_fraction in export_cfgs:
        newdir = dirpath.replace(init_dir, export_dir)
        if not os.path.exists(newdir):
            os.makedirs(newdir)

        if len(filenames) == 0:
            continue

        fs_cnt = int(len(filenames) * export_fraction)
        moving_files = fnames_left[0:fs_cnt]
        fnames_left = fnames_left[fs_cnt:]

        for f in moving_files:
            f_old = os.path.join(dirpath, f)
            f_new = f_old.replace(init_dir, export_dir)
            os.rename(f_old, f_new)
    
print('done')