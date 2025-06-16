from twilio.rest import Client
from app.core.config import settings

account_sid = settings.TWILIO_ACCOUNT_SID
auth_token = settings.TWILIO_AUTH_TOKEN

client = Client(account_sid, auth_token)

def send_whatsapp_message(to: str, body: str):
    """
    Send a WhatsApp message using Twilio API.
    
    :param to: The recipient's WhatsApp number in the format 'whatsapp:+1234567890'.
    :param body: The message content to be sent.
    :return: The message SID if the message was sent successfully, otherwise raises an exception.
    """
    try:
        message = client.messages.create(
            from_=settings.TWILIO_PHONE_NUMBER,
            body=body,
            to=to
        )
        return message.sid
    except Exception as e:
        raise RuntimeError(f"Failed to send WhatsApp message: {str(e)}")