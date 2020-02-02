from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request
from twilio.rest import Client
from yolo_object_detection_currentframe import currentNumPeople
import cv2

#import os



account_sid = 'ACf6de1d8ba49873dd53a9836ce60a36a0'
auth_token = '593c2ec2877155d4a8262c0607a76a11'
client = Client(account_sid, auth_token)


app = Flask(__name__) #flask app is only if I want to receive messages
@app.route('/sms', methods=['GET', 'POST'])
def incoming_sms():
    msg = request.values.get('Body').lower().strip()
    res = MessagingResponse()
    if msg == "update" or msg == "never gonna give you up":
        res.message("Number of People in Picture: " + str(currentNumPeople()))
    else:
        res.message("Invalid input")

    return str(res)

if __name__ == "__main__":
    app.run(debug=True)