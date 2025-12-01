import cv2
import matplotlib.pyplot as plt
from skimage import exposure
def load_image(number):
    img = cv2.imread(f"img{number}_sub.png")  
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray
src = load_image(1)
dst = load_image(2)
matched_src = exposure.match_histograms(src, dst)
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.imshow(src, cmap='gray')
plt.title("Source Image")
plt.axis("off")
plt.subplot(1, 3, 2)
plt.imshow(dst, cmap='gray')
plt.title("Reference Image")
plt.axis("off")
plt.subplot(1, 3, 3)
plt.imshow(matched_src, cmap='gray')
plt.title("Matched Image")
plt.axis("off")
plt.show()
