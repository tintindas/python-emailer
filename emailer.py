# import required libraries
import os
import smtplib
from email.message import EmailMessage
import requests

# Fetch dog image
dog_url = requests.get('https://dog.ceo/api/breeds/image/random').json()['message']


# Message to send if HTML is disabled
message_body = f"""\
    🐶 Woof 🐶
    {dog_url}

    ❤️ I love you ❤️ 
    """

# HTML message
html_message = f"""\
    <!DOCTYPE html>
<html lang="en">
  <body style="width: 400px">
    <p style="font-family: sans-serif; font-size: xx-large; margin-bottom: 30px; text-align: center;">🐶 Woof 🐶</p>
    <img src="{dog_url}" alt="cute dog" style="border-radius: 6px; width: 100%;" />

    <div> 
        <p style="text-align: center"> ❤️ I love you ❤️ </p>
    <div>
  </body>
</html>
    """

# Google Auth secrets
user = os.environ.get('EMAIL_USER')
password = os.environ.get('EMAIL_PASSWORD')
to_email = os.environ.get('TO_EMAIL')

# Email content
msg = EmailMessage()

msg['Subject'] = '🐕'
msg['From'] = user
msg['To'] = ['upamanyudas16@gmail.com', to_email]
msg.set_content(message_body)
msg.add_alternative(html_message, subtype='html')

# Send Email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(user, password)

    smtp.send_message(msg)


