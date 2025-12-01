
# Python program to read image using OpenCV
# importing OpenCV(cv2) module
import cv2
import numpy as np
# Save image in set directory
# Read RGB image
img = cv2.imread('black.png',1) # Replace with your image file
# 0 --> for gray scale images
# 1 --> for colored images
#Note that OpenCV loads color image files in BGR order, not RGB.
#image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#brighter=np.clip(img*1.5,0,255).astytpe(np.uint8)
# Output img with window name as 'image'
cv2.imshow('image', img)
# Maintain output window until
# user presses a key
cv2.waitKey(0)
# Destroying present windows on screen
cv2.destroyAllWindows()