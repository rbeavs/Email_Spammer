import send_email
from email.mime.text import MIMEText


def email():
    message = MIMEText("You Smell")
    message['subject'] = "Lots of Malware"
    message['from'] = "rinobear05@outlook.com"
    message['to'] = "beavers.ryan@usd109.org"
    send_email.send_email(message)
