# Advent of Code Day 3
# Part 2

file_name = "input.txt"

santa_x = 0
santa_y = 0
robot_x = 0
robot_y = 0

moving = True

location = {(0,0)}

with open (file_name, "r") as file:
    for char in file.read():
        if moving:
            if char == "^":
                santa_y +=1
            elif char == "v":
                santa_y -=1
            elif char == "<":
                santa_x -= 1
            elif char == ">":
                santa_x += 1
            location.add((santa_x, santa_y))
        else: 
            if char == "^":
                robot_y +=1
            elif char == "v":
                robot_y -=1
            elif char == "<":
                robot_x -= 1
            elif char == ">":
                robot_x += 1
            location.add((robot_x, robot_y))
        moving = not moving
print(location)
print(len(location))
