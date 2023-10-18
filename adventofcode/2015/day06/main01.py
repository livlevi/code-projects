# Advent of Code Day 6
# Part 1

# Functions:
# Turn on Lights, Turn off Lights, Toggle lights
def on(start_r, start_c, end_r, end_c):
    for i in range(start_r, end_r + 1):
        for j in range(start_c, end_c + 1):
            grid[i][j] = 1

def off(start_r, start_c, end_r, end_c):
    for i in range(start_r, end_r + 1):
        for j in range(start_c, end_c + 1):
            grid[i][j] = 0

def toggle(start_r, start_c, end_r, end_c):
    for i in range(start_r, end_r + 1):
        for j in range(start_c, end_c + 1):
            grid[i][j] = 1 - grid[i][j]

# Variables
file_name = "input.txt"
rows = 1000
columns = 1000
on_count = 0
grid = [[0 for _ in range(columns)] for _ in range(rows)]

# Fill grid with values (or turn off the lights)
for i in range(rows):
    for j in range(columns):
        grid[i][j] = 0

with open (file_name, "r") as file:
    for line in file:
        proc = line.strip().split(" ")
        # Check input, turn on?
        if proc[1] == "on":
            coord01 = proc[2]
            coord02 = proc[4]
            start_rc = coord01.split(",")
            end_rc = coord02.split(",")
            on(int(start_rc[0]), int(start_rc[1]), int(end_rc[0]), int(end_rc[1]))
        # Check input, turn off?
        if proc[1] == "off":
            coord01 = proc[2]
            coord02 = proc[4]
            start_rc = coord01.split(",")
            end_rc = coord02.split(",")
            off(int(start_rc[0]), int(start_rc[1]), int(end_rc[0]), int(end_rc[1]))
        # Check input, toggle?
        if proc[0] == "toggle":
            coord01 = proc[1]
            coord02 = proc[3]
            start_rc = coord01.split(",")
            end_rc = coord02.split(",")
            toggle(int(start_rc[0]), int(start_rc[1]), int(end_rc[0]), int(end_rc[1]))

# Count each light that's been turned on.
for i in range(rows):
    for j in range(columns):
        if grid[i][j] == 1:
            on_count += 1

print(on_count)


