#send email through python through tls
#reference: https://realpython.com/python-send-email/

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "sender@domain.com"
receiver_email = "receiver@gmail.com"
password = input("Type your password and press enter:")

# Create message container - the correct MIME type is multipart/alternative.
message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """
Hi,
How are you?
This is a text email
"""
html = """
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       This is a html email<br>
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
with smtplib.SMTP("smtp.domain.com", 587) as smtp:
    smtp.login(sender_email, password)
    smtp.sendmail(
        sender_email, receiver_email, message.as_string()
    )
