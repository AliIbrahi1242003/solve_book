import cv2
import matplotlib.pyplot as plt

# Read images
tom = cv2.imread("tt.png")
tom = cv2.cvtColor(tom, cv2.COLOR_BGR2RGB)

jerry = cv2.imread("jj.png")
jerry = cv2.cvtColor(jerry, cv2.COLOR_BGR2RGB)

# Addition of the two images
ADD = cv2.add(tom, jerry)

# Plot the images
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(tom)
plt.title("Tom")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(jerry)
plt.title("Jerry")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(ADD)
plt.title("Tom + Jerry")
plt.axis("off")

plt.show()
