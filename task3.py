import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time

def send_email(to_address, subject, message):
    # Email configuration
    from_address = 'lokesharya78@gmail.com'
    app_password = '123455678'

    # Create message
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    # Attach the message to the email
    msg.attach(MIMEText(message, 'plain'))

    # Setup the server
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        # Login to the email account
        server.login(from_address, app_password)

        # Send the email
        server.sendmail(from_address, to_address, msg.as_string())

def send_reminder():
    to_address = 'bhumirya04@gmail.com'
    subject = 'Reminder: Your Task'
    message = 'This is a reminder for your task. Do not forget to complete it.'

    send_email(to_address, subject, message)

# Schedule the reminder to be sent every day at a specific time (adjust as needed)
schedule.every().day.at("09:00").do(send_reminder)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
