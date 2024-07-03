import string
import random

def generate_password(length):
    char = string.ascii_letters + string.digits + string.punctuation

    password = "".join(random.choice(char) for i in range(length))

    return password

length = int(input("Password length : "))
print(f"password : {generate_password(length)}")