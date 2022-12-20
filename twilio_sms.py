import os
from twilio.rest import Client
import keys

def sms_auth(present:str, missing : str, phone_number : str , name: str ):

    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    client = Client(keys.account_sid, keys.auth_token)

    message = client.messages.create(
            body=f'Dear {name} , There are currently {present} students in the hostel. The number of missing students is {missing}.',
            from_='+14454477617',
            to = phone_number
        )

def sms_leave(name:str, sid:str, date:str, time:str, parent_phone:str):
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    client = Client(keys.account_sid, keys.auth_token)

    message = client.messages.create(
            body=f'Hello, Your ward {name} (SID : {sid}) has left the hostel premises on {date} at {time}.\nVindhya Hostel',
            from_='+14454477617',
            to = parent_phone
        )
    
def sms_leave_auth(name:str, sid:str, date:str, time:str, phone_number:str):
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    client = Client(keys.account_sid, keys.auth_token)

    message = client.messages.create(
            body=f'Hello, Student {name} (SID : {sid}) has left the hostel premises on {date} at {time}.',
            from_='+14454477617',
            to = parent_phone
        )