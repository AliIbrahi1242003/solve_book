## Using PIL (Pillow)
from PIL import Image
# 1. Load the original image
img = Image.open("ali_test.jpeg")
img.show()   # Display original image
# 2. Define the crop rectangle (left, upper, right, lower)
# Example: crop 500x500 pixels from the center of a 1000x1000 image
box = (250, 250, 750, 750)
# 3. Crop the image
cropped_img = img.crop(box)
# 4. Save the cropped result
cropped_img.save("cropped_output.jpg")
cropped_img.show()    # Display cropped image
###################################################
## Using OpenCV
import cv2
# 1. Read the image
image = cv2.imread("ali_test.jpeg")
# 2. Define the crop area
# We want a 500x500 area from the center of a 1000x1000 image
start_x = 250
start_y = 250
end_x = 750
end_y = 750
# 3. Crop the image using array slicing
cropped_image = image[start_y:end_y, start_x:end_x]
# 4. Display the result
cv2.imshow("Cropped Image", cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 5. Save cropped image
cv2.imwrite("cropped_output_opencv.jpg", cropped_image)
