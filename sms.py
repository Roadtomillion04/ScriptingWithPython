# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python

import twilio
import twilio.rest

account_sid = 'AC349fc1413ec4b778baa48e87ba1e8421'
auth_token = 'b8a5392217470bc38ea610fa623e3dbb'
client = twilio.rest.Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='MG3c5d5577dcc099ee1fee41356d28f41b',
    body='Hi there, Nirmal How are you? Messaging YOU from PYTHON!',
    to='+918610846845'
)

print(message.sid)
