from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request
from twilio.rest import Client
from yolo_object_detection_currentframe import currentNumPeople
import cv2

#import os



account_sid = 'ACf6de1d8ba49873dd53a9836ce60a36a0'
auth_token = '593c2ec2877155d4a8262c0607a76a11'
client = Client(account_sid, auth_token)

ROOM_CAPACITY = 3 # can change


app = Flask(__name__) #flask app is only if I want to receive messages
@app.route('/sms', methods=['GET', 'POST'])
def incoming_sms():
    msg = request.values.get('Body').lower().strip()
    res = MessagingResponse()
    if msg == "update" or msg == "never gonna give you up":
        numpeople = currentNumPeople()
        if numpeople < ROOM_CAPACITY:
            res.message("Number of people in picture: " + str(numpeople) + '\n'
            	+ "You are " + str(ROOM_CAPACITY - numpeople) + 
            	" people away from the room's max capacity, " + str(ROOM_CAPACITY))
        else:
            res.message("Number of people in picture: " + str(numpeople) + '\n' +
            	"You have reached the room's max capacity of " +
                str(ROOM_CAPACITY) + " people. You are over by " +
                str(numpeople - ROOM_CAPACITY) + " people (person).")
    else:
        res.message("Invalid input")

    return str(res)

if __name__ == "__main__":
    app.run(debug=True)