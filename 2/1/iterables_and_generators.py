# Often all we need is to iterate over the collection using for and in. 
# In this case we can create generators, which can be iterated over just 
# like lists but generate their values lazily on demand.

# One way to create generators is with functions and the yield operator:

def generate_range(n):
    i = 0
    while i < n:
        yield i # every call to yield produces a value of the generator
        i += 1

for i in generate_range(10):
    print(f"i: {i}")

# (In fact, range is itself lazy, so there’s no point in doing this.)


# def natural_numbers():
#     """returns 1, 2, 3, ..."""
#     n = 1
#     while True:
#         yield n
#         n += 1


# By generator comprehension
evens_below_20 = (i for i in generate_range(20) if i % 2 == 0)


names = ["Felipe", "Luisa"]
# Pythonic
for i, name in enumerate(names):
    print(f"name {i} is {name}")