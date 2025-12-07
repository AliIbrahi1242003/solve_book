import cv2
im = cv2.imread('lena.jpg')   # Replace with your image file
print(type(im))
print(im.shape)
print(type(im.shape))
h, w, c = im.shape
print('width:', w)
print('height:', h)
print('channel:', c)
################
import cv2
im_gray = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
print(im_gray.shape)
print(type(im_gray.shape))
h, w = im_gray.shape
print('width:', w)
print('height:', h)
####################
from PIL import Image
im = Image.open('lena.jpg')   # Replace with your image file
print(im.size)
print(type(im.size))
w, h = im.size
print('width:', w)
print('height:', h)
print('width:', im.width)
print('height:', im.height)
