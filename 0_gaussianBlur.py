import cv2

src = cv2.imread('rose.png', cv2.IMREAD_GRAYSCALE)

dst1 = cv2.GaussianBlur(src, (0,0), 3)
# 시그마 값 3에 의해 바뀜
dst2 = cv2.blur(src,(7,7))
# 7,7 마스크에 따라 바뀜

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)

cv2.waitKey()
