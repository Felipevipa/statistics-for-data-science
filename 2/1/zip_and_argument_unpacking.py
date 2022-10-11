list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

# zip is lazy, so you have to do something like the following
[pair for pair in zip(list1, list2)]    # is [('a', 1), ('b', 2), ('c', 3)]

# It's possible to "unzip"
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)
# The asterisk (*) performs argument unpacking

# The same result could be achieved:
letters, numbers = zip(('a', 1), ('b', 2), ('c', 3))

# argument unpacking could be used with any function or list
def add(a, b): return a + b

add(1, 2)      # returns 3
try:
    add([1, 2])
except TypeError:
    print("add expects two inputs")
add(*[1, 2])   # returns 3