# Task 1: Create a dictionary for a user profile
user_profile = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Display the dictionary
print(user_profile)

# Task 2 - Step 1: Access the name
print("User's Name:", user_profile["name"])

# Step 2: Update the age
user_profile["age"] = 31

# Step 3: Display updated profile
print("Updated User Profile:", user_profile)

# Step 4: Safe access using get()
print("Email:", user_profile.get("email", "not set"))

# Step 5: Handle a missing key using KeyError
try:
    user_profile["email"]
except KeyError as e:
    print("KeyError for missing key:", e)

# Task 3 - Step 1: Remove city using pop()
removed = user_profile.pop("city")
print("Removed value:", removed)

# Step 2: Display profile after removal
print("Profile after removing city:", user_profile)

# Step 3: Verify city key is removed
assert 'city' not in user_profile
print("Verified: 'city' is not in user_profile")

# Task 4 - Step 1: Iterate over dictionary items
for key, value in user_profile.items():
    print(f"{key}: {value}")

# Step 2: Iterate over dictionary keys
for key in user_profile.keys():
    print(f"Key: {key}")
