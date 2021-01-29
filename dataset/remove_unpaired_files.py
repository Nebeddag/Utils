import os
from os.path import isfile, join
import uuid

dir_path = '/media/cundo/HardDisk_01/Datasets/cleaning_data/final'

paired_extensions = ['jpg', 'xml']

for (dirpath, dirnames, filenames) in os.walk(dir_path):
    for f in filenames:
        if f.endswith('.' + paired_extensions[0]):
            if isfile(os.path.join(dirpath, f.replace(paired_extensions[0], paired_extensions[1]))):
                continue
        if f.endswith('.' + paired_extensions[1]):
            if isfile(os.path.join(dirpath, f.replace(paired_extensions[1], paired_extensions[0]))):
                continue
        os.remove(os.path.join(dirpath, f))