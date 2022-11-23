import smtplib, ssl
import os
from email.mime.text import MIMEText

'''
This is modular code to use for sending an email with the msg_str variable holding the string of email text to send. It is configured to use secret env variables defined below. It can be used to send to at&t cell email-to-text number in the variables.
'''
#define the text to send and assign to msg_str variable
msg_str = 'test message: trade bot text just executed'

def send_email(message):
    port = 465  # For SSL
    #define env variables below in secrets before use
    smtp_server = os.environ['smtp_server']
    sender_email = os.environ['sender_email']
    receiver_email = os.environ['receiver_email']
    sender_email_pw = os.environ['sender_email_pw']
    
    msg = MIMEText(msg_str)
    
    msg['Subject'] = 'Alpaca Trade Alert'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
      
      server.login(sender_email, sender_email_pw)
      server.sendmail(sender_email, [receiver_email], msg.as_string())
      print('mail successfully sent')
      
#uses send mail function to execute test email with msg_str text:
send_email(msg_str)


    
  