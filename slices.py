# Unlike arrays, lists are typed only by the elements they contain (not the number of elements).
# To create an empty list with non-zero length, you can simply use `[]` or the `list()` constructor.
# Here we make a list of strings with length `3` (initially empty).
s = [""] * 3
print("emp:", s)

# We can set and get just like with arrays.
s[0] = "a"
s[1] = "b"
s[2] = "c"
print("set:", s)
print("get:", s[2])

# `len` returns the length of the slice as expected.
print("len:", len(s))

# In addition to these basic operations, lists support several more that make them richer than arrays.
# One is the `append` method, which adds one or more new values to the list.
s.append("d")
s.extend(["e", "f"])
print("apd:", s)

# Lists can also be copied using the `copy` method or by slicing.
c = s.copy()
print("cpy:", c)

# Lists support a "slice" operator with the syntax `list[low:high]`.
# For example, this gets a slice of the elements `s[2]`, `s[3]`, and `s[4]`.
l = s[2:5]
print("sl1:", l)

# This slices up to (but excluding) `s[5]`.
l = s[:5]
print("sl2:", l)

# And this slices up from (and including) `s[2]`.
l = s[2:]
print("sl3:", l)

# We can declare and initialize a variable for a list in a single line as well.
t = ["g", "h", "i"]
print("dcl:", t)

# Lists can be composed into multi-dimensional data structures.
# Unlike with multi-dimensional arrays, the length of the inner lists can vary.
twoD = []
for i in range(3):
    inner_len = i + 1
    inner_list = [i + j for j in range(inner_len)]
    twoD.append(inner_list)
print("2d:", twoD)

