# mms only available in us and canada
# send/receive mms
# doesn't include people counting

from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request
from twilio.rest import Client

#from yolo_object_detection import countPeople
# http://6e06ec56.ngrok.io/sms


account_sid = 'ACf6de1d8ba49873dd53a9836ce60a36a0'
auth_token = '593c2ec2877155d4a8262c0607a76a11'
client = Client(account_sid, auth_token)

#C:\Users\Sharon Xia\Github\heckuci\yolo
#python twiddleyothumbs.py


app = Flask(__name__)
@app.route('/sms', methods=['GET', 'POST'])
def sms_reply():
    msg = request.values.get('Body').lower().strip()
    res = MessagingResponse()
    if msg == "matcha":
        res.message("noice")
    else:
        res.message("meh")

    return str(res)

if __name__ == "__main__":
    app.run(debug=True)