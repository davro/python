# Here's a basic example.
if 7 % 2 == 0:
    print("7 is even")
else:
    print("7 is odd")

# You can have an `if` statement without an else.
if 8 % 4 == 0:
    print("8 is divisible by 4")

# A statement can precede conditionals; any variables
# declared in this statement are available in all
# branches.
num = 9
if num < 0:
    print(num, "is negative")
elif num < 10:
    print(num, "has 1 digit")
else:
    print(num, "has multiple digits")

