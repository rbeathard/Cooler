from picamera import PiCamera
import time
camera = PiCamera()
time.sleep(2)
camera.resolution = (1280, 720)
camera.vflip = False
camera.contrast = 10
file_name = "/home/pi/Pictures/img_" + str(time.time()) + ".jpg"
camera.capture(file_name)
print("Done.")