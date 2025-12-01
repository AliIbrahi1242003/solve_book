import cv2
import matplotlib.pyplot as plt
import numpy as np
# Read the original image
img = cv2.imread('lena_gray_256.tif')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#using built in cv2 function
laplacian = cv2.Laplacian(img,cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))
img_new = img + laplacian
fig=plt.figure(figsize=(10, 10))
plt.subplot(1,3,1), plt.imshow(img), plt.xticks([]),plt.yticks([])
plt.subplot(1,3,2), plt.imshow(laplacian,cmap = 'gray'), plt.xticks([]),plt.yticks([])
plt.subplot(1,3,3), plt.imshow(img_new,cmap = 'gray'), plt.xticks([]),plt.yticks([])
plt.show()