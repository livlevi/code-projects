# define an empty list to store the file contents
calorie_list = []
elf_total = 0

#specify the file name
file_name = "input.txt"

print("###################################################################")
print("###################################################################")
print("###################################################################")
#open the file for reading
with open(file_name, "r") as file:
    #read each line fromt he file and add it to the list
    for line in file:
        #remove leading and trailing whitespace (including newline characters)

        cleaned_line = line.strip()

        # check if the line is not blank (contains content)
        if cleaned_line:
            elf_total += int(cleaned_line)
        else:
            # add the elf's total to the list
            calorie_list.append(elf_total)
            elf_total = 0

#print(calorie_list)

calorie_list.sort(reverse=True)

#Most calories

#print(calorie_list)
print("Elf with most calories: ", calorie_list[0])

print("###################################################################")
print("###################################################################")
print("###################################################################")