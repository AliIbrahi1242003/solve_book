import cv2
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread('faterscaling1-300x241.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
kernel = np.ones((5, 5), np.float32)
kernel=kernel/25
dst = cv2.filter2D(img,-1, kernel)
blur = cv2.blur(img, (5, 5))
fig=plt.figure(figsize=(20, 20))
plt.subplot(1,3,1), plt.imshow(img)
plt.subplot(1,3,2), plt.imshow(dst)
plt.subplot(1,3,3), plt.imshow(blur)
plt.show()