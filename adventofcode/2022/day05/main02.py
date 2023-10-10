# Advent of Code, Day 5 Part 2
# Link: https://adventofcode.com/2022/day/5#part2



file_name = "input.txt"
move = 0
start_crate = 0
end_crate = 0

stack01 = ['[H]', '[R]', '[B]', '[D]', '[Z]', '[F]', '[L]', '[S]']
stack02 = ['[T]', '[B]', '[M]', '[Z]', '[R]']
stack03 = ['[Z]', '[L]', '[C]', '[H]', '[N]', '[S]']
stack04 = ['[S]', '[C]', '[F]', '[J]']
stack05 = ['[P]', '[G]', '[H]', '[W]', '[R]', '[Z]', '[B]']
stack06 = ['[V]', '[J]', '[Z]', '[G]', '[D]', '[N]', '[M]', '[T]']
stack07 = ['[G]', '[L]', '[N]', '[W]', '[F]', '[S]', '[P]', '[Q]']
stack08 = ['[M]', '[Z]', '[R]']
stack09 = ['[M]', '[C]', '[L]', '[G]', '[V]', '[R]', '[T]']

# stack01 = ['[Z]', '[N]']
# stack02 = ['[M]', '[C]', '[D]']
# stack03 = ['[P]']

def find_crate(crate_number):
    if crate_number == 1:
        return stack01
    elif crate_number == 2:
        return stack02
    elif crate_number == 3:
        return stack03
    elif crate_number == 4:
        return stack04
    elif crate_number == 5:
        return stack05
    elif crate_number == 6:
        return stack06
    elif crate_number == 7:
        return stack07
    elif crate_number == 8:
        return stack08
    elif crate_number == 9:
        return stack09
    else:
        return None


with open (file_name, "r") as file:
    for line in file:
        lines = line.strip().split(" ")
        move = int(lines[1])
        start_crate = int(lines[3])
        end_crate = int(lines[5])

        in_transit = find_crate(start_crate)[-move:]
        find_crate(end_crate).extend(in_transit)
        while move > 0:
            garbage = find_crate(start_crate).pop()
            move -= 1

temp_stack01 = stack01[-1]
sliced_stack01 = temp_stack01[1]
temp_stack02 = stack02[-1]
sliced_stack02 = temp_stack02[1]
temp_stack03 = stack03[-1]
sliced_stack03 = temp_stack03[1]
temp_stack04 = stack04[-1]
sliced_stack04 = temp_stack04[1]
temp_stack05 = stack05[-1]
sliced_stack05 = temp_stack05[1]
temp_stack06 = stack06[-1]
sliced_stack06 = temp_stack06[1]
temp_stack07 = stack07[-1]
sliced_stack07 = temp_stack07[1]
temp_stack08 = stack08[-1]
sliced_stack08 = temp_stack08[1]
temp_stack09 = stack09[-1]
sliced_stack09 = temp_stack09[1]

print(sliced_stack01 + sliced_stack02 + sliced_stack03 + sliced_stack04 + sliced_stack05 + sliced_stack06 + sliced_stack07 + sliced_stack08 + sliced_stack09)
# print(stack01)
# print(stack02)
# print(stack03)
# print(sliced_stack01 + sliced_stack02 + sliced_stack03)