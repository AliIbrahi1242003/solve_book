import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image in grayscale
image = cv2.imread('ali_test.jpeg', cv2.IMREAD_GRAYSCALE)

# Log Transformation
c = 45
log_transformed = c * (np.log1p(image))  # np.log1p for log(image + 1)
log_transformed = np.uint8(log_transformed)

# Inverse Log Transformation
inverse_log_transformed = c * (np.expm1(log_transformed / c))  # np.expm1 for exp(x) - 1
inverse_log_transformed = np.uint8(inverse_log_transformed)

# Display the original and transformed images side by side
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(log_transformed, cmap='gray')
plt.title("Log Transformed")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(inverse_log_transformed, cmap='gray')
plt.title("Inverse Log Transformed")
plt.axis('off')

plt.show()
