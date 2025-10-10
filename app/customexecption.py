# Custom Exception Example
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("You must be 18 or older.")
    print("Access granted!")

try:
    check_age(15)
except InvalidAgeError as e:
    print(e)
