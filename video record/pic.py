from picamera import PiCamera
from time import sleep
camera = PiCamera()
camera.start_preview()
camera.start_recording('/home/pi/video.h264')
sleep(5*60)
camera.stop_preview()
