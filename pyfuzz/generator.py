import random
import os

def generateRandomBytes():
    length = random.randint(0, 4080)
    return os.urandom(length)
