# Create a set of numbers
number_set = {1, 2, 3, 4, 5}
print("Initial Set:", number_set)

# Attempt to add a duplicate number to the set
size_before = len(number_set)
number_set.add(3)
print("Set after adding duplicate:", number_set)
assert len(number_set) == size_before
print("Length unchanged:", len(number_set))

# Set operations
other = {4, 5, 6, 7}
print("Union:", number_set | other)
print("Intersection:", number_set & other)
print("Difference:", number_set - other)

# Sets need hashable items
try:
    bad = {[1, 2], 3}
except TypeError as e:
    print("Error:", e)

print("Tuple in set:", {(1, 2), 3})
