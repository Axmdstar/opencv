import cv2 as cv

image = cv.imread("me.jpg")
image = cv.resize(image, (350, 660))
imageG = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

print("Show Image")
cv.imshow("Image", imageG)
cv.waitKey(0)


# Write to Writeto folder
cv.imwrite("./Writeto/new_img.jpg", image)
