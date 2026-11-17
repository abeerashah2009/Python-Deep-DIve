import sys

# Use the command-line argument if given, otherwise prompt the user
if len(sys.argv) > 1:
    text = sys.argv[1]
else:
    text = input("Enter a number: ")

try:
    number = float(text)
except ValueError:
    print("Invalid number")
    sys.exit(1)

# Check if the number is positive, negative, or zero
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
