import cv2
import numpy as np
import matplotlib.pyplot as plt
# 1. Read the X-ray dental image in grayscale
xray = cv2.imread('dental_xray.jpg', 0)
# 2. Create a black mask with the same size as the image
mask_xray = np.zeros(xray.shape, dtype="uint8")
# 3. Draw a white rectangle (value = 1) on the mask
mask_xray = cv2.rectangle(mask_xray, (400, 200), (650, 700), 1, -1)
# 4. Multiply the image with the mask
masked_xray = cv2.multiply(xray, mask_xray)
# 5. Show original image, mask, and result
plt.figure(figsize=(10, 10))
plt.subplot(1, 3, 1)
plt.imshow(xray, cmap='gray')
plt.title('Original X-ray')
plt.axis('off')
plt.subplot(1, 3, 2)
plt.imshow(mask_xray, cmap='gray')
plt.title('Mask')
plt.axis('off')
plt.subplot(1, 3, 3)
plt.imshow(masked_xray, cmap='gray')
plt.title('Masked X-ray')
plt.axis('off')
plt.show()
