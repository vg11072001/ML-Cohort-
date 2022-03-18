import os
import cv2
import csv

csv_file = open("data_labels.csv")
csvreader = csv.reader(csv_file)
header = next(csvreader)
# print(header)
rows = []
for row in csvreader:
    rows.append(row)

path = 'cat' # Source Folder
dstpath = 'result' # Destination Folder

im = cv2.imread(os.path.join(path,rows[1][0]))
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    x = int(rows[1][4])
    y = int(rows[1][5])
    xm = int(rows[1][6])
    ym = int(rows[1][7])
cv2.rectangle(im,(x,y),(xm,ym),(0,0,0),2)
cv2.putText(im,'Cat',(x-10,y-10),0,0.6,(0,0,0))
cv2.imshow("Show",im)
cv2.waitKey()
cv2.destroyAllWindows()
