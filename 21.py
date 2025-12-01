import numpy as np 
import cv2 
# from google.colab.patches import cv2_imshow 
import matplotlib.pyplot as plt 
black = np.zeros((256, 256), dtype=np.uint8)

hist = cv2.calcHist([black],[0],None,[50],[0,256]) 
# different methods for displaying a histogram 
plt.bar(range(50), hist.ravel()) 
plt.title('Histogram of the black image') 
plt.xlabel('Gray values') 
plt.ylabel('Frequency') 

# Another method 
hist,bins = np.histogram(black.ravel(),256,[0,256]) 
plt.plot(hist) 

# Let's read two other images 
high = cv2.imread('hist_highkey.jpg') 
low = cv2.imread('hist_lowkey.jpg') 

# show images 
plt.subplot(121), plt.imshow(high) 
plt.grid(False), plt.xticks([]), plt.yticks([]) 


plt.subplot(122), plt.imshow(low) 
plt.grid(False), plt.xticks([]), plt.yticks([]) 
plt.show() 

# Calculate histogram of both images for the last channel. 
# Channels can differ from 0 to 2. 
hist_high = cv2.calcHist([high],[2],None,[256],[0,256]) 
hist_low = cv2.calcHist([low],[2],None,[256],[0,256]) 

# Plot histograms 
plt.subplot(121) 
plt.plot(hist_high) 
plt.subplot(122) 
plt.plot(hist_low) 
plt.show()
