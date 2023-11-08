from itertools import permutations

guests = ['Alice', 'Bob', 'Carol', 'David', 'Eric', 'Frank', 'George', 'Mallory', 'Me']
seating = []
factor = []
happiness = 0
file_name = "c:\\codebase\\python\\adventofcode\\2015\\day13\\input.txt"

def findHappiness(guest, adj):
    for k in factor:
        if guest == 'Me' or adj == 'Me':
            return 0
        if guest == k[0] and adj == k[2]:
            return k[1]

for r in range(1, len(guests) + 1):
    if r == 9:
        perm_gen = permutations(guests, r)
        seating.extend(perm_gen)

with open (file_name, "r") as file:
    for line in file:
        g, gl, n, a = line.strip().split(" ")
        if gl == "lose":
            f = -1 * int(n)
        else:
            f = int(n)
        hold = [g, f, a]
        factor.append(hold)

for item in seating:
    h1 = 0
    for i in range(len(item) - 1):
        h1 += findHappiness(item[i], item[i+1])
        h1 += findHappiness(item[i+1], item[i])
    h1 += findHappiness(item[7], item[0])
    h1 += findHappiness(item[0], item[7])
    if h1 > happiness:
        happiness = h1

print(happiness)
print(seating[-1])

# create permutations: all possible seating arrangements for guests
# find the highest sum (happiness)
# iterate through list forward and backward