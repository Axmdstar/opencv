import cv2

# Load the color image
img = cv2.imread("me.jpg")
# Display original shape
smallsize = cv2.resize(img, (350, 660))
cv2.imshow("Src", smallsize)
crop = ""
# 82 189
# 259 538
while True:
    # roi = smallsize[100:200, 150:300]
    # Modify the region: Set it to blue
    crop = smallsize[130:500, 80:280]
    # r = cv2.selectROI("Image", smallsize, False)
    # Show the modified image
    cv2.imshow("Dest", crop)
    if cv2.waitKey(3) == ord("x"):
        break

cv2.imwrite("./Writeto/crop.jpg", crop)
