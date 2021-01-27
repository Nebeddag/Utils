import os

dirname = '/mnt/Data/Datasets/cleaning'

for (dirpath, dirnames, filenames) in os.walk(dirname):
    for f in filenames:
        nn = f.replace(':','_')
        if nn != f:
            fpo = os.path.join(dirpath, f)
            fpn = os.path.join(dirpath, nn)
            os.rename(fpo, fpn)