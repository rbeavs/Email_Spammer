import os
import platform
from rich import print
from single_email import single_email
from multiple_email import multiple_emails
import sys

if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

art = '[bold cyan]     ░█▀▀░█▄█░█▀█░▀█▀░█░░░░░█▀▄░█▀█░█▄█░█▀▄░█▀▀░█▀▄\n     ░█▀▀░█░█░█▀█░░█░░█░░░░░█▀▄░█░█░█░█░█▀▄░█▀▀░█▀▄\n     ░▀▀▀░▀░▀░▀░▀░▀▀▀░▀▀▀░░░▀▀░░▀▀▀░▀░▀░▀▀░░▀▀▀░▀░▀'

def home():
    print('\n')
    print(art)
    print('\n')
    print('[bold cyan]     ______________________________________________')
    print("\n [1] Email One Person ")
    print("\n [2] Email A List of People ")
    user = input("\n -> ")

    try:
        if user == '1':
            single_email()
        elif user == '2':
            multiple_emails()
        else:
            print('[bold red] [!] Unrecognized Input ')
            sys.exit()

    except KeyboardInterrupt:
        print('\n[bold red] [-] Bombing Interrupted')
        sys.exit()
