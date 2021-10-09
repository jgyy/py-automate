"""
Manipulating Strings
"""
from sys import argv
from pyperclip import copy, paste


def wrapper1():
    """
    wrapper function part 1
    """
    spam = "That is Alice's cat."
    spam = 'Say hi to Bob\'s mother.'
    print("Hello there!\nHow are you?\nI\'m doing fine.")
    print(r'That is Carol\'s cat.')
    spam = 'Hello world!'
    print(spam[0])
    print(spam[4])
    print(spam[-1])
    print(spam[0:5])
    print(spam[:5])
    print(spam[6:])

    spam = 'Hello world!'
    fizz = spam[0:5]
    print(fizz)
    print('Hello' in 'Hello World')
    print('HELLO' in 'Hello World')
    print('' in 'spam')
    print('cats' not in 'cats and dogs')
    spam = 'Hello world!'
    spam = spam.upper()
    print(spam)
    spam = spam.lower()
    print(spam)
    print('How are you?')
    feeling = "sad"

    if feeling.lower() == 'great':
        print('I feel great too.')
    else:
        print('I hope the rest of your day is good.')
    spam = 'Hello world!'
    print(spam.islower())
    print(spam.isupper())

    print('HELLO'.isupper())
    print('abc12345'.islower())
    print('12345'.islower())
    print('12345'.isupper())
    print('Hello'.upper())
    print('Hello'.upper().lower())
    print('Hello'.upper().lower().upper())
    print('HELLO'.lower())
    print('HELLO'.lower().islower())
    print('hello'.isalpha())
    print('hello123'.isalpha())
    print('hello123'.isalnum())
    print('hello'.isalnum())
    print('123'.isdecimal())
    print('    '.isspace())


def wrapper2():
    """
    wrapper function part 2
    """
    print('This Is Title Case'.istitle())
    print('This Is Title Case 123'.istitle())
    print('This Is not Title Case'.istitle())
    print('This Is NOT Title Case Either'.istitle())
    while True:
        print('Enter your age:')
        age = input()
        if age.isdecimal():
            break
        print('Please enter a number for your age.')
    while True:
        print('Select a new password (letters and numbers only):')
        password = input()
        if password.isalnum():
            break
        print('Passwords can only have letters and numbers.')
    print('Hello world!'.startswith('Hello'))
    print('Hello world!'.endswith('world!'))
    print('abc123'.startswith('abcdef'))
    print('abc123'.endswith('12'))
    print('Hello world!'.startswith('Hello world!'))
    print('Hello world!'.endswith('Hello world!'))
    print(', '.join(['cats', 'rats', 'bats']))
    print(' '.join(['My', 'name', 'is', 'Simon']))
    print('ABC'.join(['My', 'name', 'is', 'Simon']))
    print('My name is Simon'.split())
    print('MyABCnameABCisABCSimon'.split('ABC'))
    print('My name is Simon'.split('m'))
    spam = '''Dear Alice,
    How have you been? I am fine.
    There is a container in the fridge
    that is labeled "Milk Experiment".

    Please do not drink it.
    Sincerely,
    Bob'''
    spam.split('\n')
    print('Hello'.rjust(10))
    print('Hello'.rjust(20))
    print('Hello World'.rjust(20))
    print('Hello'.ljust(10))
    print('Hello'.rjust(20, '*'))
    print('Hello'.ljust(20, '-'))
    print('Hello'.center(20))
    print('Hello'.center(20, '='))


def wrapper3():
    """
    wrapper function part 3
    """
    def print_picnic(items_dict, left_width, right_width):
        print('PICNIC ITEMS'.center(left_width + right_width, '-'))
        for key, value in items_dict.items():
            print(key.ljust(left_width, '.') + str(value).rjust(right_width))

    picnic_items = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
    print_picnic(picnic_items, 12, 5)
    print_picnic(picnic_items, 20, 6)
    spam = '    Hello World     '
    spam.strip()
    spam.lstrip()
    spam.rstrip()
    spam = 'SpamSpamBaconSpamEggsSpamSpam'
    spam.strip('ampS')
    copy('Hello world!')
    print(paste())

    passwords = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
                'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
                'luggage': '12345'}
    if len(argv) < 2:
        print('Usage: python pw.py [account] - copy account password')
    account = argv[1]
    if account in passwords:
        copy(passwords[account])
        print('Password for ' + account + ' copied to clipboard.')
    else:
        print('There is no account named ' + account)
    text = paste()
    copy(text)
    text = paste()
    lines = text.split('\n')
    for i, j in enumerate(lines):
        lines[i] = '* ' + j

    print('Hello world!'[1])
    print('Hello world!'[0:5])
    print('Hello world!'[:5])
    print('Hello world!'[3:])
    print('Hello'.upper())
    print('Hello'.upper().isupper())
    print('Hello'.upper().lower())
    print('Remember, remember, the fifth of November.'.split())
    print('-'.join('There can be only one.'.split()))
    table_data = [['apples', 'oranges', 'cherries', 'banana'],
                ['Alice', 'Bob', 'Carol', 'David'],
                ['dogs', 'cats', 'moose', 'goose']]

    def print_table(table):
        tablet = [
            "".join([table[indexr][indexc] for indexr, _ in enumerate(table)])
            for indexc, _ in enumerate(table[0])
        ]
        for i in tablet:
            print(" ".join(i))

    print_table(table_data)


if __name__ == "__main__":
    wrapper1()
    wrapper2()
    wrapper3()
