import cv2

# Load the color image
img = cv2.imread("images.jpg")
# Display original shape
cv2.imshow("Src", img)
# Define a ROI: rows 100–200 and columns 150–300
roi = img[100:200, 150:300]
# Modify the region: Set it to blue
img[100:200, 150:300] = [255, 0, 0]
# Show the modified image
cv2.imshow("Dest", img)
cv2.waitKey(0)
