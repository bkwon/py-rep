"""
Slicing strings. bk
Test
"""

word = "everything"

# Selecting substrings
print("")
print("Selecting Substrings:")
print(word[1:5])  #gets all chars between 1-4 but not including 5
print(word[5:9])

# Open ended slices
print("")
print("Open Ended Slices:")
print(word[5:])
print(word[:4])

# Using negative indices
print("")
print("Using negative indices:")
print(word[-3:])
print(word[2:-3])

# Indexing past the end
print("")
print("Indexing past end:")
print(word[8:20])
print("$" + word[22:29] + "^")

# Empty slices
print("")
print("Empty Slices:")
print(word[6:6])
print(word[4:2])
print(type(word[6:6]))
