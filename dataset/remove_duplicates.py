import os

def get_files_by_file_size(dirname, reverse=False):

    filepaths = []
    for basename in os.listdir(dirname):
        filename = os.path.join(dirname, basename)
        if os.path.isfile(filename):
            filepaths.append(filename)

    for i in range(len(filepaths)):
        filepaths[i] = (filepaths[i], os.path.getsize(filepaths[i]))

    filepaths.sort(key=lambda filename: filename[1], reverse=reverse)

    return filepaths

dirpath = "/media/cundo/HardDisk_01/Datasets/cleaning_data/all/cleaner"
files = get_files_by_file_size(dirpath)
sizes = {}
for key, val in files:
    sizes[val] = sizes.get(val, [])
    sizes[val].append(key)

#Пока всё, не понадобилось
print('')
