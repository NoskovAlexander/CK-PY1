import string
from random import sample


def get_random_password(length=8) -> str:
    alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits
    password = ""
    for symbol in sample(alphabet, length):
        password += str(symbol)
    return password


print(get_random_password())
