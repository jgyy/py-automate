"""
Pattern Matching with Regular Expressions
"""
import re
from re import VERBOSE
from pyperclip import copy, paste


def wrapper1():
    """
    wrapper function part 1
    """

    def is_phone_number(text):
        if len(text) != 12 or text[3] != "-":
            return False
        for i in range(0, 3):
            if not text[i].isdecimal():
                return False
        for i in range(4, 7):
            if not text[i].isdecimal():
                return False
        if text[7] != "-":
            return False
        for i in range(8, 12):
            if not text[i].isdecimal():
                return False
        return True

    print("415-555-4242 is a phone number:")
    print(is_phone_number("415-555-4242"))
    print("Moshi moshi is a phone number:")
    print(is_phone_number("Moshi moshi"))
    message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."
    for i in range(len(message)):
        chunk = message[i : i + 12]
        if is_phone_number(chunk):
            print("Phone number found: " + chunk)

    print("Done")
    phone_num_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
    mobile = phone_num_regex.search("My number is 415-555-4242.")
    print("Phone number found: " + mobile.group())
    phone_num_regex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
    mobile = phone_num_regex.search("My number is 415-555-4242.")
    print(mobile.group(1))
    print(mobile.group(2))
    print(mobile.group(0))
    print(mobile.group())
    print(mobile.groups())

    area_code, main_cumber = mobile.groups()
    print(area_code)
    print(main_cumber)
    phone_num_regex = re.compile(r"(\(\d\d\d\)) (\d\d\d-\d\d\d\d)")
    mobile = phone_num_regex.search("My phone number is (415) 555-4242.")
    print(mobile.group(1))
    print(mobile.group(2))


def wrapper2():
    """
    wrapper function part 2
    """
    hero_regex = re.compile(r"Batman|Tina Fey")
    mo1 = hero_regex.search("Batman and Tina Fey.")
    print(mo1.group())
    mo2 = hero_regex.search("Tina Fey and Batman.")
    print(mo2.group())
    bat_regex = re.compile(r"Bat(man|mobile|copter|bat)")
    mobile = bat_regex.search("Batmobile lost a wheel")
    print(mobile.group())
    print(mobile.group(1))

    bat_regex = re.compile(r"Bat(wo)?man")
    mo1 = bat_regex.search("The Adventures of Batman")
    print(mo1.group())
    mo2 = bat_regex.search("The Adventures of Batwoman")
    print(mo2.group())
    phone_regex = re.compile(r"(\d\d\d-)?\d\d\d-\d\d\d\d")
    mo1 = phone_regex.search("My number is 415-555-4242")
    print(mo1.group())

    mo2 = phone_regex.search("My number is 555-4242")
    print(mo2.group())
    bat_regex = re.compile(r"Bat(wo)*man")
    mo1 = bat_regex.search("The Adventures of Batman")
    print(mo1.group())
    mo2 = bat_regex.search("The Adventures of Batwoman")
    print(mo2.group())
    mo3 = bat_regex.search("The Adventures of Batwowowowoman")
    print(mo3.group())
    bat_regex = re.compile(r"Bat(wo)+man")
    mo1 = bat_regex.search("The Adventures of Batwoman")
    print(mo1.group())

    mo2 = bat_regex.search("The Adventures of Batwowowowoman")
    print(mo2.group())
    mo3 = bat_regex.search("The Adventures of Batman")
    print(mo3 is None)
    ha_regex = re.compile(r"(Ha){3}")
    mo1 = ha_regex.search("HaHaHa")
    print(mo1.group())
    mo2 = ha_regex.search("Ha")
    print(mo2 is None)
    greedy_ha_regex = re.compile(r"(Ha){3,5}")
    mo1 = greedy_ha_regex.search("HaHaHaHaHa")
    print(mo1.group())
    non_greedy_ha_regex = re.compile(r"(Ha){3,5}?")
    mo2 = non_greedy_ha_regex.search("HaHaHaHaHa")
    print(mo2.group())


