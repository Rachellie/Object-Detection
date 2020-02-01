import cv2
from funs import *
import time

conf = 0.5 #confidence percentage (0-1)
room_threshold = 1 #max num of ppl in room

#def count_people(image, conf_thresh=0.5 ,showSample=False):
#showSample, will display analysis with boxes around people

#take picture from laptop
img = take_still_laptop()

#or use local image
#img = cv2.imread('testr.jpg')

#resize img
#img = cv2.resize(img, None, fx=0.4, fy=0.4)

ppl = count_people(img, conf, True) #will display analysis

if(ppl > room_threshold):
    print("Too many people")
else:
    print("Safe!")
