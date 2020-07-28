from PIL import Image 

import glob
import os

list_of_files = glob.glob('/Users/raymondfeng/Desktop/TrickyWays/*') 
latest_file = max(list_of_files, key=os.path.getctime)

# Opens a image in RGB mode 
im = Image.open(latest_file) 
  
left = 570
top = 685
right = 1860
bottom = 1000	
 
im1 = im.crop((left, top, right, bottom)) 
im1.save(latest_file)

import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import pytesseract

img = cv2.imread(latest_file,0)
print("Hoopla: ", img.shape)

thresh,img_bin = cv2.threshold(img,128,255,cv2.THRESH_BINARY |cv2.THRESH_OTSU)

img_bin = 255-img_bin
cv2.imwrite(latest_file,img_bin)

start_x, end_x = 0,1000
start_y, end_y = 0,1000

img = cv2.imread(latest_file)
print(img.shape)
for i in range(9):
	start_x, end_x = 0, img.shape[1]
	start_y, end_y = int((i) * (img.shape[0] / 8)) ,int((i) * (img.shape[0] / 8)) 
	cv2.line(img, (start_x, start_y), (end_x, end_y), (0, 0, 0), 3, 1)

cv2.line(img, (0, 0), (0, img.shape[0]), (0, 0, 0), 3, 1)
cv2.line(img, (200, 0), (200, img.shape[0]), (0, 0, 0), 3, 1)
cv2.line(img, (324, 0), (324, img.shape[0]), (0, 0, 0), 3, 1)
cv2.line(img, (520, 0), (520, img.shape[0]), (0, 0, 0), 3, 1)
cv2.line(img, (660, 0), (660, img.shape[0]), (0, 0, 0), 3, 1)
cv2.line(img, (800, 0), (800, img.shape[0]), (0, 0, 0), 3, 1)
cv2.line(img, (930, 0), (930, img.shape[0]), (0, 0, 0), 3, 1)
cv2.line(img, (1100, 0), (1100, img.shape[0]), (0, 0, 0), 3, 1)
cv2.line(img, (img.shape[1], 0), (img.shape[1], img.shape[0]), (0, 0, 0), 3, 1)

cv2.imwrite(latest_file,img)

# # Length(width) of kernel as 100th of total width
# kernel_len = np.array(img).shape[1]//100
# # Defining a vertical kernel to detect all vertical lines of image 
# ver_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_len))
# # Defining a horizontal kernel to detect all horizontal lines of image
# hor_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_len, 1))
# # A kernel of 2x2
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))

# #Use vertical kernel to detect and save the vertical lines in a jpg
# image_1 = cv2.erode(img, ver_kernel, iterations=3)
# vertical_lines = cv2.dilate(image_1, ver_kernel, iterations=3)
# cv2.imwrite("/Users/YOURPATH/vertical.jpg",vertical_lines)
#Plot the generated image
im = cv2.imread(latest_file)
plotting = plt.imshow(im,cmap='gray')
plt.show()

#Use horizontal kernel to detect and save the horizontal lines in a jpg
# image_2 = cv2.erode(img, hor_kernel, iterations=3)
# horizontal_lines = cv2.dilate(image_2, hor_kernel, iterations=3)
# cv2.imwrite("/Users/YOURPATH/horizontal.jpg",horizontal_lines)
# #Plot the generated image
# plotting = plt.imshow(image_2,cmap='gray')
# plt.show()

# from fpdf import FPDF
# scaling = 8
# pdf = FPDF()
# pdf.add_page()
# pdf.image(latest_file,20,20,img.shape[1]//scaling,img.shape[0]//scaling)
# pdf.output("yourfile.pdf", "F")

# import tabula
# df = tabula.read_pdf("yourfile.pdf", pages='all')

# print(df)

# plotting = plt.imshow(img,cmap='gray')
# plt.show()