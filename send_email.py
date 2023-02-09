import smtplib


def send_email(message):
    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    server.login("rinobear05@outlook.com", "yakuta2r")
    server.send_message(message)
    server.quit()
