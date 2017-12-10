"""
If we want to split a list 𝚖𝚢_𝚕𝚒𝚜𝚝 into two halves,
which of the following uses slices to do so correctly?

More precisely, if the length of 𝚖𝚢_𝚕𝚒𝚜𝚝 is 2n, i.e.,
even, then the two parts should each have length n.
If its length is 2n+1, i.e., odd, then the two parts
should have lengths n and n+1.
"""
my_list = ["This", "course", "is", "great"]

print("Option 1 = Good")

print(my_list[0:len(my_list)//2])
print(my_list[len(my_list)//2:len(my_list)])

print("Option 2 = Bad")

print(my_list[:len(my_list)//2-1])
print(my_list[len(my_list)//2:])

print("Option 3 = Bad")

print(my_list[0:len(my_list)//2])
print(my_list[len(my_list)//2+1:len(my_list)])

print("Open 4 = Good")

print(my_list[:len(my_list)//2])
print(my_list[len(my_list)//2:])

"""
If n and m are non-negative integers, consider the list 𝚏𝚒𝚗𝚊𝚕_𝚕𝚒𝚜𝚝 computed by the code snippet below.

    init_list = list(range(1, n))
    final_list = init_list * m

The length of this list depends on the particular values of n and m used in computation. 
Which option below correctly expresses the length of 𝚏𝚒𝚗𝚊𝚕_𝚕𝚒𝚜𝚝 in terms of n and m?
"""
print("")
print("Question 4:")

n = 5
m = 4
init_list = list(range(1, n))
final_list = init_list * m
print(len(final_list))
print((n-1) * m)   # good
# print(n * m)
# print(n * (m - 1))
# print(n + m)


print("")

print("Question 5:")
"""
If n is a non-negative integer, consider the list split_last computed by the code snippet below:
    test_string = "xxx" + " " * n + "xxx"
    split_list = test_string.split(" ")
The length of this list depends on the particular values of n used in computation.
Which option below correctly expresses the length of split_list in terms of n? 
"""

n = 5
test_string = "xxx" + " " * n + "xxx"
split_list = test_string.split(" ")
print(len(split_list))
print(split_list)

print("")
print("Question 6: ")

'''
Question 6
Select the code snippets below in which 𝚕𝚒𝚜𝚝𝟸 is a copy of list 𝚕𝚒𝚜𝚝𝟷 
(as opposed to simply being another reference to the list 𝚕𝚒𝚜𝚝𝟷).
Uncomment the code blocks below a pair at a time to see the answers...
'''
# list1 = list(range(1, 10))
# list2 = [] + list1

list1 = list(range(1, 10))
list2 = list1    # this is just a reference to existing list 1. no ops done other than assignment
#
# list1 = list(range(1, 10))
# list2 = list1[:]
#
# list1 = list(range(1, 10))
# list2 = list(list1)

print(hex(id(list1)))
print(hex(id(list2)))
if ((hex(id(list1))) == hex(id(list2))):
    print("This is just a reference, not a copy.")
else:
    print("This is a copy with a unique hex id in memory!")


print("")
print("Question 7: ")

"""
Write a function 𝚜𝚝𝚛𝚊𝚗𝚐𝚎_𝚜𝚞𝚖(𝚗𝚞𝚖𝚋𝚎𝚛𝚜) that takes a list of integers and returns the sum of 
those items in the list that are not divisible by 3. When you are done, test your function 
using the code snippet below.

    print(strange_sum([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))
    print(strange_sum(list(range(123)) + list(range(77))))

The first line in the test should print the number 𝟸𝟺 in the console. Enter the second number
printed in the console in the box below.
"""

def strange_sum(numbers):
    print(numbers)
    result_list = []
    count = 0
    sum_results = 0
    for num in numbers:
        if num % 3 != 0:
            count += 1
            result_list.insert(count, num)
            sum_results = sum(result_list)
    return sum_results, result_list

print(strange_sum([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))
print(strange_sum(list(range(123)) + list(range(77))))
