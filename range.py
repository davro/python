# Here we use `range` to sum the numbers in a list.
# Lists work like this too.
nums = [2, 3, 4]
sum = 0
for num in nums:
    sum += num
print("sum:", sum)

# `range` on lists and tuples provides the index and value for each entry.
# In Python, you can use `enumerate` to achieve this.
for i, num in enumerate(nums):
    if num == 3:
        print("index:", i)

# `items()` method on dictionaries provides key/value pairs.
kvs = {"a": "apple", "b": "banana"}
for k, v in kvs.items():
    print(f"{k} -> {v}")

# Iterating over a string directly will give Unicode code points.
# To achieve the starting byte index and the character itself, you can use `enumerate`.
for i, c in enumerate("go"):
    print(i, c)

