import re
import string

def has_three_vowels(input):
    vowel_count = 0
    if re.search("a", input):
        vowel_count += 1
    if re.search("e", input):
        vowel_count += 1
    if re.search("i", input):
        vowel_count += 1
    if re.search("o", input):
        vowel_count += 1
    if re.search("u", input):
        vowel_count += 1

    if vowel_count >= 3:
        return True
    else:
        return False
    
def has_duplicate_letters2(input):
    for i in range(len(input)):
        for j in range(i + 1, len(input)):
            if input[i] == input[j]:
                return True
    return False

def has_duplicate_letters(input, test_case):
    for i in range(len(test_case)):
        if re.search(test_case[1], input):
            return True
    return False

def no_naughty_strings(input):
    if re.search("ab", input):
        return False
    elif re.search("cd", input):
        return False
    elif re.search("pq", input):
        return False
    elif re.search("xy", input):
        return False
    else:
        return True

alphabet = string.ascii_lowercase
dbl_alpha = []

# Iterate through each letter in the alphabet and double it
for letter in alphabet:
    doubled_letter = letter * 2
    dbl_alpha.append(doubled_letter)

# Print the list of doubled letters
print(dbl_alpha)






# test_string = "dddddddddddd"
# if has_three_vowels(test_string):
#     print("This has at least three vowels.")
# else:
#     print("This does NOT have at least three vowels.")

# # Test cases
# test_string1 = "hello"  # has 'l' twice
# test_string2 = "world"  # No duplicate letters

# result0 = has_duplicate_letters(test_string)
# result1 = has_duplicate_letters(test_string1)
# result2 = has_duplicate_letters(test_string2)

# print(f"Does '{test_string1}' contain two of the same letters? {result1}")
# print(f"Does '{test_string2}' contain two of the same letters? {result2}")
# print(f"Does '{test_string}' contain two of the same letters? {result0}")

# print(no_naughty_strings("haegwjzuvuyypxyu"))
