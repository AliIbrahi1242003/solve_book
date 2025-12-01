import cv2
import matplotlib.pyplot as plt

# Read the two images in grayscale
img1_sub = cv2.imread('img1_sub.png', 0)
img2_sub = cv2.imread('img2_sub.png', 0)

# Perform image subtraction
changes = cv2.subtract(img1_sub, img2_sub)

# Plot the images
plt.figure(figsize=(20, 20))

plt.subplot(1, 3, 1)
plt.imshow(img1_sub, cmap='gray')
plt.title("Image 1")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(img2_sub, cmap='gray')
plt.title("Image 2")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(changes, cmap='gray')
plt.title("Subtraction Result")
plt.axis("off")

plt.show()
