# Creating a tuple representing coordinates (x, y, z)
coordinates = (10, 20, 30)
print("Coordinates Tuple:", coordinates)

# Tuple unpacking
x, y, z = coordinates
print("Unpacked:", x, y, z)

# Attempt to change the x-coordinate
try:
    coordinates[0] = 100
except TypeError as e:
    print("Error:", e)

# A tuple can be a dictionary key
locations = {coordinates: "origin marker"}
print("Dict with tuple key:", locations)
