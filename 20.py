import cv2
import numpy as np
import matplotlib.pyplot as plt
# Read the image in greyscale 
img = cv2.imread('testt.png',0) 
#Iterate over each pixel and change pixel value to binary using np.binary_repr() and  store it in a list
lst = [] 
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        lst.append(np.binary_repr(int(img[i][j]), width=8))  # width = no. of bits
# We have a list of strings where each string represents binary pixel value. To extract 
# bit planes we need to iterate over the strings and store the characters corresponding 
# to bit planes into lists. 
# Multiply with 2^(n-1) and reshape to reconstruct the bit image. 
plane = []
for i in range(7, -1, -1):
    plane.append(
        (np.array([int(pxl[i]) * (2**(7 - i)) for pxl in lst], dtype=np.uint8))
        .reshape(img.shape[0], img.shape[1])
    )
# set up side-by-side image display 
fig = plt.figure() 
fig.set_figheight(5) 
fig.set_figwidth(5) 
# Higher order bits usually 
# contain most of the significant visual information Lower order bits contain 
# subtle details 
for i in range(1,9): 
 plt.subplot(4,2,i) 
 plt.imshow(plane[i-1], cmap='gray')
 plt.axis('off')
plt.show()
