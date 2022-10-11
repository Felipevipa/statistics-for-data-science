def apply_to_one(f):
    """Calls the function f with 1 as its argument"""
    return(f(1))

#How to create lambda functions
y = apply_to_one(lambda x: x + 4)   # equals 5

print(y)


# Extend a list 
x = [1, 2, 3]
x.extend([4, 5, 6])     # x is now [1, 2, 3, 4, 5, 6]

# Extend a list but in new list
x = [1, 2, 3]
y = x + [4, 5, 6]       # y is [1, 2, 3, 4, 5, 6]; x is unchanged


tweet = {
    "user" : "joelgrus",
    "text" : "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

# Iterate a dictionary
tweet_keys   = tweet.keys()     # iterable for the keys
tweet_values = tweet.values()   # iterable for the values
tweet_items  = tweet.items()    # iterable for the (key, value) tuples


# DefaultDict is useful because when consulting a non existing key it gives a zero function to use
from collections import defaultdict

word_counts = defaultdict(int)  # int() produces 0

dd_list = defaultdict(list)             # list() produces an empty list
dd_list[2].append(1)                    # now dd_list contains {2: [1]}

dd_dict = defaultdict(dict)             # dict() produces an empty dict
dd_dict["Joel"]["City"] = "Seattle"     # {"Joel" : {"City": Seattle"}}

dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1                       # now dd_pair contains {2: [0, 1]}

# Counters. A Counter turns a sequence of values into a defaultdict(int)-like object mapping keys to counts:
from collections import Counter
c = Counter([0, 1, 2, 0]) # c is (basically) {0: 2, 1: 1, 2: 1}

## Most common method for Counter
## print the 10 most common words and their counts
# for word, count in word_counts.most_common(10):
#     print(word, count)


# Defining sets
s = set()
s.add(1)       # s is now {1}
s.add(2)       # s is now {1, 2}
s.add(2)       # s is still {1, 2}
x = len(s)     # equals 2
y = 2 in s     # equals True
z = 3 in s     # equals False

# In-line if else 
parity = "even" if x % 2 == 0 else "odd"

# in for loops control iteration with continue and break
for x in range(10):
    if x == 3:
        continue  # go immediately to the next iteration
    if x == 5:
        break     # quit the loop entirely
    print(x)

# Check if a variable is None
x = None
assert x == None, "this is the not the Pythonic way to check for None"
assert x is None, "this is the Pythonic way to check for None"

# Check Boolean clauses with all and any
all([True, 1, {3}])   # True, all are truthy
all([True, 1, {}])    # False, {} is falsy
any([True, 1, {}])    # True, True is truthy
all([])               # True, no falsy elements in the list
any([])               # False, no truthy elements in the list

# Sorted
x = sorted([-4, 1, -2, 3], key=abs, reverse=True)  # is [-4, 3, -2, 1]

wc = sorted(word_counts.items(),
            key=lambda word_and_count: word_and_count[1],
            reverse=True)

# List Comprehensions
even_numbers = [x for x in range(5) if x % 2 == 0]  # [0, 2, 4]
squares      = [x * x for x in range(5)]            # [0, 1, 4, 9, 16]
even_squares = [x * x for x in even_numbers]        # [0, 4, 16]

square_dict = {x: x * x for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
square_set  = {x * x for x in [1, -1]}      # {1}

## If you don’t need the value from the list, it’s common to use an underscore as the variable
zeros = [0 for _ in even_numbers]      # has the same length as even_numbers


## A list comprehension can include multiple fors:
pairs = [(x, y)
         for x in range(10)
         for y in range(10)]   # 100 pairs (0,0) (0,1) ... (9,8), (9,9)


# Automated testing and assert
assert 1 + 1 == 2
assert 1 + 1 == 2, "1 + 1 should equal 2 but didn't"

def smallest_item(xs):
    return min(xs)

assert smallest_item([10,20,5,40]) == 5
assert smallest_item([1,0,-1,2]) == -1, "Should be -1"





