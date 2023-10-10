# Advent of Code Day 4
# Part 1

import hashlib

def find_num(key, zeroes):
    num = 1
    while True:
        data = f"{key}{num}".encode()
        md5_hash = hashlib.md5(data).hexdigest()
        if md5_hash[:zeroes] == "00000":
            return num
        num += 1

key = "yzbqklnj"

result = find_num(key, 5)

print("Lowest num: ", result)