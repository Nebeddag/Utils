import random

from os import listdir
from os.path import isfile, join
from shutil import copyfile

cfgs = []

cfgs.append({
    'in': r'D:\Datasets\cleaning\TR-D3223WDZIR3_1\found\person_f',
    'out': r'D:\Datasets\cleaning\TR-D3223WDZIR3_1\found\final\person',
    'count': 500
})
cfgs.append({
    'in': r'D:\Datasets\cleaning\TR-D3223WDZIR3_1\found\person_t',
    'out': r'D:\Datasets\cleaning\TR-D3223WDZIR3_1\found\final\person',
    'count': 300
})
cfgs.append({
    'in': r'D:\Datasets\cleaning\TR-D3223WDZIR3_1\found\cleaner_f',
    'out': r'D:\Datasets\cleaning\TR-D3223WDZIR3_1\found\final\cleaner',
    'count': 20
})
cfgs.append({
    'in': r'D:\Datasets\cleaning\TR-D3223WDZIR3_1\found\cleaner_t',
    'out': r'D:\Datasets\cleaning\TR-D3223WDZIR3_1\found\final\cleaner',
    'count': 180
})
cfgs.append({
    'in': r'D:\Datasets\cleaning\TR-D3223WDZIR3_1\found\cwu_f',
    'out': r'D:\Datasets\cleaning\TR-D3223WDZIR3_1\found\final\cwu',
    'count': 50
})
cfgs.append({
    'in': r'D:\Datasets\cleaning\TR-D3223WDZIR3_1\found\cwu_t',
    'out': r'D:\Datasets\cleaning\TR-D3223WDZIR3_1\found\final\cwu',
    'count': 50
})

for cfg in cfgs:
    inp, out, cnt = cfg['in'], cfg['out'], cfg['count']
    files = random.sample(listdir(inp), cnt)
    for f in files:
        if isfile(join(inp, f)):
            copyfile(join(inp, f), join(out, f))