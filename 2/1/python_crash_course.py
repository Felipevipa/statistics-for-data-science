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
for word, count in word_counts.most_common(10):
    print(word, count)
