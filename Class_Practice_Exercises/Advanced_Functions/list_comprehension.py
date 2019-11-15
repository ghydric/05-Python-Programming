#############################
# List Comprehension  ########
#############################
# Good way to create a new list by performing an
# operation on each item in an existing list

# separate letters in a string
chars = []
for ch in 'Daniel':
    chars.append(ch)
print(chars)

# list comprehension way of doing the above for loop
chars2 = [ch for ch in 'Daniel']
print(chars2)

# get the square of each x in my range of 0-10
squares = [x*x for x in range(11)]
print(squares)

# list of tuples
list1 = [1,2,3]
list2 = ['a','b','c']
combined_list = [(x,y) for x in list1 for y in list2]
print(combined_list)

# list comprehension with optional predicate
evens = [x for x in range(21) if x % 2 == 0]
print(evens)

# list comprehension with multiple optional predicates
numbers = [x for x in range(21) if x % 2 == 0 or x % 5 == 0]
print(numbers)

# if else list comprehension
obj = ['Even' if i % 2 == 0 else 'Odd' for i in range(10) if i % 5 == 0]
print(obj)

# flatten a list
matrix = [[1,2,3],[4,5,6],[7,8,9]]
flat_list = [num for row in matrix for num in row]
print(flat_list)

nums = [1, 2, 3, 4]
str = ['a', 'b', 'c', 'd']
# I want a (letter, number) pair for each letter in
# str and each number in nums

# for loop way
my_list = []
for letter in str:
    for num in nums:
        my_list.append((letter, num))
print(my_list)

# list comprehension way
my_list2 = [(letter, num) for letter in str for num in nums]
print(my_list2)

##########################################################
# Set comprehension
nums = [1, 1, 2, 1, 3, 9, 4, 5, 5, 6, 7, 7, 8, 9, 10]

# for loop way
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)

# set comprehension way
my_set = {n for n in nums}
print(my_set)

########################################################
# Dictionary Comprehension
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
secrets = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# I want a dict{'name': 'secret'} for each name, secret
# in zip(names, secrets)

# using for loop
my_dict = {}
for name, secret in zip(names, secrets):
    my_dict[name] = secret
print(my_dict)

# same as above except using dictionary comprehension
my_dict2 = {name:secret for name, secret in zip(names, secrets)}
print(my_dict2)

##################################################
# Generator expression
# I want to yield 'n*n' for each 'n' in nums
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for loop way
def gen_func(nums):
    for n in nums:
        yield n*n
my_gen = gen_func(nums)
print(next(my_gen))
print(next(my_gen))

# generator comprehension
my_gen2 = (n*n for n in nums)
for i in my_gen2:
    print(i)