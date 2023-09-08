from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'rahuldhirendersingh@gmail.com'
email_password = 'daar bbut mlvv eqvd'

email_receiver = 'vanay25586@horsgit.com' # Temporary Email by temp-mail.org.

subject = 'Climate Change'
body = """
Climate change is a threat to the exsistence of mankind.
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    
