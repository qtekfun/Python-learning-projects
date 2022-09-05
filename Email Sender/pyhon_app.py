from email.message import EmailMessage
from multiprocessing import context

# import pass from another file
from pass_file import email_password

# import needed libs
import ssl
import smtplib

# create email content
email_sender = 'qtekfun@gmail.com'
email_destination = ''
email_subject = "Pyhton test app"
email_body = """
hello, this is python app
"""

#create mail object
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_destination
em['subject'] = email_subject
em.set_content(email_body)

#send the email
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_destination, em.as_string())