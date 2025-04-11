import cv2 as cv

image = cv.imread("images.jpg") 

print("Show Image")
cv.imshow("Image", image)
# cv.waitKey(0)


# Write to Writeto folder
cv.imwrite("./Writeto/new_img.jpg", image)

