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
inverted = 255 - grayscale

cv2.imwrite('invertedImage.jpg', inverted)
