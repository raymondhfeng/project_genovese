from PIL import Image 

import glob
import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage import color
from skimage import io

list_of_files = glob.glob('/Users/raymondfeng/Desktop/TrickyWays/*') 
latest_file = max(list_of_files, key=os.path.getctime)

# Opens a image in RGB mode 
im = Image.open(latest_file) 
  
# left = 570
# top = 685
# right = 1860
# bottom = 1000	

num_ppl_width = 60
num_ppl_height = 30
num_ppl_2_5 = im.crop((1419, 733, 
	1419+num_ppl_width, 733+num_ppl_height)) 

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

img = color.rgb2gray(np.array(num_ppl_2_5))
# img = rgb2gray(np.array(num_ppl_2_5))
print(img.shape)

thresh,img_bin = cv2.threshold(img,128,255,cv2.THRESH_BINARY |cv2.THRESH_OTSU)
img_bin = 255-img_bin
plotting = plt.imshow(img_bin,cmap='gray')
plt.show()

import pytesseract

print(pytesseract.image_to_string(num_ppl_2_5))

# num_ppl_2_5.show()
# im1.save(latest_file)

# im = cv2.imread(latest_file)
# plotting = plt.imshow(im,cmap='gray')
# plt.show()
