import os
import cv2
import numpy as np


list1 = []
list_imgs = os.listdir("/home/vision/zeeshan/hdrcnn/training_code/video_data")
list_imgs.sort()
# print (list_imgs)
# print(a)
# print (list_imgs)
# for img in list_imgs:
# 	a = img.split("_")[0]
# 	list1.append(int(a))

# print (list1)
# # list1.sort()
# # print (list1)

suffix = "exr"
z = 0
# i = 300
for i in list_imgs:
	if i.endswith(suffix):
		print(i)
		# x = "/home/vision/zeeshan/hdrcnn/out/"
		# j = x+i
		j = i
		i = "/home/vision/zeeshan/hdrcnn/training_code/video_data/"+i
		hdr = cv2.imread(i,-1).astype(np.float32)
		# Tonemap using Durand's method obtain 24-bit color image
		tonemapDurand = cv2.createTonemapDurand(1.5,4,1.0,1,1)
		ldrDurand = tonemapDurand.process(hdr)
		# ldrDurand = 3 * ldrDurand
		cv2.imwrite("/home/vision/zeeshan/hdrcnn/tonemapped_hdr_ground_th/"+j+".jpg", ldrDurand * 255)
		z+=1


