# from picamera2 import Picamera2
from picamera2 import Picamera2
from time import sleep
import cv2

picam2 = Picamera2()

picam2.preview_configuration.size = (2592, 1944) 
picam2.start(show_preview=True) 

sleep(2) 

picam2.capture_file('toProcess.jpg')  
picam2.close() 


img = cv2.imread('toProcess.jpg') 
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
inverted = 255-grayscale 
blur_inverted = cv2.GaussianBlur(inverted, (125, 125), 5) 
inverted_blur = 255-blur_inverted 
sketch = cv2.divide(grayscale, inverted_blur, scale=256) 
cv2.imwrite('sketchImage.jpg', sketch) 
cv2.imwrite('negativeImage.jpg', 255-grayscale)
