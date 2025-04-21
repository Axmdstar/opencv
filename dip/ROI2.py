import cv2

# Load the images
img1 = cv2.imread("images3.png")
img2 = cv2.imread("images2.png")

# Display original shape
cv2.imshow("Src1", img1)
cv2.imshow("Src2", img2)

# Define a ROIs:
roi1 = img1[246:953, 120:961]
roi2 = img2[197:814, 18:747]
roi2 = cv2.resize(roi2, (roi1.shape[1], roi1.shape[0]))

# Show the ROI
cv2.imshow("ROI1", roi1)
cv2.imshow("ROI2", roi2)

# Modify the region
img1[246:953, 120:961] = roi2

# Show the modified image
cv2.imshow("Dest", img1)
cv2.waitKey(0)
