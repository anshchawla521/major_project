import os
from twilio.rest import Client
import keys

def sms(present:str, missing : str, phone_number : str , name: str ):

    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    client = Client(keys.account_sid, keys.auth_token)

    message = client.messages.create(
            body=f'Dear {name} , There are currently {present} students in the hostel. The number of missing students is {missing}.',
            from_='+14454477617',
            to = phone_number
        )

    print(message.sid)
