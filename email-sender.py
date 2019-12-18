import smtplib, ssl
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('input.html').read_text())
email = EmailMessage()
email['from'] = 'Python Master'
email['to'] ='<to email address>'
email['subject'] = 'You won 100,000 dollars!'

email.set_content(html.substitute({'name' : 'Tintin'}),'html')
context = ssl.create_default_context()

#login to client and send email
with smtplib.SMTP_SSL(host='smtp.gmail.com',port=465,context=context) as smtp:
    # smtp.ehlo()
    # smtp.starttls() #encryption mechanism
    smtp.login('<from mail adress>','<password>') #credentials
    smtp.send_message(email)
    print('everything works!')
