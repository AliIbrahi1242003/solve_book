import cv2
import matplotlib.pyplot as plt
# Read the original image
img = cv2.imread('lena_gray_256.tif')
# converting because opencv uses BGR as default
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(RGB_img)
# converting to gray scale
gray = cv2.cvtColor(RGB_img, cv2.COLOR_BGR2GRAY)
# remove noise
img = cv2.GaussianBlur(gray,(3,3),0)
# convolute with sobel kernels
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5) # x
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5) # y
fig=plt.figure(figsize=(10, 10))
plt.subplot(1,3,1), plt.imshow(RGB_img), plt.xticks([]),plt.yticks([])
plt.subplot(1,3,2), plt.imshow(sobelx,cmap = 'gray'), plt.xticks([]),plt.yticks([])
plt.subplot(1,3,3), plt.imshow(sobely,cmap = 'gray'), plt.xticks([]),plt.yticks([])
plt.show()