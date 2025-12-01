import cv2
import matplotlib.pyplot as plt
img=cv2.imread('dull.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
blur= cv2.GaussianBlur(img, (25,25), 0)
mask=cv2.subtract(img,blur)
# fig=plt.figure(figsize=(10, 10))
plt.subplot(1,5,1), plt.imshow(img), plt.xticks([]),plt.yticks([])
plt.subplot(1,5,2), plt.imshow(blur,cmap = 'gray'), plt.xticks([]),plt.yticks([])
plt.subplot(1,5,3), plt.imshow(mask,cmap = 'gray'), plt.xticks([]),plt.yticks([])
plt.subplot(1,5,4), plt.imshow(cv2.add(img,mask),cmap = 'gray'),
plt.xticks([]),plt.yticks([])
plt.subplot(1,5,5), plt.imshow(cv2.add(img,5*mask),cmap = 'gray'),
plt.xticks([]),plt.yticks([])
plt.show()