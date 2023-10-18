def on(start_row, start_column, end_row, end_column):
    i = start_row
    j = start_column
    for i in range(end_row):
        for j in range(end_column):
            grid[i][j] = 1

def off(start_row, start_column, end_row, end_column): 
    i = start_row
    j = start_column
    for i in range(end_row):
        for j in range(end_column):
            grid[i][j] = 0

def toggle(start_row, start_column, end_row, end_column):
    i = start_row
    j = start_column
    for i in range(end_row):
        for j in range(end_column):
            grid[i][j] = 1 - grid[i][j]

r = 1000 # rows
c = 1000 # columns
file_name = "input.txt" # input file

grid = [[0 for _ in range(c)] for _ in range(r)]

for i in range(r):
    for j in range(c):
        grid[i][j] = 0

on(0, 0, 500, 500)

# Testing
for i in range(r):
    for j in range(c):
        print("Position ", i, ",", j, " = ", grid[i][j])

