import smtplib,ssl

port = 587

smtp_server = "smtp.gmail.com"
sender_emailu = "testu@gmail.com"
password="test"

def send_mail(email,token):
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server,port) as server:
        message = f"Heres Your Reset Token Link http://domainU/reset_passwordU?token={token}"
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_emailu,password)
        server.sendmail(sender_emailu,email,message)
        

