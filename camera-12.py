from gpiozero import Button
import time
from picamera2 import Picamera2, Preview

button = Button(2)

picam2 = Picamera2()
picam2.preview_configuration.main.size = (800, 600)
picam2.configure("preview")
picam2.start(show_preview=True)

cnt = 1

try:
    while True:
        if button.is_pressed:

            file_name = "Click" + str(cnt)
            print(file_name + ".jpg")

            picam2.capture_file(file_name + ".jpg")

            cnt += 1

            while button.is_pressed:
                time.sleep(0.01)

        time.sleep(0.01)

except KeyboardInterrupt:
    pass

