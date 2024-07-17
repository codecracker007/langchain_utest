import smtplib
from email.mime.text import MIMEText




def send_email(email,token):
    subject = "Forgot Password"
    body = f"Here is your reset password link https://sahasra.ai/ressetpassword?token={token}"
    sender = "administrator@sahasra.ai"
    recipients = [email]
    password = "Bisleri12!@"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('webhosting2052.is.cc', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")