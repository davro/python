# The function signature `(int, int)` indicates that the function returns 2 `int`s.
def vals():
    return 3, 7

# Here we use the 2 different return values from the call with _multiple assignment_.
a, b = vals()
print(a)
print(b)

# If you only want a subset of the returned values, use the blank identifier `_`.
_, c = vals()
print(c)