def wrapper3():
    """
    wrapper function part 3
    """
    phone_num_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
    mobile = phone_num_regex.search("Cell: 415-555-9999 Work: 212-555-0000")
    print(mobile.group())
    phone_num_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
    print(phone_num_regex.findall("Cell: 415-555-9999 Work: 212-555-0000"))
    phone_num_regex = re.compile(r"(\d\d\d)-(\d\d\d)-(\d\d\d\d)")
    print(phone_num_regex.findall("Cell: 415-555-9999 Work: 212-555-0000"))
    xmas_regex = re.compile(r"\d+\s\w+")

    print(
        xmas_regex.findall(
            "12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, "
            + "7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge"
        )
    )
    vowel_regex = re.compile(r"[aeiouAEIOU]")
    print(vowel_regex.findall("Robocop eats baby food. BABY FOOD."))
    consonant_regex = re.compile(r"[^aeiouAEIOU]")
    print(consonant_regex.findall("Robocop eats baby food. BABY FOOD."))
    begins_with_hello = re.compile(r"^Hello")
    print(begins_with_hello.search("Hello world!"))
    print(begins_with_hello.search("He said hello.") is None)

    ends_with_number = re.compile(r"\d$")
    print(ends_with_number.search("Your number is 42"))
    print(ends_with_number.search("Your number is forty two.") is None)
    whole_string_is_num = re.compile(r"^\d+$")
    print(whole_string_is_num.search("1234567890"))
    print(whole_string_is_num.search("12345xyz67890") is None)
    print(whole_string_is_num.search("12 34567890") is None)

    at_regex = re.compile(r".at")
    print(at_regex.findall("The cat in the hat sat on the flat mat."))
    name_regex = re.compile(r"First Name: (.*) Last Name: (.*)")
    mobile = name_regex.search("First Name: Al Last Name: Sweigart")
    print(mobile.group(1))
    print(mobile.group(2))
    non_greedy_regex = re.compile(r"<.*?>")
    mobile = non_greedy_regex.search("<To serve man> for dinner.>")
    print(mobile.group())
    greedy_regex = re.compile(r"<.*>")
    mobile = greedy_regex.search("<To serve man> for dinner.>")
    print(mobile.group())


def wrapper4():
    """
    wrapper function part 4
    """
    no_new_line_regex = re.compile(".*")
    print(
        no_new_line_regex.search(
            "Serve the public trust.\nProtect the innocent.\nUphold the law."
        ).group()
    )
    newline_regex = re.compile(".*", re.DOTALL)
    print(
        newline_regex.search(
            "Serve the public trust.\nProtect the innocent.\nUphold the law."
        ).group()
    )
    robocop = re.compile(r"robocop", re.I)
    print(robocop.search("Robocop is part man, part machine, all cop.").group())
    print(robocop.search("ROBOCOP protects the innocent.").group())
    print(
        robocop.search(
            "Al, why does your programming book talk about robocop so much?"
        ).group()
    )
    names_regex = re.compile(r"Agent \w+")
    names_regex.sub("CENSORED", "Agent Alice gave the secret documents to Agent Bob.")
    agent_names_regex = re.compile(r"Agent (\w)\w*")
    agent_names_regex.sub(
        r"\1****",
        "Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.",
    )
    phone_regex = re.compile(
        r"""(
        (\d{3}|\(\d{3}\))?                # area code
        (\s|-|\.)?                        # separator
        (\d{3})                           # first 3 digits
        (\s|-|\.)                         # separator
        (\d{4})                           # last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
        )""",
        VERBOSE,
    )
    email_regex = re.compile(
        r"""(
        [a-zA-Z0-9._%+-]+      # username
        @                      # @ symbol
        [a-zA-Z0-9.-]+         # domain name
        (\.[a-zA-Z]{2,4})      # dot-something
        )""",
        VERBOSE,
    )
    text = str(paste())
    matches = []
    for groups in phone_regex.findall(text):
        phone_num = "-".join([groups[1], groups[3], groups[5]])
        if groups[8] != "":
            phone_num += " x" + groups[8]
        matches.append(phone_num)
    for groups in email_regex.findall(text):
        matches.append(groups[0])
    for groups in email_regex.findall(text):
        matches.append(groups[0])
    if len(matches) > 0:
        copy("\n".join(matches))
        print("Copied to clipboard:")
        print("\n".join(matches))
    else:
        print("No phone numbers or email addresses found.")


if __name__ == "__main__":
    wrapper1()
    wrapper2()
    wrapper3()
    wrapper4()
