# Python program to read
# image using matplotlib
# importing matplotlib modules
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
# Read Images
img = mpimg.imread('black.png') # Replace with your image file
# Output Images
plt.imshow(img)
# -------------------------------------------------
# Python program to read
# image using PIL module
# importing PIL
from PIL import Image
# Read image
img = Image.open('black.png')
# Output Images
img.show()
# prints format of image
print(img.format)
# prints mode of image
print(img.mode)