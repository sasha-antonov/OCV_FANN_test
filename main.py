# coding=utf-8
__author__ = 'sasha'

import cv
from create_data import *

img = cv.LoadImage("/home/sasha/Project_X/test_OpenCV/PyTest/frame.jpg")

gray = cv.CreateImage((img.width, img.height), cv.IPL_DEPTH_8U, 1)
binary = cv.CreateImage(cv.GetSize(img), cv.IPL_DEPTH_8U, 1)
msk = cv.CreateImage((img.width + 2, img.height + 2), cv.IPL_DEPTH_8U, 1)
dst = cv.CreateImage((img.width, img.height), cv.IPL_DEPTH_8U, 1)

#cv.NamedWindow("gray", cv.CV_WINDOW_AUTOSIZE)
#cv.NamedWindow("bin", cv.CV_WINDOW_AUTOSIZE)

cv.NamedWindow("test1", cv.CV_WINDOW_AUTOSIZE)
cv.NamedWindow("test2", cv.CV_WINDOW_AUTOSIZE)
#cv.NamedWindow("test3", cv.CV_WINDOW_AUTOSIZE)
#cv.NamedWindow("test4", cv.CV_WINDOW_AUTOSIZE)
#cv.NamedWindow("test5", cv.CV_WINDOW_AUTOSIZE)

cv.CvtColor(img, gray, cv.CV_RGB2GRAY)
cv.Not(gray, gray)
cv.Threshold(gray, binary, 20, 255, cv.CV_THRESH_BINARY)

color = 100
color_list = []
for x in range(binary.width):
     for y in range(binary.height):
          if(binary[y,x] > color):
               cv.FloodFill(binary, (x,y), color, cv.ScalarAll(10), cv.ScalarAll(10), 0, msk)
               color_list.append(color)
               color = color + 1

obj = []
l_x = 0
r_x = 0
d_y = 0
u_y = 0
color = 0
for col in range(len(color_list)):
     for x in range(binary.width):
          for y in range(binary.height):
               if(binary[y,x] == color_list[col] and
               binary[y,x] != color):
                    obj.append([x,x,y,y])
                    color = color_list[col]

for n in range(len(color_list)):
     for x in range(binary.width):
          for y in range(binary.height):
               if(binary[y,x] == color_list[n]):
                    if(obj[n][0] > x):
                         obj[n][0] = x
                    if(obj[n][1] < x):
                         obj[n][1] = x
                    if(obj[n][2] > y):
                         obj[n][2] = y
                    if(obj[n][3] < y):
                         obj[n][3] = y

for l in range(len(obj)):
     print(obj[l], color_list[l])

num = []
for k in range(len(obj)):
    l_x = obj[k][0]
    r_x = obj[k][1]
    d_y = obj[k][2]
    u_y = obj[k][3]
    if((u_y - d_y) > 200 and
    (r_x - l_x) > 100):
        num.append(k)

list_img = []
print[num]
print(l_x, r_x, d_y, u_y)

for k in range(len(num)):
    l_x = obj[num[k]][0]
    r_x = obj[num[k]][1]
    d_y = obj[num[k]][2]
    u_y = obj[num[k]][3]
    list_img.append(binary[d_y : u_y, l_x : r_x])

crop_num_6 = binary[185:450, 90:250]
crop_num_7 = binary[185:450, 370:530]

mat = cv.GetMat(list_img[0], 0)
cv.Save('matrix.xml',mat)

in_data = []
for y in range(list_img[0].height):
    for x in range(list_img[0].width):
        if(list_img[0][y,x] != 0):
            in_data.append(1)
        else:
            in_data.append(-1)

create_data(in_data, 6)

#cv.ShowImage("gray", gray)
#cv.ShowImage("bin", binary)

cv.ShowImage("test1", list_img[0])
cv.ShowImage("test2", list_img[1])
#cv.ShowImage("test3", list_img[2])
#cv.ShowImage("test4", list_img[3])
#cv.ShowImage("test5", list_img[4])

cv.WaitKey(0)