import cv2
from detect_people import count_people

imgg = cv2.imread("test6.jpg")

print(count_people(imgg, 0.4))
