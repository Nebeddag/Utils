import os
import cv2

import uuid

import xml.etree.ElementTree as ET

s_path = '/media/cundo/HardDisk_01/Data/Validation/Cleaning/LabledFrames/train'
out_img_path = '/media/cundo/HardDisk_01/Data/Validation/Cleaning/Classifier/train'

img_ext = '.jpg'
desc_ext = '.xml'

overlap_perc = 0

fnames = []

for f in os.listdir(s_path):
    if f.endswith(desc_ext):
        fnames.append(os.path.join(s_path, f))

for fn in fnames:
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
    
    for fn, obj in objects:
        img = cv2.imread(fn.replace(desc_ext, img_ext))

        width = img.shape[1]
        height = img.shape[0]

        ol_x = int((obj['xmax'] - obj['xmin']) * overlap_perc)
        ol_y = int((obj['ymax'] - obj['ymin']) * overlap_perc)

        xmin = max(0, obj['xmin'] - ol_x)
        xmax = min(width, obj['xmax'] + ol_x)
        ymin = max(0, obj['ymin'] - ol_y)
        ymax = min(height, obj['ymax'] + ol_y)

        obj_img = img[ymin:ymax, xmin:xmax]

        dn = os.path.join(out_img_path, obj['name'])
        if not os.path.exists(dn):
            os.makedirs(dn)
        
        cv2.imwrite(os.path.join(dn, uuid.uuid4().hex + '.jpg'), obj_img)

t = 0