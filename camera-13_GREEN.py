# Blue Filter

from picamera2 import Picamera2 
import cv2 
import numpy as np 

picam2 = Picamera2() 
config = picam2.create_preview_configuration(main={'size':(320, 240)})
picam2.configure(config) 
picam2.start() 
 
while True: 
	frame = picam2.capture_array() # RGB
	# hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV) 
	bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR) # to BGR
	hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV) 

	lower_green = (35, 100, 50)
	upper_green = (85, 255, 255)

	mask = cv2.inRange(hsv, lower_green, upper_green) 

	green_only = cv2.bitwise_and(bgr, bgr, mask=mask) 

	cv2.imshow('Original', bgr) 
	cv2.imshow('Mask', mask) 
	cv2.imshow('Result', green_only) 

	if cv2.waitKey(1) & 0xFF == ord('q'): 
		break

picam2.stop() 
cv2.destroyAllWindows()
