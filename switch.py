import datetime

# Here's a basic `switch`.
i = 2
print("write", i, "as ", end="")
if i == 1:
    print("one")
elif i == 2:
    print("two")
elif i == 3:
    print("three")

# You can use commas to separate multiple expressions
# in the same `case` statement. We use the optional
# `default` case in this example as well.
today = datetime.datetime.now().weekday()
if today in (5, 6):
    print("it's the weekend")
else:
    print("it's a weekday")

# `switch` without an expression is an alternate way
# to express if/else logic. Here we also show how the
# `case` expressions can be non-constants.
t = datetime.datetime.now()
if t.hour < 12:
    print("it's before noon")
else:
    print("it's after noon")

