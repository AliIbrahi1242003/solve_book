import cv2
import matplotlib.pyplot as plt

# Read the two images in grayscale
img1 = cv2.imread('img1_dev.png', 0)
img2 = cv2.imread('img2_dev.png', 0)

# Perform image division
division_result = img1 / img2   # or cv2.divide(img1, img2)

# Plot images
plt.figure(figsize=(10, 10))

plt.subplot(1, 3, 1)
plt.imshow(img1, cmap='gray')
plt.title("Image 1")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(img2, cmap='gray')
plt.title("Image 2")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(division_result, cmap='gray')
plt.title("img1 / img2")
plt.axis('off')

plt.show()
