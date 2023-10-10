file_name = "input.txt"
priorities = 0

def return_priority(letter): #Determine priority based on ASCII num
    if (ord(letter) - 64) >= 1 and (ord(letter) - 64) <= 26:
        priority = ord(letter) - 38    # integer used to align w/assignment score
        return priority
    elif (ord(letter) - 70) >= 27 and (ord(letter) - 70) <= 52:
        priority = ord(letter) - 96    # integer used to align w/assignment score
        return priority
    
def has_duplicates(list0, list1, list2):
    
    #Iterate though list and check if any item is in set2
    for item in list0:
        if item in list1:
            if item in list2:
            # print(item)
                return item
    #No error handling necessary as input is set

with open (file_name, "r") as file:
    rucksacks = []
    

    for line in file:
        
        presents0, presents1, presents2 = [], [], []

        rucksacks.append(line.strip())
        # print(rucksacks)
        # print(len(rucksacks))
        if len(rucksacks) == 3:
            for char in rucksacks[0]:
                presents0.append(char)
            for char in rucksacks[1]:
                presents1.append(char)
            for char in rucksacks[2]:
                presents2.append(char)
            common_item = has_duplicates(presents0, presents1, presents2)
            print("This is the common item " + common_item)
            priorities += return_priority(common_item)
            rucksacks = []

        
print(" ")
print("These are the priorities: ")
print(priorities)