import cv2
import matplotlib.pyplot as plt

img = cv2.imread('lena_gray_256.tif')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

gblur = cv2.GaussianBlur(img, (5, 5), 0)

fig = plt.figure(figsize=(20, 20))
plt.subplot(1,3,1), plt.imshow(img)
plt.subplot(1,3,2), plt.imshow(gblur, cmap='gray')
plt.show()
