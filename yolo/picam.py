from picamera import PiCamera
from time import sleep

camera = PiCamera()


def pi_capture():
	sleep(2)
	camera.capture('snap.jpg')
