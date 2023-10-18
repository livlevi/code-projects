# Advent of Code Day 7
# Part 1

def bin_str(char):
    binary_char = format(ord(char), 'b')
    return binary_char

table = {}
file_name = "input.txt"

with open (file_name, "r") as file:
    for line in file:
        if "AND" in line:
            hold = line.strip().split(" ")
            bin1 = bin_str(hold[0])
            print("This is bin1: " + bin1)
            print(type(bin1))
            # table[hold[-1]] = bin_str(hold[0]) & bin_str(hold[4])
        elif "OR" in line:
            hold = line.strip().split(" ")
            table[hold[-1]] = bin_str(hold[0]) | bin_str(hold[4])
        elif "LSHIFT" in line:
            hold = line.strip().split(" ")
            table[hold[-1]] = bin_str(hold[0]) << bin_str(hold[2])
        elif "RSHIFT" in line:
            hold = line.strip().split(" ")
            table[hold[-1]] = bin_str(hold[0]) >> bin_str(hold[2])
        elif "NOT" in line:
            hold = line.strip().split(" ")
            table[hold[-1]] = ~ bin_str(hold[1])
        else:
            hold = line.strip().split(" ")
            table[hold[-1]] = hold[0]

print(table)

# 123 -> x
# 456 -> y
# x AND y -> d
# x OR y -> e
# x LSHIFT 2 -> f
# y RSHIFT 2 -> g
# NOT x -> h
# NOT y -> i