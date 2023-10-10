# Advent of Code Challenge
# Day 4

# Two sets of numbers are given on each line in a file. Process the line 

import os

def clear_screen():
    os.system('cls')

clear_screen()
file_name = "input.txt"
overlap = 0

print("############################################################")
print("############################################################")
print("############################################################")

with open (file_name, "r") as file:
    for line in file:
        ranges = line.strip().split(",")
        first_range = ranges[0]
        second_range = ranges[1]
        first_range_split = first_range.split("-")
        second_range_split = second_range.split("-")

        if (int(first_range_split[0]) >= int(second_range_split[0])) and (int(first_range_split[1]) <= int(second_range_split[1])):
            overlap += 1
        elif (int(second_range_split[0]) >= int(first_range_split[0])) and (int(second_range_split[1]) <= int(first_range_split[1])):
            overlap +=1

print("The number of overlaps: ", overlap)
