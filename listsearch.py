"""
Searching lists.
"""

toys = ["blocks", "slinky", "fidget spinner", "cards", "doll house", "legos", "blocks", "teddy bear"]
food = ["chicken", "beef", "candy"]

# Finding items in a list
print(toys.index("legos"))
print(toys.index("blocks"))
#print(toys.rindex("blocks"))
#print(toys.index("video game"))

print("")

# Checking if items are in a list
print("legos" in toys)
# print("chicken" in food)
# print("candycane" in food)
print("blocks" in toys)
print("video game" in toys)
print("teddy bear" not in toys)
print("dice" not in toys)

print("")

# Counting items in list
print(toys.count("slinky"))
print(toys.count("blocks"))