file_name = "input.txt"
priorities = 0

def return_priority(letter): #Determine priority based on ASCII num
    if (ord(letter) - 64) >= 1 and (ord(letter) - 64) <= 26:
        priority = ord(letter) - 38    # integer used to align w/assignment score
        return priority
    elif (ord(letter) - 70) >= 27 and (ord(letter) - 70) <= 52:
        priority = ord(letter) - 96    # integer used to align w/assignment score
        return priority
    
def has_duplicates(list1, list2):
    
    #Iterate though list and check if any item is in set2
    for item in list1:
        if item in list2:
            # print(item)
            return item
    #No error handling necessary as input is set

with open (file_name, "r") as file:
    for line in file:
        length = len(line.strip())
        i = 0
        compartment1 = []
        compartment2 = []
        while i <= ((length/2) - 1): #Assign first half of line to compartment 1
            compartment1.append(line[i])
            i += 1 
        while i <= (length - 1): #Assign second half of line to compartment 2
            compartment2.append(line[i])
            i += 1
        
        common_item = has_duplicates(compartment1, compartment2)
        priorities += return_priority(common_item)

print(priorities)