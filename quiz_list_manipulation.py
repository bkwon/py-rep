"""
Given the list 𝚖𝚢_𝚕𝚒𝚜𝚝 = [𝟷, 𝟹, 𝟻, 𝟽, 𝟿], which of the following slices returns the list [𝟹, 𝟻, 𝟽, 𝟿]?
"""
my_list = [1,3,5,7,9]
print(my_list[1:4])
print(my_list[1:])
print(my_list[1:-1])
print(my_list[2:4])


"""
Which of the following expressions returns a tuple of length one?
-- a bit of a trick question --
"""
print(len([1]))
# print(len(1, ))
# print(len((1)))
print(len((1,)))
# print(len(1))

print(type([1])) #this will return type 'list' <-- but course quiz says this is a tuple.. ???
print(type(1, )) #this returns 'int' but i expected tuple because it's an int followed by a comma..???
print(type((1,)))  #this will return type 'tuple' which is immutable
print(type(1))

"""
Why does the following code snippet raise an error in Python? 
"""
# instructors = ("Scott", "Joe", "John", "Stephen") #this won't work because tuples are immutable
instructors = ["Scott", "Joe", "John", "Stephen"] #this would work because it's a list that can be manipulated
instructors[2 : 4] = []
print(instructors)


"""
Given a non-empty list 𝚖𝚢_𝚕𝚒𝚜𝚝, which item in the list does the operation 𝚖𝚢_𝚕𝚒𝚜𝚝.𝚙𝚘𝚙() remove?
"""
my_list = [1,2,3,4,5]
print(my_list[-1])
print(my_list.pop())


"""
What output does the following code snippet print to the console?
my_list = [1, 3, 5, 7, 9]
my_list.reverse()
print(my_list.reverse())
"""
print()
print("Printing my_list examples for reverse")
my_list = [1, 3, 5, 7, 9]
my_list.reverse()
print(my_list)
print(my_list.reverse())


"""
Given a list 𝚏𝚒𝚋 = [𝟶, 𝟷], write a loop that appends the sum of the last two items in 𝚏𝚒𝚋 to the end of 𝚏𝚒𝚋. 
What is the value of the last item in 𝚏𝚒𝚋 after twenty iterations of this loop? Enter the answer below as an integer.

As a check, the value of the last item in 𝚏𝚒𝚋 after ten iterations is 89.
"""
print()
print("Last item in fib after 'x' iterations is")
fib = [0, 1]
count = 0
for item in fib:
    while count < 20:
        numbers = fib[-2:]
        next_num = sum(numbers)
        # print(next_num)
        fib.append(next_num)
        count += 1
print(fib[-1])


"""
One of the first examples of an algorithm was the Sieve of Eratosthenes. This algorithm computes all 
prime numbers up to a specified bound. The provided code below implements all but the innermost loop 
for this algorithm in Python. Review the linked Wikipedia page and complete this code.
"""
"""
Implement the Sieve of Eratosthenes
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""


def compute_primes(bound):
    """
    Return a list of the prime numbers in range(2, bound)
    Note: I did not follow the expected solution for this problem in the course.
    I understood my logic below better than what the course was presenting to me so i did it my way. -bk
    """

    sieve = [True] * bound
    # answer = list(range(2, bound))
    list1 = []
    # print("Answer: " + str(answer))
    for divisor in range(2, bound):
        # Remove appropriate multiples of divisor from answer
        if (sieve[divisor]):
            list1.append(divisor)
            for i in range(divisor, bound, divisor):
                sieve[i] = False
    return list1

print()
print("List of Primes")
print(len(compute_primes(200)))
print("Second list................")
print(len(compute_primes(2000)))