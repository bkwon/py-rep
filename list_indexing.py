"""
List Indexing

You access elements of a list using their index. The first element of a
list is located at index 0 (not 1!). The last element of a list named 𝚕𝚜𝚝
is located at index 𝚕𝚎𝚗(𝚕𝚜𝚝) - 𝟷 (not 𝚕𝚎𝚗(𝚕𝚜𝚝)). The syntax to access an
element of a list is to place the index in square brackets after the variable
that refers to a list.

Note that you can also access elements of a list using negative indices. The
last element of a list is located at index -1. The second to last element is
located at index -2. And so on.

"""

lst = list(range(10))

# First element
print(lst[0])

# Third element
print(lst[2])

# Length
print(len(lst))

# Last element
print(lst[9])
print(lst[len(lst) - 1])
print(lst[-1])