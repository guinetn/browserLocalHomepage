# OpenCV
"""
OpenCV is also a kind of image processing library that makes it easy to interface with webcams, images, and videos

simplicity and code readability. Nowadays, it is mostly used in computer vision tasks such as face detection and recognition, object detection, and more.

pip install opencv-python

"""

import cv2
img = cv2.imread("images/test.jpg")
imgCropped = img[50:283,25:190]
shape = imgCropped.shape
print(shape[0])
imgCropped = cv2.resize(imgCropped,(shape[0]*12//10,shape[1]*2))
cv2.imshow("Image cropped",imgCropped)
cv2.imshow("Image",img)
cv2.waitKey(0)