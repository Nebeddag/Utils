import os
import cv2

import uuid

import xml.etree.ElementTree as ET

s_path = '/mnt/HardDisk_01/Datasets/cleaning_data/detection_lbl/upd20201013'
out_img_path = '/mnt/HardDisk_01/Datasets/cleaning_data/detection_lbl/output'

img_ext = '.jpg'
desc_ext = '.xml'

extend_perc = 10

fnames = []

out_names = {}

# for f in os.listdir(s_path):
#     if f.endswith(desc_ext):
#         fnames.append(os.path.join(s_path, f))

for (dirpath, dirnames, filenames) in os.walk(s_path):
    for f in filenames:
        if f.endswith(desc_ext):
            fnames.append((dirpath, f))

for dirpath, filename in fnames:
    fn = os.path.join(dirpath, filename)
    root = ET.parse(fn).getroot()
    objects = []

    for type_tag in root.findall('object'):
        obj = {}
        for ch in type_tag:
            if ch.tag == 'name':
                obj['name'] = ch.text.strip().lower()
            elif ch.tag == 'bndbox':
                for el in ch:
                    obj[el.tag] = int(el.text)
        
        objects.append((fn, obj))

    img = cv2.imread(fn.replace(desc_ext, img_ext))
    
    for fn, obj in objects:
        try:
            width = img.shape[1]
            height = img.shape[0]

            ol_x = int((obj['xmax'] - obj['xmin']) * extend_perc/100)
            ol_y = int((obj['ymax'] - obj['ymin']) * extend_perc/100)

            xmin = max(0, obj['xmin'] - ol_x)
            xmax = min(width, obj['xmax'] + ol_x)
            ymin = max(0, obj['ymin'] - ol_y)
            ymax = min(height, obj['ymax'] + ol_y)

            obj_img = img[ymin:ymax, xmin:xmax]

            dn = os.path.join(out_img_path, obj['name'])
            if not os.path.exists(dn):
                os.makedirs(dn)
            
            newname = filename[0: filename.rfind('.')]
            out_names[newname] = out_names.get(newname, -1) + 1
            newname = newname + '_' + str(out_names[newname])
            cv2.imwrite(os.path.join(dn, newname + img_ext), obj_img)
        except:
            print(f'error in {filename}')

print('done')