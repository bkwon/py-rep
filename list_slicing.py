"""
List Slicing

Python allows you to extract a sublist from a list using slicing.
When you slice a list you access it with two indices separated by
a colon. This will produce a new list with the elements with indices
starting at the first index up to, but not including, the second
index. If the index before the colon is missing, the slice starts at
the first element of the list. If the index after the colon is missing,
the slice ends at the last element of the list.

Negative indices may be used in slicing, and they have exactly the same
meaning that they did when used as indices. You can even mix positive
and negative indices in a slice.

Rather than causing errors, if there are no elements in the list between
the indices in the slice, then an empty list is produced.

"""

lst = list(range(10))

# Slice with 3 elements
print(lst[4:7])

# Slice with the last 2 elements of the list
print(lst[8:10])
print(lst[8:])
print(lst[-2:])

# Slice with the first 4 elements of the list
print(lst[0:4])
print(lst[:4])

# Empty slices
print(lst[20:25])
print(lst[7:3])