# arithmetic_operations.py
import sys

number1 = int(sys.argv[1]) if len(sys.argv) > 1 else 17
number2 = int(sys.argv[2]) if len(sys.argv) > 2 else 5

print(f"Addition: {number1} + {number2} = {number1 + number2}")
print(f"Subtraction: {number1} - {number2} = {number1 - number2}")
print(f"Multiplication: {number1} * {number2} = {number1 * number2}")

try:
    print(f"Division: {number1} / {number2} = {number1 / number2}")
    print(f"Integer Division: {number1} // {number2} = {number1 // number2}")
    print(f"Modulus: {number1} % {number2} = {number1 % number2}")
    print(f"divmod({number1}, {number2}) = {divmod(number1, number2)}")
except ZeroDivisionError:
    print("Cannot divide by zero: division, //, % and divmod are undefined.")

print(f"Exponent: {number1} ** {number2} = {number1 ** number2}")
