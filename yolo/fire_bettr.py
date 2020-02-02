
from funs import *
import time

conf = 0.5 #confidence percentage (0-1)
room_threshold = 1 #max num of ppl in room



#resize img
#img = cv2.resize(img, None, fx=0.4, fy=0.4)
img = 'testr.jpg'
ppl = smart_count(img, conf, True) #will display analysis

if(ppl > room_threshold):
    print("Too many people")
else:
    print("Safe!")
