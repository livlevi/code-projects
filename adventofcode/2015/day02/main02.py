# Part 2

file_name = "input.txt"
total = 0

with open (file_name, "r") as file:
    for line in file:
        temp_area = 0
        p = 0
        area = [int(item) for item in line.strip().split("x")]
        area.sort()
        p += (area[0] * 2) + (area[1] * 2)
        p += (area[0] * area[1] * area[2])  
      
        total += p

print(total)


