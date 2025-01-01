# This is about Remove Duplicates From Sorted Array
# Brute Force Approach

arr = [1,2,2,2,3,4,4,5,5,5,6,7,7,7,9,9,9,9]
unique_elements = set()

for num in arr:
    unique_elements.add(num)
print(list(unique_elements))

'''
What is a set in Python?
A set is an unordered collection of unique elements.
It is mutable, meaning you can add or remove items.
Sets do not allow duplicate elements, making them useful for operations like removing duplicates.


my_set = set()  # Creates an empty set

my_set = {1, 2, 3}  # A set with three elements

my_list = [1, 2, 2, 3]
my_set = set(my_list)  # Converts list to set and removes duplicates

my_set.add(4)  # Adds 4 to the set

my_set.remove(2)  # Removes 2; raises an error if 2 is not in the set
my_set.discard(5)  # Removes 5; does nothing if 5 is not in the set

if 3 in my_set:
    print("3 is in the set")

print(len(my_set))  # Number of unique elements in the set

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # {1, 2, 3, 4, 5}

intersection_set = set1 & set2  # {3}

difference_set = set1 - set2  # {1, 2}

sym_diff_set = set1 ^ set2  # {1, 2, 4, 5}

Special Methods:

new_set = my_set.copy()

my_set.clear()  # Empties the set

frozen = frozenset([1, 2, 3])
# You cannot add or remove elements from a frozenset

my_list = [1, 2, 2, 3]
unique_elements = set(my_list)  # {1, 2, 3}

allowed_numbers = {1, 3, 5, 7}
if 4 not in allowed_numbers:
    print("4 is not allowed")

primes = {2, 3, 5, 7}
evens = {2, 4, 6, 8}
print(primes & evens)  # Intersection: {2}

'''