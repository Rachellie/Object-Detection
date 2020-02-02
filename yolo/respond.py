# mms only available in us and canada
# send/receive mms??? might need C#

from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request
from twilio.rest import Client
from funs import *
#from picam import *



account_sid = 'AC8550ac766e49ad6908236d3431804369'
auth_token = '983e1ae21f61259b62288b7d9e1c2678'
client = Client(account_sid, auth_token)


def get_str():
    #name = pi_capture()
    #num = smart_count(name, 0.5, False)

    num = smart_count1(0.5, False)
    capacity = 500
    string = "Number of people in room: "+str(num)+"\n"
    return string+("Below maximum capacity by: "+str(capacity-num) \
                   if num < capacity else "Above maximum capacity by: " \
                   +str(num-capacity) if num > capacity else \
                   "AT MAXIMUM CAPACITY")


app = Flask(__name__)
@app.route('/sms', methods=['GET', 'POST'])
def sms_reply():
    msg = request.values.get('Body').lower().strip()
    res = MessagingResponse()
    if ('update' in msg):
        res.message(get_str())
    else:
        res.message('unknown command')
    return str(res)
    
if __name__ == "__main__":
    app.run(debug=True)
