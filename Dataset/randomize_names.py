from shutil import copyfile

from os import listdir
from os.path import isfile, join
import uuid

s_path = '/media/cundo/HardDisk_01/Datasets/cleaning_data/test/person'
d_path = '/media/cundo/HardDisk_01/Datasets/cleaning_data/all/person'

for f in listdir(s_path):
    if isfile(join(s_path, f)):
        nn = uuid.uuid4().hex + f[-4:]
        copyfile(f'{s_path}/{f}', f'{d_path}/{nn}')
        pass