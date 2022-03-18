import os
import cv2
import csv
from os import listdir,makedirs

path = 'cat' # Source Folder
dstpath = 'result' # Destination Folder
try:
    makedirs(dstpath)
except:
    print ("Directory already exist, images will be written in same folder")

#csv file loaded
csv_file = open("data_labels.csv")
csvreader = csv.reader(csv_file)
header = next(csvreader)
# print(header)
rows = []
for row in csvreader:
    rows.append(row)

fonts=[ cv2.FONT_HERSHEY_SIMPLEX, cv2.FONT_HERSHEY_PLAIN, cv2.FONT_HERSHEY_DUPLEX, cv2.FONT_HERSHEY_COMPLEX, cv2.FONT_HERSHEY_TRIPLEX, cv2.FONT_HERSHEY_COMPLEX_SMALL, cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, cv2.FONT_HERSHEY_SCRIPT_COMPLEX]

finalcat_images = []
for i in range(10):
    # try:
        im = cv2.imread(os.path.join(path,rows[i+1][0]))
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            x,y,w,h = cv2.boundingRect(c)
            x = int(rows[i+1][4])
            y = int(rows[i+1][5])
            xm = int(rows[i+1][6])
            ym = int(rows[i+1][7])
            cv2.rectangle(im,(x,y),(xm,ym),(i*i,i,25*i),2*i)
            cv2.putText(im,rows[i+1][1],(100,100),fonts[i%8], i+1,(255,i*i,25*i))
        finalcat_images.append(im)
        cv2.imwrite("result/"+rows[i+1][0]+".jpg",im)

#     except:
#         print ("{} is not converted".format(rows[i+1][0]))
#
# csv_file.close()
