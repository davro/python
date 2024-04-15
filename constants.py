import math

# Constants can be defined directly without a specific keyword.
# Python supports character, string, boolean, and numeric values as constants.
s = "constant"
print(s)

# A constant expression performs arithmetic with arbitrary precision.
n = 500000000
d = 3e20 / n
print(d)

# A numeric constant has no type until it's given one, such as by an explicit cast.
print(int(d))

# Constants can be used in contexts that require a specific type.
# For example, `math.sin` expects a `float`.
print(math.sin(n))

