# Red Filter

from picamera2 import Picamera2 
import cv2, time
import numpy as np 

picam2 = Picamera2() 
config = picam2.create_preview_configuration(main={'size':(320, 240)})
picam2.configure(config) 
picam2.start() 
time.sleep(0.1)

while True: 
	frame = picam2.capture_array() # RGB
	bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR) # to BGR
	hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV) 

	lower_red1 = np.array([0, 50, 50]) 
	upper_red1 = np.array([10, 255, 255]) 
	mask1 = cv2.inRange(hsv, lower_red1, upper_red1) 

	lower_red2 = np.array([170, 50, 50]) 
	upper_red2 = np.array([180, 255, 255]) 
	mask2 = cv2.inRange(hsv, lower_red2, upper_red2) 

	mask = cv2.bitwise_or(mask1, mask2) 
	
	red_only = cv2.bitwise_and(bgr, bgr, mask=mask) 

	cv2.imshow('Original', bgr) 
	cv2.imshow('Mask', mask) 
	cv2.imshow('Result', red_only) 

	if cv2.waitKey(1) & 0xFF == ord('q'): 
		break

picam2.stop() 
cv2.destroyAllWindows()
