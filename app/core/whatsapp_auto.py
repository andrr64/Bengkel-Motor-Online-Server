# app/utils/twilio_whatsapp.py
import os
from dotenv import load_dotenv
from twilio.rest import Client
from app.core.config import settings

TWILIO_ACCOUNT_SID =settings.TWILIO_ACCOUNT_SID
TWILIO_AUTH_TOKEN =settings.TWILIO_AUTH_TOKEN
TWILIO_WHATSAPP_NUMBER ="whatsapp:+14155238886"

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_whatsapp_message(to_number: str, message: str):
    try:
        message = client.messages.create(
            body=message,
            from_=TWILIO_WHATSAPP_NUMBER,
            to=f"whatsapp:{to_number}"
        )
        return {"sid": message.sid, "status": message.status}
    except Exception as e:
        print("Error sending WhatsApp message:", e)
        return None
