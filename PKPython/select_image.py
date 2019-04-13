#!/usr/bin/python
import cv2
import os 
import sys


img_dir_r = sys.argv[1]
img_dir_w = sys.argv[2]
list_img_name_full_r = []
list_img_name_full_w = []
print("Select image... by key a, pass by key p")
for img_name in os.listdir(img_dir_r):
    list_img_name_full_r.append(os.path.join(img_dir_r, img_name))
    list_img_name_full_w.append(os.path.join(img_dir_w, img_name))
count = 0    
interval = 9
total = len(list_img_name_full_r)
for i in range(total):
    img_name_full=list_img_name_full_r[count]
    img = cv2.imread(img_name_full)
    cv2.imshow("Select by press key c, pass by key p, or jump by j", img)
    key = cv2.waitKey(50)
    if (key == 'c'):
        print("Selected"+img_name_full) 
        img_name_full_w=list_img_name_full_w[count]
        cv2.imwrite(img_name_full_w,img)
        count=count+1
        if (count == total):
            break
    elif (key == 'p'):
        continue
    elif (key == 'j' ):
        count = count+interval
        if (count >= total):
            break