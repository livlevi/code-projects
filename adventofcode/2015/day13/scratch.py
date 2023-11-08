my_list = [1, 2, 3, 4, 5]

# Get the length of the list
list_length = len(my_list)

# Use range() to create a range that starts from the last index and goes backward
for i in range(list_length - 2, -1, -1):
    print("i = ", i, "my list: ", my_list[i])
