import bimmer_connected
from bimmer_connected.account import ConnectedDriveAccount
from bimmer_connected.country_selector import Regions
import os
from twilio.rest import Client
import json

twilio_account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
twilio_auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
sms_from = os.environ.get('SMS_FROM')
receivers = os.environ.get('SMS_RECEIVERS').split(",")
login = {
            'username': os.environ.get('BMW_USERNAME'), 
            'password': os.environ.get('BMW_PASSWORD'),
            "regions": Regions(2)
        }

def notify_lock_state(vehicle):
    message = f"{vehicle.name} is {vehicle.status.door_lock_state}"
    for receiver in receivers:
        print(f"SENDING SMS: '{message}' to {receiver}")
        send_sms(message, receiver)
    
def send_sms(message, number):
    client = Client(twilio_account_sid, twilio_auth_token)
    message = client.messages \
    .create(
         body=message,
         from_=sms_from,
         to=number
     )

def handler(event, context):
    
    sendSuccessNotification = os.environ.get('SEND_SUCCESS_NOTIFICATION')

    try:
        print("Connecting to BMW Connected")
        account = ConnectedDriveAccount(login["username"], login["password"], login["regions"])
        print(f"Fetched {str(len(account.vehicles))} vehicles")

        for vehicle in account.vehicles:
            print(f"Vehicle {vehicle.name} is {vehicle.status.door_lock_state}")
            if vehicle.status.door_lock_state != "LOCKED" or sendSuccessNotification == "true":
                notify_lock_state(vehicle)

        return {
            'statusCode': 200,
            'body': json.dumps('Completed BMW notify check')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(e)
        }

if __name__ == "__main__":
    handler(None, None)
