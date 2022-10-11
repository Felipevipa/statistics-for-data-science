# To define a class, you use the class keyword and a PascalCase name:
from pydoc import cli


class CountingClicker:
    """A class can/should have a docstring, just like a function"""

    # A class has a constructor named __init__
    def __init__(self, count = 0):
        self.count = count

    # Another such method is __repr__, which produces the string representation of a class instance:
    def __repr__(self):
        return f"CountingClicker(count={self.count})"

    # And finally we need to implement the public API of our class:
    def click(self, num_times = 1):
        """Click the clicker some number of times."""
        self.count += num_times
    
    def read(self):
        return self.count

    def reset(self):
        self.count = 0

clicker1 = CountingClicker()           # initialized to 0
clicker2 = CountingClicker(100)        # starts with count=100
clicker3 = CountingClicker(count=100)  # more explicit way of doing the same


# Notice that the __init__ method name starts and ends
#  with double underscores. These “magic” methods are sometimes called 
# “dunder” methods (double-UNDERscore, get it?) and represent “special” 
# behaviors.

# Having defined it, let’s use assert to write some test cases for our clicker
clicker = CountingClicker()
assert clicker.read() == 0, "clicker should start with count 0"
clicker.click()
clicker.click()
assert clicker.read() == 2, "after two clicks, clicker shoud have count 2"
clicker.reset()
assert clicker.read() == 0, "after reset, clicker should be back to 0"


class NoResetClicker(CountingClicker):
    # This class has all the samen methods as CountingClicker

    # Except that it has a reset method that does nothing.
    def reset(self):
        pass

clicker2 = NoResetClicker()
assert clicker2.read() == 0
clicker2.click()
assert clicker2.read() == 1
clicker2.reset()
assert clicker2.read() == 1, "reset shouldn't do anything"