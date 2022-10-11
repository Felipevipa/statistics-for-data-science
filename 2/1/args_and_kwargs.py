# Let’s say we want to create a higher-order function that takes as input 
# some function f and returns a new function that for any input returns 
# twice the value of f:

def doubler(f):
    # Here we define a new function that keeps a reference to f
    def g(x):
        return 2 * f(x)

    # And return that new function
    return g

def f1(x):
    return x + 1

g = doubler(f1)
assert g(3) == 8,  "(3 + 1) * 2 should equal 8"
assert g(-1) == 0, "(-1 + 1) * 2 should equal 0"


def f2(x, y):
    return x + y

g = doubler(f2)
try:
    g(1, 2)
except TypeError:
    print("as defined, g only takes one argument")


def magic(*args, **kwargs):
    print("unnamed args:", args)
    print("keyword args:", kwargs)


magic(1, 2, key="word", key2="word2") 
## prints
#  unnamed args: (1, 2)
#  keyword args: {'key': 'word', 'key2': 'word2'}

def other_way_magic(x, y, z):
    return x + y + z

x_y_list = [1, 2]
z_dict = {"z": 3}
assert other_way_magic(*x_y_list, **z_dict) == 6, "1 + 2 + 3 should be 6"


def doubler_correct(f):
    """Work no matter what kind of inputs f expects"""
    def g(*args, **kwargs):
        """Whatever argument g is supplied, pass them through to f"""
        return 2 * f(*args, **kwargs)
    
    return g

g = doubler_correct(f2)
assert g(1, 2) == 6, "soubler should work now"