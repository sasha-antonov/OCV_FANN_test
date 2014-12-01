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

"""" находим все белые связанные поля и
     заливаем разными цветами
"""""

cv.FloodFill(binary, (0,10), 100, cv.ScalarAll(10), cv.ScalarAll(10), 0, dst)

crop_num_6 = binary[185:450, 90:250]
crop_num_7 = binary[185:450, 370:530]

cv.ShowImage("gray", gray)
cv.ShowImage("bin", binary)
#cv.ShowImage("test", dst)

cv.WaitKey(0)

