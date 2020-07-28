from PIL import Image 

import glob
import os

import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import pytesseract
from datetime import datetime
import sched, time

s = sched.scheduler(time.time, time.sleep)

def log_stats(sc):
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

	img = cv2.imread(latest_file,0)

	thresh,img_bin = cv2.threshold(img,128,255,cv2.THRESH_BINARY |cv2.THRESH_OTSU)

	img_bin = 255-img_bin
	cv2.imwrite(latest_file,img_bin)

	start_x, end_x = 0,1000
	start_y, end_y = 0,1000

	img = cv2.imread(latest_file)
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

	im = Image.open(latest_file)

	num_ppl_width = 60
	num_ppl_height = 25
	left = 855
	num_ppl_2_5 = im.crop((left, 45, 
		left+num_ppl_width, 45+num_ppl_height)) 
	num_ppl_5_10 = im.crop((left, 87, 
		left+num_ppl_width, 87+num_ppl_height)) 
	num_ppl_10_25 = im.crop((left, 125, 
		left+num_ppl_width, 125+num_ppl_height)) 
	num_ppl_25_50 = im.crop((left, 168, 
		left+num_ppl_width, 168+num_ppl_height)) 
	num_ppl_50_100 = im.crop((left, 206, 
		left+num_ppl_width, 206+num_ppl_height))
	num_ppl_100_200 = im.crop((left, 244, 
		left+num_ppl_width, 244+num_ppl_height)) 
	num_ppl_250_500 = im.crop((left, 288, 
		left+num_ppl_width, 288+num_ppl_height)) 

	num_ppl_imgs = [num_ppl_2_5, num_ppl_5_10, num_ppl_10_25, num_ppl_25_50, num_ppl_50_100, num_ppl_100_200, 
		num_ppl_250_500]

	avg_pot_width = 100
	avg_pot = []
	y_start = 45
	y_delta = 40
	left_avg_pot = 995
	for i in range(7):
		img = im.crop((left_avg_pot, y_start+i*y_delta, 
			left_avg_pot+avg_pot_width, y_start+i*y_delta+num_ppl_height))
		avg_pot.append(pytesseract.image_to_string(img, 
			config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789+.$'))

	plrs_flop_width = 75
	plrs_flop = []
	y_start = 45
	y_delta = 40
	left_plrs_flop = 1156
	for i in range(7):
		img = im.crop((left_plrs_flop, y_start+i*y_delta, 
			left_plrs_flop+avg_pot_width, y_start+i*y_delta+num_ppl_height))
		plrs_flop.append(pytesseract.image_to_string(img, 
			config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789%'))

	num_ppl = []
	for img in num_ppl_imgs:
		num_ppl.append(pytesseract.image_to_string(img, 
			config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789+'))

	print(num_ppl, avg_pot, plrs_flop)

	with open("log.txt", "a") as file_object:
	    # Append 'hello' at the end of file
	    file_object.write(str(datetime.now()))
	    file_object.write('\n')
	    file_object.write(",".join(num_ppl))
	    file_object.write('\n')
	    file_object.write(",".join(avg_pot))
	    file_object.write('\n')
	    file_object.write(",".join(plrs_flop))
	    file_object.write('\n')

	print("Finished logging at: ", datetime.now())
	s.enter(60, 1, log_stats, (sc,))


s.enter(60, 1, log_stats, (s,))
s.run()
