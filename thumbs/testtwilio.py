## imports image from image's url
## counts number of people in imported image
## brute sends # of people to txt
## not a reply program


from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request
from twilio.rest import Client
from yolo_object_detection_edit import countPeople
import cv2

#import os

import wget


# Your Account Sid and Auth Token from twilio.com/user/account
"""account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)
"""

image_url = "https://upload.wikimedia.org/wikipedia/commons/1/12/Flickr_-_moses_namkung_-_The_Crowd_For_DMB_1.jpg"
local_image_filename = wget.download(image_url)
img = cv2.imread(local_image_filename)


account_sid = '###'
auth_token = '###'

client = Client(account_sid, auth_token)

string = 'Number of People in Picture: ' + str(countPeople(img))

message = client.messages.create(
         body=string,
         from_='+14243425576',
         to='+18587808856' # or your phone number
     )

print(message.sid)
