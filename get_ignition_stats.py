# from PIL import Image 

# import glob
# import os

# import cv2
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import csv
# import pytesseract
# from datetime import datetime

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

	list_of_files = glob.glob('/Users/raymondfeng/Desktop/TrickyWays/screenshots/*') 
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

	cv2.threshold(img,128,255,cv2.THRESH_BINARY |cv2.THRESH_OTSU)

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

	# cv2.line(img, (0, 0), (0, img.shape[0]), (0, 0, 0), 3, 1)
	# cv2.line(img, (200, 0), (200, img.shape[0]), (0, 0, 0), 3, 1)
	# cv2.line(img, (324, 0), (324, img.shape[0]), (0, 0, 0), 3, 1)
	# cv2.line(img, (520, 0), (520, img.shape[0]), (0, 0, 0), 3, 1)
	# cv2.line(img, (660, 0), (660, img.shape[0]), (0, 0, 0), 3, 1)
	# cv2.line(img, (800, 0), (800, img.shape[0]), (0, 0, 0), 3, 1)
	# cv2.line(img, (930, 0), (930, img.shape[0]), (0, 0, 0), 3, 1)
	# cv2.line(img, (1100, 0), (1100, img.shape[0]), (0, 0, 0), 3, 1)
	# cv2.line(img, (img.shape[1], 0), (img.shape[1], img.shape[0]), (0, 0, 0), 3, 1)

	cv2.imwrite(latest_file,img)

	im = Image.open(latest_file)

	def add_margin(pil_img, top, right, bottom, left, color):
	    width, height = pil_img.size
	    new_width = width + right + left
	    new_height = height + top + bottom
	    result = Image.new(pil_img.mode, (new_width, new_height), color)
	    result.paste(pil_img, (left, top))
	    return result


	num_ppl = []
	num_ppl_width = 65
	num_ppl_height = 25
	left = 865
	# y_start = 45
	y_start = 6
	y_delta = 40.5
	for i in range(5):
		img = im.crop((left, y_start+i*y_delta - 2,
			left+num_ppl_width, y_start+i*y_delta+num_ppl_height))
		# img.show()
		img = add_margin(img, 5, 0, 5, 0, (255,255,255))
		# img = img.resize((round(img.size[0]*2), round(img.size[1]*2)))
		img.save(os.path.join('/Users/raymondfeng/Desktop/TrickyWays/cropped/ignition_cropped', 
			str(datetime.now())[10:19].replace(':','_') + '_' + str(i) + '_' + 'num_ppl.png'))
		num_ppl.append(pytesseract.image_to_string(img, 
			config='--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789+'))
		# num_ppl.append(pytesseract.image_to_string(img, 
		# 	config='-c tessedit_char_whitelist=0123456789+'))

	avg_pot_width = 100
	avg_pot = []
	y_start = 6
	y_delta = 40.2
	left_avg_pot = 1008
	for i in range(5):
		if i == 0 or i == 1:
			img = im.crop((left_avg_pot + 5, y_start+i*y_delta, 
				left_avg_pot+avg_pot_width - 5, y_start+i*y_delta+num_ppl_height))			
		else:
			img = im.crop((left_avg_pot, y_start+i*y_delta, 
				left_avg_pot+avg_pot_width, y_start+i*y_delta+num_ppl_height))
		img = add_margin(img, 5, 0, 5, 0, (255,255,255))
		# img = img.resize((round(img.size[0]*2), round(img.size[1]*2)))
		img.save(os.path.join('/Users/raymondfeng/Desktop/TrickyWays/cropped/ignition_cropped', 
			str(datetime.now())[10:19].replace(':','_') + '_' + str(i) + '_' + 'avg_pot.png'))
		avg_pot.append(pytesseract.image_to_string(img, 
			config='--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789+.$'))
		# avg_pot.append(pytesseract.image_to_string(img, 
		# 	config='-c tessedit_char_whitelist=0123456789+.$'))

	plrs_flop_width = 66
	plrs_flop = []
	y_start = 6
	y_delta = 40.2
	left_plrs_flop = 1180
	for i in range(5):
		img = im.crop((left_plrs_flop, y_start+i*y_delta, 
			left_plrs_flop+plrs_flop_width, y_start+i*y_delta+num_ppl_height))
		img = add_margin(img, 5, 0, 5, 0, (255,255,255))
		# img = img.resize((round(img.size[0]*2), round(img.size[1]*2)))
		img.save(os.path.join('/Users/raymondfeng/Desktop/TrickyWays/cropped/ignition_cropped', 
			str(datetime.now())[10:19].replace(':','_') + '_' + str(i) + '_' + 'pct_flop.png'))
		plrs_flop.append(pytesseract.image_to_string(img, 
			config='--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789%'))
		# plrs_flop.append(pytesseract.image_to_string(img, 
		# 	config='-c tessedit_char_whitelist=0123456789%'))


	print(num_ppl, avg_pot, plrs_flop)
	return num_ppl, avg_pot, plrs_flop

# get_stats()