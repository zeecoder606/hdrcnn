import cv2
import os

image_folder = 'tonemapped_hdr'
video_name = 'video_25.avi'
images = []
for i in range(300):
    j=i+1
    images.append(str(j)+".jpg")


# images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 25, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()
