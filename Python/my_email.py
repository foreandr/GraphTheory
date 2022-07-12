# 16 char pass: bwtbtucxrjsmzzvy
from email.message import EmailMessage
import ssl
import smtplib
email_sender = "andrelogosdemo@gmail.com"
password = 'bwtbtucxrjsmzzvy'
reciver = "foreandr@gmail.com"

subject = "hi subject"
body = """
test body
"""
em = EmailMessage()

em['From'] = email_sender
em["To"] = reciver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
                       # EMAIL SERVER
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, password)
    smtp.sendmail(email_sender, reciver, em.as_string())


