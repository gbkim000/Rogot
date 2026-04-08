import cv2
import numpy as np

src = cv2.imread('rose2.png')
cv2.imshow('src',src)

med_val = np.median(src)
# 하위 임계값을 0 또는 중앙의 70%로 설정하겠다는 의미이다.
lower = int(max(0, 0.7 * med_val))

# 상위 임계값을 130% 또는 255로 설정하겠다.
upper = int(min(255,1.3*med_val))

# 임계값을(높은/낮은 값) 만든다음 에지값만 받아내기

dst = cv2.GaussianBlur(src, (3,3), 0,0)

# 마스크가 클 수록 얇아지고 작을수록 커진다. 에지값이
dst = cv2.Canny(dst,lower, upper,3)


cv2.imshow('dst', dst)
cv2.waitKey()
