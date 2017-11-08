import cv2
import os

for root, dirs, files in os.walk("./motion", topdown=False):
   for name in files:
      img = cv2.imread (os.path.join(root, name))
      cropped = img[ 330:640, 420:730]
      cv2.imwrite(os.path.join(root, name), cropped)






