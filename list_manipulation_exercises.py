import random

"""
Template - Update an item in a list
Given a list 𝚎𝚡𝚊𝚖𝚙𝚕𝚎_𝚕𝚒𝚜𝚝 containing at least 4 elements, write an expression that
assigns the value 𝟶 to the third element of the list.
"""

example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

# Enter update code here
example_list[2] = 0
print(example_list)

# Output
#[2, 3, 5, 7, 11, 13]
#[2, 3, 0, 7, 11, 13]


"""
Template - Update a slice of a list
Given a list 𝚎𝚡𝚊𝚖𝚙𝚕𝚎_𝚕𝚒𝚜𝚝 containing at least 4 elements, write an expression that 
replaces the second and third elements of the list by the list [𝟶, 𝟶, 𝟶]
"""

example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

# Enter update code here
example_list[1:3] = [0,0,0]
print(example_list)


# Output
#[2, 3, 5, 7, 11, 13]
#[2, 0, 0, 0, 7, 11, 13]

"""
Template - Append an item to a list
Given a list 𝚎𝚡𝚊𝚖𝚙𝚕𝚎_𝚕𝚒𝚜𝚝, write an expression that mutates 𝚎𝚡𝚊𝚖𝚙𝚕𝚎_𝚕𝚒𝚜𝚝 such that 
the number 𝟶 is appended (i.e. added to the end) to the list.
"""

example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

# Enter update code here
example_list.append(0)
print(example_list)
example_list.append(["hello", "bryant"])
print(example_list)

# Output
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13, 0]
#[2, 3, 5, 7, 11, 13, 0, ['hello', 'bryant']]


"""
Template - Extend a list with another list
Given a list 𝚎𝚡𝚊𝚖𝚙𝚕𝚎_𝚕𝚒𝚜𝚝, write an expression that mutates 𝚎𝚡𝚊𝚖𝚙𝚕𝚎_𝚕𝚒𝚜𝚝 such that 
the numbers in the list [𝟶, 𝟶, 𝟶] are appended to the list. You should not use a loop here.
"""

example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

# Enter update code here
example_list.extend([0,0,0])
print(example_list)


# Output
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13, 0, 0, 0]


"""
Template - Concatenate one list onto another
Given a list 𝚎𝚡𝚊𝚖𝚙𝚕𝚎_𝚕𝚒𝚜𝚝, write an expression that 
appends the numbers in the list [𝟶, 𝟶, 𝟶] to 𝚎𝚡𝚊𝚖𝚙𝚕𝚎_𝚕𝚒𝚜𝚝 . 
Note that this expression should not mutate 𝚎𝚡𝚊𝚖𝚙𝚕𝚎_𝚕𝚒𝚜𝚝. 
(Again, you should not use a loop here.)
"""

example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

# Enter update code here
new_list = example_list + [0,0,0]
print(example_list)
print(new_list)


# Output
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13, 0, 0, 0]


"""
Template - Append several item to a list
Given a list 𝚎𝚡𝚊𝚖𝚙𝚕𝚎_𝚕𝚒𝚜𝚝, write a loop that mutates 𝚎𝚡𝚊𝚖𝚙𝚕𝚎_𝚕𝚒𝚜𝚝 such that 
the numbers in the list [𝟶, 𝟶, 𝟶] are appended to the list. 
"""

example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

# Enter update code here
for number in [0,0,0]:
    example_list.append(number)
print("0,0,0 are appended to the following: " + str(example_list))

for number in [0,0,0]:
    example_list.pop()
print("The three 0's are popped from this list: " + str(example_list))

for word in ["hello", "bryant", "kwon"]:
    example_list.append(word)
print(example_list)

# Output
# [2, 3, 5, 7, 11, 13]
# [2, 3, 5, 7, 11, 13, 0, 0, 0]


"""
Template - Convert a list to a tuple
Given a list 𝚎𝚡𝚊𝚖𝚙𝚕𝚎_𝚕𝚒𝚜𝚝, write an expression that 
constructs a tuple whose items correspond to those in 𝚎𝚡𝚊𝚖𝚙𝚕𝚎_𝚕𝚒𝚜𝚝.
"""

