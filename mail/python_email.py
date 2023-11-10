from email.message import EmailMessage
from app2 import password1
import ssl
import smtplib

email_sender='taashnathedreamer70320@gmail.com'
email_password=password1

email_reciever='dodeci6699@newnime.com'

subject='Daily motivation'
body="""
A reminder to all to believe in themselves, 
let's bring everyone together and prosper

Excellence is not an act, it's a habit

"""
em=EmailMessage()
em['From']=email_sender
em['To']=email_reciever
em['subject']=subject
em.set_content(body)

context1=ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context1) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())



