fl = 0
file_name = "input.txt"
position = ""

with open (file_name, "r") as file:
    for line in file:
        for char in line:
            if char == "(" and fl != -1:
                fl += 1
            elif char == ")" and fl != -1:
                fl -= 1

print(fl)