import numpy as np
import cv2
import matplotlib.pyplot as plt
# Black image
black = np.zeros((256, 256), dtype=np.uint8)
black_hist = cv2.calcHist([black],[0],None,[50],[0,256])
# Read images and convert to RGB
high = cv2.cvtColor(cv2.imread('hist_highkey.jpg'), cv2.COLOR_BGR2RGB)
low = cv2.cvtColor(cv2.imread('hist_lowkey.jpg'), cv2.COLOR_BGR2RGB)
# Create figure with 1 row, 3 columns
plt.figure(figsize=(18,6))
# Subplot 1: Black image histogram
plt.subplot(1,3,1)
plt.bar(range(50), black_hist.ravel())
plt.title('Black Image Histogram')
plt.xticks([])
plt.yticks([])
# Subplot 2: High Key image
plt.subplot(1,3,2)
plt.imshow(high)
plt.title('High Key')
plt.xticks([])
plt.yticks([])
# Subplot 3: Low Key image
plt.subplot(1,3,3)
plt.imshow(low)
plt.title('Low Key')
plt.xticks([])
plt.yticks([])
plt.show()
