import smtplib , ssl
import os

def send_email(mess):
    host='smtp.gmail.com'
    port=465

    username='phanivikash@gmail.com'
    password= os.getenv("PASSWORD")
    receiver='phanivikash@gmail.com'

    content=ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=content) as server:
        server.login(user=username,password=password)
        server.sendmail(username,receiver,msg=mess)
