# coding=utf-8
__author__ = 'sasha'

import cv

img = cv.LoadImage("/home/sasha/Project_X/test_OpenCV/PyTest/frame.jpg")

gray = cv.CreateImage((img.width, img.height), cv.IPL_DEPTH_8U, 1)
binary = cv.CreateImage(cv.GetSize(img), cv.IPL_DEPTH_8U, 1)
dst = cv.CreateImage((img.width + 2, img.height + 2), cv.IPL_DEPTH_8U, 1)

cv.NamedWindow("gray", cv.CV_WINDOW_AUTOSIZE)
cv.NamedWindow("bin", cv.CV_WINDOW_AUTOSIZE)
#cv.NamedWindow("test", cv.CV_WINDOW_AUTOSIZE)

cv.CvtColor(img, gray, cv.CV_RGB2GRAY)
cv.Not(gray, gray)
cv.Threshold(gray, binary, 20, 255, cv.CV_THRESH_BINARY)

cv.iplimage.height

color = 10
color_list = []
for x in range(binary.width):
     for y in range(binary.height):
          if(binary[y,x] > color):
               cv.FloodFill(binary, (x,y), color, cv.ScalarAll(10), cv.ScalarAll(10), 0, dst)
               color_list.append(color)
               color = color + 10

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

crop_num_6 = binary[185:450, 90:250]
crop_num_7 = binary[185:450, 370:530]

cv.ShowImage("gray", gray)
cv.ShowImage("bin", binary)
#cv.ShowImage("test", dst)

cv.WaitKey(0)

