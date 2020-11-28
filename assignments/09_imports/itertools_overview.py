# Homework Assignment #10 - Imports
import itertools
import operator

steps = 5

# Here I explain some of the functions provided in the library "itertools"

# ---------------
# Helper Function
# ---------------


def printIterator(iterator, name=""):
    # This method prints out the first (steps) elements hold by an iterator object.
    # If the iterator contains less elements then it prints "None"
    print(name.upper() + ":")
    for _ in range(steps):
        print(next(iterator, None))


# INFINITE ITERATORS
# ==================

# -- COUNT --
# With the "count" method you can create a custom counter object
# You can set the starting number and the increment
# With the "__next__" method of the counter object you can retrieve the next equidistant number
counter = itertools.count(50, 10)

printIterator(counter, "Count")


# -- CYCLE --
# The "cycle" method loops through the given list and returns an iterable object like the "count" method
# With the "__next__" method of the counter object you can retrieve the next list element
cycler = itertools.cycle(["Hello", "World", "!"])

printIterator(cycler, "Cycle")


# -- REPEAT --
# The "repeat" method returns an iterable object over only one element
# This means that the "__next__" method will always return the same object
# If you specify a count. The "__next__" method only serves the object the given number of times
repeater = itertools.repeat("Repeat this", steps)

printIterator(repeater, "Repeat")

# A common use for repeat is to supply a stream of constant values to map or zip.
print(list(map(pow, range(10), itertools.repeat(2))))


# TERMINATING ITERATORS
# =====================

# -- ACCUMULATE --
# This method returns an iterator that returns accumulated sums, or accumulated results of other binary functions
inputList = [1, 2, 3, 4, 5]
accumulator = itertools.accumulate(inputList, operator.add)

printIterator(accumulator, "Accumulate Add")

accumulator = itertools.accumulate(inputList, operator.add)

printIterator(accumulator, "Accumulate Mul")


# -- CHAIN --
# With the "chain" method you can create an iterator which will go through every iterable item you provide
# If it is finished with one, it goes through the next item
chain = itertools.chain("ABC", "DEF")

# Another way to chain iterable objects is to use the "chain.from_iterable" method
# This one gets a list of iterable objects
chain = itertools.chain.from_iterable(["DEF", "ABC"])

printIterator(chain, "Chain")


# -- COMPRESS --
# This method provides an iterator, which only returns the elements from the first argument
# when the corresponding element from the second argument evaluates to True
compressor = itertools.compress("ABCDE", [1, 0, 0, 1, 0])

printIterator(compressor, "Compress")


# -- DROPWHILE --
# The "dropwhile" method drops an element until the given predicate is false.
# Then it returns each element in the list
dropper = itertools.dropwhile(lambda x: x % 2, [1, 5, 3, 2, 1, 4])

printIterator(dropper, "Dropwhile")


# -- FILTERFALSE --
# This method is used to filter all elements with the given predicate
# It only returns elements for which the predicate evaluates to false
filter = itertools.filterfalse(lambda x: x < 5, [2, 4, 7, 9, 2, 3])

printIterator(filter, "Filterfalse")


# COMBINATORIC ITERATORS
# ======================

# -- PRODUCT --
# The "product" method provides an iterator over the cartesian product between the input elements
# It is roughly equivalent to a nested for loop
products = itertools.product('ABCD', repeat=2)

printIterator(products, "Product")

products = itertools.product('ABCD', 'xyz')

printIterator(products, "Product")

# -- PERMUTATIONS --
# This method returns the successive n length permutations of the elements in the iterable object.
# The parameter n can be given or defaults to the length of the iterable.
# The permutations are emitted in lexicographic order according to the order in the iterable object.
permutations = itertools.permutations('ABCD', 2)

printIterator(permutations, "Permutations")

# -- COMBINATIONS --
# The "combinations" method returns n length subsequences of the elements in the iterable object.
# The parameter n can be given or defaults to the length of the iterable.
# The permutations are emitted in lexicographic order according to the order in the iterable object.
combinations = itertools.combinations('ABCD', 2)

printIterator(combinations, "Combinations")

# This method allows multiple occurrences of the same element in a subsequence
combinations = itertools.combinations_with_replacement('ABCD', 2)

printIterator(combinations, "Combinations With Replacement")
