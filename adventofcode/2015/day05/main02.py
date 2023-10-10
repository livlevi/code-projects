# Advent of Code 2015 Day 5
# Part 2

import re

def has_twoletters_twice(input):
    for i in range(len(input) - 3):
        sub01 = input[i]  + input[i + 1]
        j = i
        while j <= (len(input) - 4):
            sub02 = input[j + 2] + input[j + 3]
            # print("comparing sub 01: " + sub01 + " to sub 02: " + sub02)
            if sub01 == sub02:
                return True
            # print("This is j: ", j )
            j += 1
    return False

def has_splitletter(input):
    for i in range(len(input) - 2):
        if input[i] == input[i + 2]:
            return True
    return False

file_name = "input.txt"
nice_count = 0

with open (file_name, "r") as file:
    for line in file:
        lines = line.strip()
        if (has_splitletter(lines)) and (has_twoletters_twice(lines)):
            nice_count += 1

print(nice_count)
# st = "bcaabcdefgaa"
# tt = "abcdefeghi"

# print(has_twoletters_twice(st))
# print(has_splitletter(tt))