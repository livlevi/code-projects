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
        fs = int(first_range_split[0])
        fe = int(first_range_split[1])
        ss = int(second_range_split[0])
        se = int(second_range_split[1])

        if (se >= fs >= ss) or (fe >= ss >= fs):
            overlap +=1 

print("The number of overlaps: ", overlap)