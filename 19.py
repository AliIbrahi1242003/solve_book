import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('pout.jpg', 0)# Load the image 
# Find width and height of image 
row, column = img.shape
# Create an zeros array to store the sliced image 
img1 = np.zeros((row, column), dtype='uint8')
img2 = np.zeros((row, column), dtype='uint8')
# Specify the min and max range 
min_range = 51
max_range = 140
# Loop over the input image and if pixel value lies in desired range set it to 255   otherwise set it to 0
for i in range(row):
    for j in range(column):
        if img[i, j] > min_range and img[i, j] < max_range:
            img1[i, j] = 255
        else:
            img1[i, j] = 0
img = cv2.imread('pout.jpg', 0)# Load the image 
row, column = img.shape # Find width and height of image 
# Create an zeros array to store the sliced image 
img2 = np.zeros((row, column), dtype='uint8')
# Specify the min and max range 
min_range = 51
max_range = 140
for i in range(row):
    for j in range(column):
        if img[i, j] > min_range and img[i, j] < max_range:
            img2[i, j] = 255
        else:
            img2[i, j] = img[i, j]
fig = plt.figure(figsize=(20, 20))
plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray')
plt.subplot(1, 3, 2), plt.imshow(img1, cmap='gray')
plt.subplot(1, 3, 3), plt.imshow(img2, cmap='gray')
plt.show()
