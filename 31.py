import cv2
import matplotlib.pyplot as plt
import numpy as np
# Read the original image
img = cv2.imread('lena_gray_256.tif')
blur1 = cv2.blur(img, (3, 3))
laplacian = cv2.Laplacian(blur1,cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))
img_new = img + laplacian
fig=plt.figure(figsize=(10, 10))
plt.subplot(1,3,1), plt.imshow(img), plt.xticks([]),plt.yticks([])
plt.subplot(1,3,2), plt.imshow(laplacian,cmap = 'gray'), plt.xticks([]),plt.yticks([])
plt.subplot(1,3,3), plt.imshow(img_new,cmap = 'gray'), plt.xticks([]),plt.yticks([])
plt.show()