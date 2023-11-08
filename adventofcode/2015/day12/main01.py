import json

python_object = {}
file_name = "input.txt"
count = 0

with open('input.json', 'r') as json_file:
    python_object = json.load(json_file)

with open(file_name, 'r') as file:
    for line in file:
        list_obj = line.strip().split(",")

# print(list_obj)
# print(len(list_obj))
for item in list_obj:
    if item.isdigit():
        count += int(item)
    elif item[0] == "-":
        count += int(item)

print("Sum: ", count)
# print(type(python_object))
# print(python_object)

# for i in python_object:
#     for item in i:
#         print(" ")
#         print(" ")
#         print("88888888888888888888888888888888888888888888888888888888888")
#         print("This it the start of an item.")
#         print(item)

# print(python_object[1])
# for item in python_object[1]:
#     print(item)

# print(print(json.dumps(python_object, indent=4, sort_keys=True)))