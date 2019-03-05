import cv2
import numpy as np

hdr = cv2.imread("/home/vision/zeeshan/hdrcnn/out/000012_out.exr", -1).astype(np.float32)