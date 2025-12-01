import cv2
import matplotlib.pyplot as plt
img2=cv2.imread('noise.png')
gray_img2=cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
img_eq = cv2.equalizeHist(gray_img2)
grid = plt.GridSpec(3, 4, wspace=0.4, hspace=0.3)
plt.subplot(grid[:2, :2])
plt.imshow(img2, cmap='gray')
plt.grid(False), plt.xticks([]), plt.yticks([])
plt.subplot(grid[:2, 2:])
plt.imshow(img_eq, cmap='gray')
plt.grid(False), plt.xticks([]), plt.yticks([])
plt.subplot(grid[2, :2])
plt.bar(range(256),
cv2.calcHist([gray_img2],[0],None,[256],[0,256]).ravel())
plt.subplot(grid[2, 2:])
plt.bar(range(256),
cv2.calcHist([img_eq],[0],None,[256],[0,256]).ravel())
plt.show()