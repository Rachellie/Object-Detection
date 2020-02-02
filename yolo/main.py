import cv2
from funs import *
from picam import *
import time

pi_capture() #saves capture in snap.jpg

imgg = cv2.imread("snap.jpg")

print(count_people(imgg, 0.4))
