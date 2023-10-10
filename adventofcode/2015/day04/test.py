import hashlib

def find_lowest_number(secret_key, zeros_count):
    number = 1
    while True:
        data = f"{secret_key}{number}".encode()
        md5_hash = hashlib.md5(data).hexdigest()
        if md5_hash[:zeros_count] == "0" * zeros_count:
            return number
        number += 1

# Puzzle input
secret_key = "abcdef"

# Find the lowest number for a hash with 5 leading zeroes
result_5_zeros = find_lowest_number(secret_key, 5)

print("Lowest number for 5 leading zeroes:", result_5_zeros)