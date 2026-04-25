import smtplib
from email.message import EmailMessage

def send_email(subject, body, to_email):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = "your_email@gmail.com"

    # Use Gmail's SMTP server
    with smtplib.SMTP_SSL('://gmail.com', 465) as smtp:
        smtp.login("your_email@gmail.com", "your_app_password")
        smtp.send_message(msg)
    print("Email sent!")
