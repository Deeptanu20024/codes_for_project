from email.message import EmailMessage
import ssl
import smtplib

email_sender="deeptanubhowmik47@gmail.com"
password_sender="mekhowrsrsnlapwu"
email_receiver="herodeeptanu482002@gmail.com"

subject="dont"
body="""
hi my name
is deeptanu
"""
em=EmailMessage()
em["From"]=email_sender
em["To"]=email_receiver
em["subject"]=subject
em.set_content(body)
contex=ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=contex) as smtp:
    smtp.login(email_sender, password_sender)
    smtp.sendmail(email_sender,email_receiver,em.as_string())
