import os 
import smtplib
import ssl
from email.message import EmailMessage 

sender = "sm.minoor.karim@g.bracu.ac.bd"
pwd = os.environ.get("email_pass")
receiver = "minoor01@gmail.com"

subject = "Invitation to Rythm Revive 22.3"

body = """Dear Applicants,

We welcome you to our enrollment event, Rhythm Revive 22.3, which aims to provide the prospective members the taste of what the club has to offer. The event will commence from 2 pm onwards, trailed by the interview session. 


Please look into the pdf attached below, to get your assigned token numbers for the interview period. In case of any crises, please contact us beforehand. Thank you.


Date: 16th October 2022

Time: 

Venue: UB2 Auditorium

Regards"""

em = EmailMessage()
em["From"] = sender
em["To"] = receiver
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",465,context = context) as smtp:
    smtp.login(sender,pwd)
    smtp.sendmail(sender,receiver,em.as_string(body))
