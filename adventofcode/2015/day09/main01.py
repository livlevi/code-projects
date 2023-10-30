from itertools import permutations

distances = []
reversed = []
file_name = "input.txt"
routes = []
all_routes = []
places = set()
short_dist = float('inf')  # Initialize with positive infinity
long_dist = 0

# Read from file, create set of all locations and add location to list
with open (file_name, "r") as file:
    for line in file:
        route, distance = line.strip().split(" = ")
        start, dest = route.split(" to ")
        distances.append((start, dest, distance))
        places.add(start)
        places.add(dest)

# Reverse original list and reversed locations
for item in distances:
    so, de, di = item
    reversed.append((de, so, di))

all_distances = distances + reversed

places_list = list(places)

for r in range(1, len(places_list) + 1):
    if r == 8:
        perm_gen = permutations(places_list, r)
        all_routes.extend(perm_gen)

for route in all_routes:
    t = 0  # Initialize the total distance for this route
    for i in range(len(route) - 1):
        for city in all_distances:
            so, de, di = city
            if (route[i] == so) and (route[i + 1] == de):
                t += int(di)
    if t > long_dist:
        long_dist = t
    if t < short_dist:
        short_dist = t

print("Shortest distance:", short_dist)
print("Longest distance: ", long_dist)