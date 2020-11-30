import os

kitti_label_path = "/media/cundo/HardDisk_01/Datasets/TrespassDetection/train/labels/"

kitti_labels = os.listdir(kitti_label_path)

labels = set()

for fn in kitti_labels:
    kitti_fullpath = kitti_label_path + fn

    kitti_label = open(kitti_fullpath, 'r')
    
    label_contents = kitti_label.readlines()

    for line in label_contents:
        lbl = line.split()[0]
        labels.add(lbl)
    
print(labels)