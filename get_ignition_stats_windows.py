def get_stats():

	# Importing cannot be done at the module level or else it breaks.
	# This is because certain libraries are not thread safe. 
	# https://github.com/celery/celery/issues/2964	

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

	def add_margin(pil_img, top, right, bottom, left, color):
	    width, height = pil_img.size
	    new_width = width + right + left
	    new_height = height + top + bottom
	    result = Image.new(pil_img.mode, (new_width, new_height), color)
	    result.paste(pil_img, (left, top))
	    return result

	list_of_files = glob.glob('/home/pi/screenshots/') 
	latest_file = max(list_of_files, key=os.path.getctime)

	# latest_file = '/Users/raymondfeng/Desktop/TrickyWays/cropped/chubert.jpeg'

	# Opens a image in RGB mode 
	im = Image.open(latest_file) 
	  
	left = 292
	top = 341 - 4
	right = 908
	bottom = 443 - 4	

	im1 = im.crop((left, top, right, bottom)) 

	# im1.save('/Users/raymondfeng/Desktop/TrickyWays/cropped/chubert_cropped.jpeg')  
	# img = cv2.imread('/Users/raymondfeng/Desktop/TrickyWays/cropped/chubert_cropped.jpeg',0)
	# im = Image.open('/Users/raymondfeng/Desktop/TrickyWays/cropped/chubert_cropped.jpeg')
	im1.save('/home/pi/cropped.jpeg')
	im = Image.open('/home/pi/cropped.jpeg')

	num_ppl = []
	num_ppl_width = 45
	left = 419
	num_rows = 5
	y_delta = im.size[1] / num_rows
	for i in range(num_rows):
		img = im.crop((left, i*y_delta,
			left+num_ppl_width, (i+1)*y_delta))
		# img = add_margin(img, 5, 0, 5, 0, (255,255,255)) # Supposedly helps the OCR
		path_name = os.path.join('/home/pi/pre_ocr', 
			str(datetime.now())[10:19].replace(':','_') + '_' + str(i) + '_' + 'num_ppl.png')
		img = img.resize((round(img.size[0]*10), round(img.size[1]*10)), Image.ANTIALIAS)
		img.save(path_name)
		img = cv2.imread(path_name, 0)
		thresh, img = cv2.threshold(img,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
		img = 255 - img
		cv2.imwrite(path_name, img)
		img = Image.open(path_name)
		num_ppl.append(pytesseract.image_to_string(img, 
			config='--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789+'))

	avg_pot = []
	avg_pot_width = 60
	left = 483
	num_rows = 5
	y_delta = im.size[1] / num_rows
	for i in range(num_rows):
		img = im.crop((left, i*y_delta,
			left+avg_pot_width, (i+1)*y_delta))
		img = add_margin(img, 5, 0, 5, 0, (255,255,255)) # Supposedly helps the OCR
		path_name = os.path.join('/home/pi/pre_ocr', 
			str(datetime.now())[10:19].replace(':','_') + '_' + str(i) + '_' + 'avg_pot.png')
		img = img.resize((round(img.size[0]*10), round(img.size[1]*10)), Image.ANTIALIAS)
		img.save(path_name)
		img = cv2.imread(path_name, 0)
		thresh, img = cv2.threshold(img,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
		img = 255 - img
		cv2.imwrite(path_name, img)
		img = Image.open(path_name)
		avg_pot.append(pytesseract.image_to_string(img, 
			config='--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789+.$'))

	plrs_flop = []
	plrs_flop_width = 48
	left = 573
	num_rows = 5
	y_delta = im.size[1] / num_rows
	for i in range(num_rows):
		img = im.crop((left, i*y_delta,
			left+plrs_flop_width, (i+1)*y_delta))
		img = add_margin(img, 5, 0, 5, 0, (0,0,0)) # Supposedly helps the OCR
		path_name = os.path.join('/home/pi/pre_ocr', 
			str(datetime.now())[10:19].replace(':','_') + '_' + str(i) + '_' + 'plrs_flop.png')
		img = img.resize((round(img.size[0]*12), round(img.size[1]*12)), Image.ANTIALIAS)
		img.save(path_name)
		img = cv2.imread(path_name, 0)
		# img = cv2.filter2D(img, -1, np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]]))
		# img = cv2.GaussianBlur(img, (3,3), 0)
		img = cv2.erode(img, np.ones((5,5), np.uint8), iterations=2)
		thresh, img = cv2.threshold(img,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
		img = 255 - img
		cv2.imwrite(path_name, img)
		img = Image.open(path_name)
		plrs_flop.append(pytesseract.image_to_string(img, 
			config='--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789%'))

	print(num_ppl, avg_pot, plrs_flop)
	return num_ppl, avg_pot, plrs_flop

