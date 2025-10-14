# Custom exception handling
class InvalidPasswordError(Exception):
    pass

def login(password):
    if len(password) < 6:
        raise InvalidPasswordError("Password too short!")
    print("Login successful ✅")

try:
    login("123")
except InvalidPasswordError as e:
    print("❌", e)
