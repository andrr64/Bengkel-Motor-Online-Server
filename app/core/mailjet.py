from mailjet_rest import Client
from app.core.config import settings

mailjet = Client(auth=(settings.MJ_API_KEY, settings.MJ_API_SECRET), version='v3.1')

def send_email(to_email: str, subject: str, html_content: str):
    data = {
      'Messages': [
        {
          "From": {
            "Email": settings.MJ_FROM_EMAIL,
            "Name": "Bengkel Motor"
          },
          "To": [
            {
              "Email": to_email,
              "Name": "User"
            }
          ],  
          "Subject": subject,
          "HTMLPart": html_content
        }
      ]
    }

    result = mailjet.send.create(data=data)
    return result.status_code == 200