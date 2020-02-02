# Text an image url from the web
# texts back the number of people in the photo

from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, redirect
from twilio.rest import Client
from yolo_object_detection_edit import countPeople
import cv2

import wget

account_sid = 'ACf6de1d8ba49873dd53a9836ce60a36a0'
auth_token = '593c2ec2877155d4a8262c0607a76a11'
client = Client(account_sid, auth_token)


app = Flask(__name__) #flask app is only if I want to receive messages
@app.route('/sms', methods=['GET', 'POST'])
def incoming_sms():
    image_url = request.values.get('Body').lower().strip()
    local_image_filename = wget.download(image_url)
    img = cv2.imread(local_image_filename)


    res = MessagingResponse()
    res.message("Number of People in Picture: " + str(countPeople(img)))
    
    return str(res)

if __name__ == "__main__":
    app.run(debug=True)
