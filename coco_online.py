from pycocotools.coco import COCO
import requests
import io
from PIL import Image

# instantiate COCO specifying the annotations json path
coco = COCO('/home/cundo/Work/annotations/person_keypoints_val2017.json')

# Specify a list of category names of interest
# catIds = coco.getCatIds(catNms=['person'])
# Get the corresponding image ids and images using loadImgs
# imgIds = coco.getImgIds(catIds=catIds)

imgIds = coco.getImgIds()
images = coco.loadImgs(imgIds)
annIds = coco.getAnnIds()
anns = coco.loadAnns(annIds)

for im in images:
    img_data = requests.get(im['coco_url']).content
    curr_ann = [i for i in anns if i['image_id'] == im['id']]
    imageStream = io.BytesIO(img_data)
    imageFile = Image.open(imageStream)
    
    # with open('tmp.jpg', 'wb') as handler:
    #     handler.write(img_data)