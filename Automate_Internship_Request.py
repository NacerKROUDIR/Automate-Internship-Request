import gspread as gs
import pandas as pd
import numpy as np
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Import the data from Google Sheets
gc = gs.service_account(filename='GoogleSheetCredentials.json')
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1CGjrzp4MSpGiMmdja3JXmFlY7IgtgQpeXVUPFIN6j7k/edit#gid=0')
# Select the worksheet
ws = sh.worksheet('Sheet1')
df = pd.DataFrame(ws.get_all_records())

# Filter for rows with emails
df_with_emails = df[df['Email'].str.contains('@')]

# Sender email address
from_address = "email.address@gmail.com"

# Send the emails one by one
for index,row in df_with_emails.iterrows():
    try:  
        to_address = row['Email']
        # instance of MIMEMultipart
        msg = MIMEMultipart()
        msg['From'] = from_address
        msg['To'] = to_address
        msg['Subject'] = row['Email Subject']
        body = row['Email Body']
        msg.attach(MIMEText(body, 'plain'))

        # open the file to be sent
        filename = "Resume.pdf"
        attachment = open("Resume.pdf", "rb")
        # instance of MIMEBase and named as p
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        # encode into base64
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(p)

        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(from_address, "app-password")

        # Converts the Multipart msg into a string
        text = msg.as_string()

        # sending the mail
        s.sendmail(from_address, to_address, text)

        # terminating the session
        s.quit()
        print(f"Email sent to {row['Enterprise']}")
    except:
        print(f"Failed to send email to {row['Enterprise']}")
print('Done')