from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa

public = ""

def who():
    global public
    return public

def validate(key, change):
    global public
    if public == "":
        public = change
        #print(public)
        return 0
    if public == key:
        public = change
        #print(public)
        return 1
    return 0