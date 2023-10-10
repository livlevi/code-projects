# Part 1

file_name = "input.txt"
total = 0

with open (file_name, "r") as file:
    for line in file:
        temp_area = 0
        area = [int(item) for item in line.strip().split("x")]
        area.sort()        
        temp_area += (2 * (area[0] * area[1]))        
        temp_area += (2 * (area[1] * area[2]))        
        temp_area += (2 * (area[0] * area[2]))        
        temp_area += (area[0] * area[1])
        total += temp_area

print(total)


