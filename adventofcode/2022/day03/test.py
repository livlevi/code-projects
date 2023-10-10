upper_case = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Z"]
lower_case = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for letter in upper_case:
    print(letter + " = ", ord(letter), " game score =", ord(letter) - 38)

for letter in lower_case:
    print(letter + " = ", ord(letter), " game score =", ord(letter) - 96)

#quick calculation to use the ord function to calculate the scores.

# find duplicate test

def has_duplicates(list1, list2):
    # Convert list2 to a set for faster membership testing
    set2 = set(list2)

    # Iterate through list1 and check if any item is in set2 (contains duplicates)
    for item in list1:
        if item in set2:
            return True  # list1 contains duplicates from list2

    return False  # No duplicates found

# Sample lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

if has_duplicates(list1, list2):
    print("list1 contains duplicates from list2.")
else:
    print("list1 does not contain duplicates from list2.")
