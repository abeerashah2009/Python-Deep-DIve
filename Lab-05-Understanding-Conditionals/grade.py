import sys

if len(sys.argv) > 1:
    text = sys.argv[1]
else:
    text = input("Enter your score: ")

try:
    score = int(text)
except ValueError:
    print("Invalid score")
    sys.exit(1)

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
