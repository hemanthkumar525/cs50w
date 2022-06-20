import sys

try:
    x = int(input("enter a number:  "))
    y = int(input("enter a number: "))
except ValueError:
    print("Error: invalid choice")
    sys.exit(1)
try:
    result = x/y
except ZeroDivisionError:
    print("Error: cannot divide with zero.")
    sys.exit(1)

print(f"{x} / {y} = {result}")