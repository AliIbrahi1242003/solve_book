import cv2
import matplotlib.pyplot as plt

# Read grayscale image
lena = cv2.imread('lena_gray_256.tif', 0)

# Plot images
plt.figure(figsize=(20, 20))

# Original image
plt.subplot(1, 3, 1)
plt.imshow(lena, cmap='gray')
plt.title("Original Lena")
plt.axis("off")

# Using cv2.subtract
plt.subplot(1, 3, 2)
plt.imshow(cv2.subtract(lena, 128), cmap='gray')
plt.title("cv2.subtract(lena,128)")
plt.axis("off")

# Using direct subtraction (lena - 128)
plt.subplot(1, 3, 3)
plt.imshow(lena - 128, cmap='gray')
plt.title("lena - 128")
plt.axis("off")

plt.show()
