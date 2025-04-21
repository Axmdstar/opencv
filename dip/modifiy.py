import cv2 as cv
import numpy as np

# read image
im = cv.imread("images.jpg")
cv.imshow("lena.jpg", im)
# resize image
dim = (int(im.shape[1] * 1.3), int(im.shape[0] * 1.3))
im_rs_nr = cv.resize(im, dim, interpolation=cv.INTER_NEAREST)
im_rs_ln = cv.resize(im, dim, interpolation=cv.INTER_LINEAR)
im_rs_cb = cv.resize(im, dim, interpolation=cv.INTER_CUBIC)
im_rs_lz = cv.resize(im, dim, interpolation=cv.INTER_LANCZOS4)

# im_rs_lz = cv.resize(im, dim, interpolation=cv.INTER_LANCZ054)
cv.imshow("lena_rs_nr.jpg", im_rs_nr)
cv.imshow("lena_rs_ln.jpg", im_rs_ln)
cv.imshow("lena_rs_cb.jpg", im_rs_cb)
cv.imshow("lena_rs_lz.jpg", im_rs_lz)

# flip the image along the y-axis (horizontal flip))
im_flip = cv.flip(im, 1)
cv.imshow("lena_flip.jpg", im_flip)
# rotate the image around its center point
h, w = im.shape[:2]
M = cv.getRotationMatrix2D((w / 2, h / 2), 45, 1)
im_rt = cv.warpAffine(im, M, (w, h))
cv.imshow("lena_rt.jpg", im_rt)
# move 100 pixels in the negative direction along the x-axis
x = -100
y = 0
# M = np.float32([[1, 0, x], [0, 1, y]])

M = np.array([[1, 0, x], [0, 1, y]], dtype=np.float32)
im_trans = cv.warpAffine(im, M, (w, h))
cv.imshow("lena_trans.jpg", im_trans)
cv.waitKey()
