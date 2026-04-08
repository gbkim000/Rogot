
from picamera2 import Picamera2
from time import sleep
import cv2

picam2 = Picamera2()

picam2.preview_configuration.size = (800, 600) 
picam2.start(show_preview=True) 

sleep(2) 

picam2.capture_file('toProcess.jpg')  
picam2.close() 


img = cv2.imread('toProcess.jpg') 
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
cv2.imwrite('grayscaleImage.jpg', grayscale)
# 
sleep(5)
cv2.imshow('Grayscale Image', grayscale)

# 아무 키 입력 시 창 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()
S
