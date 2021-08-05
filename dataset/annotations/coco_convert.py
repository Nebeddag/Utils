# Приводит файл с аннотациями coco в канонический вид
import os
import re

ds_type = 'val' # 'train'
ds_path = '/home/cundo/Work/TestProjects/TransPose/data/coco'

filename = f'/home/cundo/Work/TestProjects/TransPose/data/coco/annotations/person_keypoints_{ds_type}2017.json'

#old_rel_path = '/datasets/tm'
new_rel_path = f'images/{ds_type}2017'


new_content = []
idx_dic = {}

with open(filename, 'r') as f:
    content = f.readlines()
    idx = 0
    imgs = False

    for line in content:
        if '"images": ' in line:
            imgs = True

        elif '"categories":' in line:
            imgs = False
        
        elif '"annotations": ' in line:
            imgs = False

        if imgs and '"id": ' in line:
            idx_old = re.sub('\D', '', line)
            new_content.append(line.replace(idx_old, str(idx)))
            idx_dic[idx_old] = str(idx)

        elif imgs and '"path": ' in line:
            imname_relative = line.split('"')[-2]
            
            #imname_full = '/home/cundo/Work/TestProjects/TransPose/data/coco' + imname_relative
            imname = imname_relative.split('/')[-1]
            imname_new = '%012d.jpg' % idx
            imname_full = os.path.join(ds_path, new_rel_path, imname)
            #imname_full_new = imname_full.replace(imname, imname_new)
            imname_full_new = os.path.join(ds_path, new_rel_path, imname_new) 
            os.rename(imname_full, imname_full_new)
            #line = line.replace(imname, imname_new)
            new_content.append(line.replace(imname, imname_new))
            idx += 1

        elif imgs and '"file_name": ' in line:
            new_content.append(line.replace(imname, imname_new))

        elif '"image_id": ' in line:
            idx_old = re.sub('\D', '', line)
            new_content.append(line.replace(idx_old, idx_dic[idx_old]))
            print(idx_old, idx_dic[idx_old])
            pass

        else:
            new_content.append(line)
    f.close()

with open(filename + '1', 'w') as f:
    f.writelines(new_content)
    f.close()