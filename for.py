# The most basic type, with a single condition.
i = 1
while i <= 3:
    print(i)
    i = i + 1

# A classic initial/condition/after `for` loop.
for j in range(7, 10):
    print(j)

# `for` without a condition will loop repeatedly
# until you `break` out of the loop or `return` from
# the enclosing function.
while True:
    print("loop")
    break

