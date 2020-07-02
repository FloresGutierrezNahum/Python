import cv2

# read the image
image = cv2.imread('saltandpeppernoise.jpg', 1)

cv2.imshow('Original', image)

# apply the 3x3 median filter on the image
processed_image = cv2.medianBlur(image, 3)
# display image
cv2.imshow('Median Filter Processing', processed_image)
# save image to disk
cv2.imwrite('processed_image.png', processed_image)
# pause the execution of the script until a key on the keyboard is pressed
cv2.waitKey(0)