import random
import os

def generateRandomBytes():
    length = random.randint(0, 400)
    return os.urandom(length)
