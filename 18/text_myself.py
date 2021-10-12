"""
Defines the textmyself() function that texts a message passed to it as a string.
"""
from twilio.rest import Client


def textmyself(message):
    """
    will not work
    """
    account_sid = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    auth_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    my_number = "+15559998888"
    twilio_number = "+15552225678"
    twilio_cli = Client(account_sid, auth_token)
    twilio_cli.messages.create(body=message, from_=twilio_number, to=my_number)


if __name__ == "__main__":
    textmyself("1234567890qwertyuiopasdfghjklzxcvbnm")
