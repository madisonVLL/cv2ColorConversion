import cv2
import urllib.request
import numpy as np
# Convert the image array to an OpenCV image
image = cv2.imread("panda.jpg")
 
# If you want to use a local image instead of downloading from a URL,
# simply replace the above lines with:
# image = cv2.imread('path/to/your/local_image.jpg')
 
# Convert the image from RGB to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
 
# Display the original and HSV images
cv2.imshow('Original Image', image)
cv2.imshow('HSV Image', hsv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()