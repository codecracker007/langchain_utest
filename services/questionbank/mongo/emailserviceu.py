import smtplib
from email.mime.text import MIMEText
from jinja2 import Template
import requests

def send_email(email,token):
   d = open("forgotpasswordU.html").read()
   body = Template(d).render(otp=token)
   subject = "Forgot Password"
   sender = "no-reply@sahasra.ai"
   data = {"from":sender,"to":email,"subject":subject,"html":body}
   url = "https://6c5d34701c432e9598fc80e5:@api.forwardemail.net/v1/emails"
   r = requests.post(url,data=data)
   print(r.text)



def register_email(email,token):
   d = open("emailU.html").read()
   body = Template(d).render(token=token)
   subject = "Welcome to Sahasra AI - Use This OTP to Get Started"
   sender = "no-reply@sahasra.ai"
   data = {"from":sender,"to":email,"subject":subject,"html":body}
   url = "https://6c5d34701c432e9598fc80e5:@api.forwardemail.net/v1/emails"
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

def register_phoneNumberU(number,token):
   url = "https://secureapi.sendshortly.com/api/sms/send"
   ubody={
    "apikey": "l42vEftXlufH9Hpa3vk8",
    "peid": "1001580741702775000",
    "senderid": "SAHAAI",
    "templateid": "1007120435373993437",
    "phonenumber": f"{number}",
    "message": f"Your Sahasra signup OTP is {token}. Please enter this code to verify your mobile number. The code is valid for 10 minutes. Do not share it with anyone.",
    "templatetype": "serviceimplicit"
}
   print(ubody)
   r = requests.post(url,json=ubody)
   print(r.content)
   if r.status_code == 200:
      return True
   return False   

def send_phoneNumberU(number,token):
   url = "https://secureapi.sendshortly.com/api/sms/send"
   ubody={
    "apikey": "l42vEftXlufH9Hpa3vk8",
    "peid": "1001580741702775000",
    "senderid": "SAHAAI",
    "templateid": "1007120435373993437",
    "phonenumber": f"{number}",
    "message": f"Your Sahasra Forgot Password OTP is {token}. Please enter this code to verify And Change Your Password. The code is valid for 10 minutes. Do not share it with anyone.",
    "templatetype": "serviceimplicit"
}
   r = requests.post(url,json=ubody)
   print(r.content)
   if r.status_code == 200:
      return True
   return False  