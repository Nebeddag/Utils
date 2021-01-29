from shutil import copyfile

from os import listdir
from os.path import isfile, join
import uuid

s_path = '/media/cundo/HardDisk_01/Datasets/cleaning_data/test/person'
d_path = '/media/cundo/HardDisk_01/Datasets/cleaning_data/all/person'

for (dirpath, dirnames, filenames) in os.walk(init_dir):
    filenames_randomized = []
    for f in filenames:
        nf = f"{uuid.uuid4().hex}.{f.split('.')[-1]}"
        f_old = os.path.join(dirpath, f)
        f_new = f_old.replace(f, nf)
        os.rename(f_old, f_new)

# for f in listdir(s_path):
#     if isfile(join(s_path, f)):
#         nn = uuid.uuid4().hex + f[-4:]
#         copyfile(f'{s_path}/{f}', f'{d_path}/{nn}')
#         pass