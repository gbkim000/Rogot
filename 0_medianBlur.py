import cv2

src = cv2.imread('noise.png', cv2.IMREAD_GRAYSCALE)

dst = cv2.medianBlur(src,5)

cv2.imshow('src', src)
cv2.imshow('dst', dst)

cv2.waitKey()
