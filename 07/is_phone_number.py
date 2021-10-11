"""
is phone number
"""


def is_phone_number(text):
    """
    Criteria to reject phone numbers
    not phone number-sized
    not an area code
    does not have first hyphen
    does not have first 3 digits
    does not have second hyphen
    does not have last 4 digits
    "text" is a phone number!
    """
    check = True
    if len(text) != 12:
        check = False
    for i in range(0, 3):
        if not text[i].isdecimal():
            check = False
    if text[3] != '-':
        check = False
    for i in range(4, 7):
        if not text[i].isdecimal():
            check = False
    if text[7] != '-':
        check = False
    for i in range(8, len(text)):
        if not text[i].isdecimal():
            check = False
    return check


if __name__ == "__main__":
    print('415-555-4242 is a phone number:')
    print(is_phone_number('415-555-4242'))
    print('Moshi moshi is a phone number:')
    print(is_phone_number('Moshi moshi'))
