import cv2

import os,glob

from os import listdir,makedirs

from os.path import isfile,join
path = 'Data' # Source Folder
dstpath = 'result' # Destination Folder
try:
    makedirs(dstpath)
except:
    print ("Directory already exist, images will be written in same folder")
# Folder won't used
files = list(filter(lambda f: isfile(join(path,f)), listdir(path)))
imgformate = []
imgno = 0
images=[]
gray_images=[]
for image in files:
    try:
        img = cv2.imread(os.path.join(path,image))
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        images.append(img)
        gray_images.append(gray)
        dstPath = join(dstpath,image)
        imgno = imgno + 1
        cv2.imwrite(dstPath,gray)
    except:
        print ("{} is not converted".format(image))
print('Format type of image:',type(images.pop()))
print('Number of images:',len(gray_images))
