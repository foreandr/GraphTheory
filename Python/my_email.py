from email.message import EmailMessage
import ssl
import smtplib
from email.mime.text import MIMEText


def send_email(email):

    email_sender = "andrelogosdemo@gmail.com"
    password = 'bwtbtucxrjsmzzvy'
    reciver = email

    subject = "Forgot Password Recovery"
    msg = MIMEText(f'''
    <a href="http://localhost:5006/password_reset">Reset Password</a>
    ''', 'html')
    em = EmailMessage()

    em['From'] = email_sender
    em["To"] = reciver
    em['Subject'] = subject
    em.set_content(msg)

    context = ssl.create_default_context()
    # EMAIL SERVER
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, password)
        smtp.sendmail(email_sender, reciver, em.as_string())
    print("SENT EMAIL", email)

