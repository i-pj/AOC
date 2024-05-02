#https://docs.python.org/3/library/hashlib.html

import hashlib
secret_key = "bgvyzdsv"

def mine_adventcoins(key):
    i = 1
    while True:
        input_str = f"{key}{i}"
        md5_hash = hashlib.md5(input_str.encode()).hexdigest()
        if md5_hash.startswith("00000"):
            return i
        i += 1

print(mine_adventcoins(secret_key))

mine_adventcoins(secret_key)

# Part 2

def mine_adventcoins(key):
    i = 1
    while True:
        input_str = f"{key}{i}"
        md5_hash = hashlib.md5(input_str.encode()).hexdigest()
        if md5_hash.startswith("000000"):
            return i
        i += 1

print(mine_adventcoins(secret_key))

mine_adventcoins(secret_key)
