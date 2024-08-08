import smtplib
from email.mime.text import MIMEText
from jinja2 import Template
import requests

def send_email(email,token):
   d = open("emailU.html").read()
   body = Template(d).render(token=token)
   subject = "Forgot Password"
   sender = "administrator@blockwiselearning.com"
   data = {"from":sender,"to":email,"subject":subject,"text":token}
   url = "https://78e09c4ef5b9bb195c9ab658:@api.forwardemail.net/v1/emails"
   r = requests.post(url,data=data)
   print(r.text)



def register_email(email,token):
   d = open("emailU.html").read()
   body = Template(d).render(token=token)
   subject = "Welcome to Sahasra AI - Use This OTP to Get Started"
   sender = "administrator@blockwiselearning.com"
   data = {"from":sender,"to":email,"subject":subject,"html":body}
   url = "https://78e09c4ef5b9bb195c9ab658:@api.forwardemail.net/v1/emails"
   r = requests.post(url,data=data)
   print(r.text)
   '''recipients = [email]
   password = "Bisleri12!@"
   msg = MIMEText(body,"html")
   msg['Subject'] = subject
   msg['From'] = sender
   msg['To'] = ', '.join(recipients)
   with smtplib.SMTP_SSL('webhosting2052.is.cc', 465) as smtp_server:
      print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
      smtp_server.login(sender, password)
      print(recipients)
      smtp_server.sendmail(sender, recipients, msg.as_string())
   print("Message sent!")'''
