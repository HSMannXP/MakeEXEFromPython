import os

while True:
    print('Welcome to MakeEXEFromPython') # Welcome
    print('Please run this on console window')
    ch = input('Installed Pyinstaller?(y,n): ')

    if ch.lower() == 'y':
        x = input('Where is *.py?(ex:D:\main.py): ')
        y = input('Name: ')
        os.system(f'pyinstaller -F -n {y}.exe {x}')
        break
    elif ch.lower() == 'n':
        os.system('pip install pyinstaller')