import cv2 as cv
import numpy as np

# read image
im = cv.imread("images.jpg")
# cv.imshow("lena.jpg", im)

# Calculate the affine transformation matrix using
# three pairs of corresponding points from the original and target images
# M = np.array([[1, 0, x], [0, 1, y]], dtype=np.float32)
srcTri = np.array(
    [[0, 0], [im.shape[1] - 1, 0], [0, im.shape[0] - 1]], dtype=np.float32
)
dstTri = np.array(
    [
        [0, im.shape[1] * 0.3],
        [im.shape[1] * 0.9, im.shape[0] * 0.2],
        [im.shape[1] * 0.1, im.shape[0] * 0.7],
    ],
    dtype=np.float32,
)
warp_mat = cv.getAffineTransform(srcTri, dstTri)

# Perform an affine transformation on the original image
# to obtain the target image.
im_affine = cv.warpAffine(im, warp_mat, (im.shape[1], im.shape[0]))
cv.imshow("im_affine.jpg", im_affine)
cv.waitKey()
cv.destroyAllWindows()
