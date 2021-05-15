import re


def email_check(email):
    if re.match(r'[^@]+@[^@]+\.[^@]', email):
        return True
    return False

