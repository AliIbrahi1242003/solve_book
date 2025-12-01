import cv2
import matplotlib.pyplot as plt
img=cv2.imread('noise.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
blur = cv2.blur(img, (5, 5))
median = cv2.medianBlur(img, 5)
fig=plt.figure(figsize=(10, 10))
plt.subplot(1,3,1), plt.imshow(img)
plt.subplot(1,3,2), plt.imshow(blur)
plt.subplot(1,3,3), plt.imshow(median)
plt.show()