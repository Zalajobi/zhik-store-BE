from werkzeug.security import generate_password_hash
import string
import random


def generate_random_password(length):
    return generate_password_hash(''.join(random.choice(string.ascii_uppercase) for i in range(length)))
