distances = [
    ('Tristram', 'AlphaCentauri', 34),
    ('Tristram', 'Snowdin', 100),
    ('Tristram', 'Tambi', 63),
    # ... (the rest of your distances)
]

reversed_distances = []

# Reverse the list of distances
for distance in distances:
    source, destination, dist = distance
    reversed_distances.append((destination, source, dist))

# Now, reversed_distances contains the reversed distances

# If you want to merge both original and reversed distances:
all_distances = distances + reversed_distances


for r in range(1, len(places_list) + 1):
    permutation_generator = permutations(places_list, r)
    all_routes.extend(permutation_generator)

    from itertools import permutations

# Your original iterable, for example, a list
original_iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Specify the desired length (e.g., 8)
desired_length = 8

# Generate and filter permutations
for perm in permutations(original_iterable, desired_length):
    # Check if the permutation has the desired length
    if len(perm) == desired_length:
        print(perm)
