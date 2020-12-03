import os
import smtplib
from email.message import EmailMessage
import requests

dog_url = requests.get('https://dog.ceo/api/breeds/image/random').json()['message']

quote = requests.get('http://tintin-quotes-api.herokuapp.com/quotes/random').json()
quote_text = quote['text']
quote_author = quote['author']

message_body = f"""\
    🐶 Woof 🐶
    {dog_url}

    {quote_text}
    - {quote_author}
    """

html_message = f"""\
    <!DOCTYPE html>
<html lang="en">
  <body style="width: 400px">
    <p style="font-family: sans-serif; font-size: xx-large; margin-bottom: 30px; text-align: center;">🐶 Woof 🐶</p>
    <img src="{dog_url}" alt="cute dog" style="border-radius: 6px; width: 100%;" />

    <div>
      <p>
        {quote_text}
      </p>
      <p style="text-align: right"><em>- {quote_author}</em></p>
    </div>

    <div>
        <p>I put the smart people's words before my own because everytime I think about you every neuron in my brain goes in to overdrive and short-circuits. And, honestly what is there left to say except,</p>
        <p style="text-align: center"> ❤️ I love you ❤️ </p>
    <div>
  </body>
</html>
    """

user = os.environ.get('EMAIL_USER')
password = os.environ.get('EMAIL_PASSWORD')

msg = EmailMessage()

msg['Subject'] = '🐕'
msg['From'] = user
msg['To'] = ['upamanyudas16@gmail.com']
msg.set_content(message_body)
msg.add_alternative(html_message, subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(user, password)

    smtp.send_message(msg)


