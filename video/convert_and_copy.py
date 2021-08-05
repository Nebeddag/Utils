# %%
from genericpath import isfile
from collections import defaultdict
import os

init_dir = '/mnt/Data/Datasets/cleaning_srb'
out_dir = '/mnt/Data/Datasets/cleaning_srb/out'

# %%
import base64

def isBase64(s):
    try:
        return base64.b64encode(base64.b64decode(s)) == s
    except Exception:
        return False


# %%
dirs = [os.path.join(init_dir, name) for name in os.listdir(init_dir) if os.path.isdir(os.path.join(init_dir, name))]
dirs_files = {}

for d in dirs:
    files = [name.split('._') for name in os.listdir(d) if os.path.isfile(os.path.join(d, name)) and '._' in name]
    files = sorted(files, key=lambda f: (int(f[1].replace('_', ''), 16), int(f[0], 16)))
    dirs_files[d] = files

# %%
dirs_files_grouped = {}
for d in dirs_files:
    ddict = defaultdict(list)
    for k, v in dirs_files[d]:
        ddict[v].append(k)
    dirs_files_grouped[d] = ddict


# %%
gr_fnames = []

for d in dirs_files_grouped:
    for i, gr in enumerate(dirs_files_grouped[d]):
        # Only this group works
        if gr != '02':
            continue
        fn = os.path.join(d, f'files_{i}.txt')
        #gr_fnames.append((gr, d, f'files_{i}.txt'))
        gr_fnames.append((d.split('/')[-1].replace(' ', '_'), d, f'files_{i}.txt'))
        with open(fn, 'w') as text_file:
            for f in dirs_files_grouped[d][gr]:
                text_file.write(f'file {f}._{gr}\r')


# %%
import subprocess

for gr, dn, fn in gr_fnames:
    fn_in = os.path.join(dn, fn)
    fn_out = os.path.join(out_dir, f'{gr}.mp4')
    #subprocess.call(f'ffmpeg -f concat -i "{fn_in}" -c copy "{fn_out}"', shell=True)
    subprocess.call(f'ffmpeg -f concat -i "{fn_in}" -filter:v fps=1 "{fn_out}"', shell=True)
    subprocess.call(f'rm "{fn_in}"', shell=True)
# %%
