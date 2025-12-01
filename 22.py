import cv2
import matplotlib.pyplot as plt

img=cv2.imread('equl.png') 
gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
img_eq = cv2.equalizeHist(gray_img) 
grid = plt.GridSpec(3, 4, wspace=0.4, hspace=0.3) 
plt.subplot(grid[:2, :2]) 
plt.imshow(img, cmap='gray') 
plt.grid(False), plt.xticks([]), plt.yticks([]) 
plt.subplot(grid[:2, 2:]) 
plt.imshow(img_eq, cmap='gray') 
plt.grid(False), plt.xticks([]), plt.yticks([]) 
plt.subplot(grid[2, :2]) 
plt.bar(range(256), 
 cv2.calcHist([img],[0],None,[256],[0,256]).ravel()) 
plt.subplot(grid[2, 2:]) 
plt.bar(range(256), 
 cv2.calcHist([img_eq],[0],None,[256],[0,256]).ravel()) 

plt.show()