print()
print("Converting List to Tuple")
example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

# Enter update code here
example_tuple = tuple(example_list)
print(example_tuple)

# Output
# [2, 3, 5, 7, 11, 13]
# (2, 3, 5, 7, 11, 13)


"""
Template - Shuffle the items in a list
Given a list 𝚎𝚡𝚊𝚖𝚙𝚕𝚎_𝚕𝚒𝚜𝚝, write an expression that mutates 𝚎𝚡𝚊𝚖𝚙𝚕𝚎_𝚕𝚒𝚜𝚝 by shuffling 
(i.e. randomly reordering) the items in this list. 
Hint: investigate the various methods in the 𝚛𝚊𝚗𝚍𝚘𝚖 module.
"""

print()
print("Random Shuffle Module Example")
example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

# Enter update code here
random.shuffle(example_list)
print(example_list)

# Output - note that order of second list may vary due to randomness
# [2, 3, 5, 7, 11, 13]
# [11, 2, 7, 5, 13, 3]


"""
Template - Flatten a nested list
    Challenge: The items in a list can themselves be lists. 
    These nested lists can be used to represent a wide range of 2D data such as spreadsheet information. 
    Write a function 𝚏𝚕𝚊𝚝𝚝𝚎𝚗(𝚗𝚎𝚜𝚝𝚎𝚍_𝚕𝚒𝚜𝚝) that takes as input the list of lists 𝚗𝚎𝚜𝚝𝚎𝚍_𝚕𝚒𝚜𝚝. 
    The function 𝚏𝚕𝚊𝚝t𝚎𝚗() should return a list consisting of the items in the sublists of 𝚗𝚎𝚜𝚝𝚎𝚍_𝚕𝚒𝚜𝚝 
    all appended together. (See the provided template for example input and output.) 
"""

def flatten(nested_list):
    """
    Given a list whose items are list,
    return the list formed by joining all of these lists
    """
    flat_list = []
    for sub_list in nested_list:
        flat_list.extend(sub_list)
    return flat_list
print()
print("Flatten a nested list")
# Test code
print(flatten([]))
print(flatten([[]]))
print(flatten([[1, 2, 3]]))
print(flatten([["cat", "dog"], ["pig", "cow"]]))
print(flatten([[9, 8, 7], [6, 5], [4, 3, 2], [1]]))


# Output
#[]
#[]
#[1, 2, 3]
#['cat', 'dog', 'pig', 'cow']
#[9, 8, 7, 6, 5, 4, 3, 2, 1]


"""
Template - Remove duplicates from a list while preserving the order of items
Challenge: Write a function 𝚛𝚎𝚖𝚘𝚟𝚎_𝚍𝚞𝚙𝚕𝚒𝚌𝚊𝚝𝚎𝚜(𝚒𝚝𝚎𝚖𝚜) that takes a list 𝚒𝚝𝚎𝚖𝚜 
and returns a new list that consists of all unique items in 𝚒𝚝𝚎𝚖𝚜. The items in 
the returned list should be in the same order as those in 𝚒𝚝𝚎𝚖𝚜. 
"""

myList = [1, 2, 3, 1, 2, 5, 6, 7, 8]
cleanlist = []
[cleanlist.append(x) for x in myList if x not in cleanlist]


def remove_duplicates(items):
    """
    Given a list, return a list with duplicate items removed
    and the remaining items in the same order
    """
    no_duplicates = []
    for item in items:
        if item not in no_duplicates:
            no_duplicates.append(item)

    return no_duplicates



# Test code
print()
print("Remove duplicates and return a clean list in order")
print(remove_duplicates([]))
print(remove_duplicates([1, 2, 3, 4]))
print(remove_duplicates([1, 2, 2, 3, 3, 3, 4, 5, 6, 6]))
print(remove_duplicates(["cat", "dog", "cat", "pig", "cow", "cat", "pig", "pug"]))


# Output
#[]
#[1, 2, 3, 4]
#[1, 2, 3, 4, 5, 6]
#['cat', 'dog', 'pig', 'cow', 'pug']