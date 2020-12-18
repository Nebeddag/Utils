from shutil import copyfile

import os
from os.path import isfile, join
import uuid

s_path = '/media/cundo/HardDisk_01/Datasets/cleaning_data/final'
d_path = '/media/cundo/HardDisk_01/Data/zone247/LabledData'

ext_white_list = ['jpg', 'xml']
ext_black_list = []

all_files = []

for (dirpath, dirnames, filenames) in os.walk(s_path):
    for f in filenames:
        all_files.append((dirpath, f))

for d, f in all_files:
    f_dest = f
    f_ext = f.split('.')[-1]
    f_name = f[0:len(f)-len(f_ext)-1]

    if len(ext_black_list) > 0 and f_ext in ext_black_list:
        continue

    if len(ext_white_list) > 0 and f_ext not in ext_white_list:
        continue

    i = 0
    while isfile(join(d_path, f_dest)):
        i += 1
        f_dest = f'{f_name} ({str(i)}).{f_ext}'

    copyfile(os.path.join(d,f), os.path.join(d_path,f_dest))