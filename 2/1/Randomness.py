import random
random.seed(10) # this ensures we get the same results every time

for_uniform_randoms = [random.random() for _ in range(4)]
# print(for_uniform_randoms)

# Randrange to get random between two values.
random.randrange(10)    # choose randomly from range(10) = [0, 1, ..., 9]
random.randrange(3, 6)  # choose randomly from range(3, 6) = [3, 4, 5]

# random.shuffle to disorder a list
up_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(up_to_ten)
print(up_to_ten) # [7, 2, 6, 8, 9, 4, 10, 1, 3, 5]   (your results will probably be different)

# Select a rondom pick in a list with random.choice
my_best_friend = random.choice(["Alice", "Bob", "Charlie"])     # "Bob" for me
print(my_best_friend)

# Select a sample of random values from a list with random.sample with no replacement
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6) # [16, 36, 10, 6, 25, 9]
print(winning_numbers)

# Select a sample of random values from a list with random.choice with replacement
four_with_replacement = [random.choice(range(10)) for _ in range(4)]
print(four_with_replacement)  # [9, 4, 4, 2]