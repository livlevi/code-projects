# Advent of Code 2015 Day 5
# Part 1

import re
import string

def has_three_vowels(input):
    vowel_count = 0
    for c in input:
        if c in 'aeiou':
            vowel_count += 1
    if vowel_count >= 3:
        return True
    else:
        return False
    
def has_duplicate_letters(input):
    for i in range(len(input) - 1):
        if input[i] == input[i + 1]:
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
    
file_name = "input.txt"
nice_count = 0


with open (file_name, "r") as file:
    for line in file:
        s_string = line.strip()
        if has_three_vowels(s_string) and has_duplicate_letters(s_string) and no_naughty_strings(s_string):
            nice_count += 1

print(nice_count)
