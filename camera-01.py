from picamera2 import Picamera2
from time import sleep

picam2 = Picamera2() 
picam2.preview_configuration.size = (1024, 768)
picam2.configure('preview') 
picam2.start(show_preview=True) 

sleep(2) 

picam2.capture_file('max_1024.jpg') 
picam2.close()
