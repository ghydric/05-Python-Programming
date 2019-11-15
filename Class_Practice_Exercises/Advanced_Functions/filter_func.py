# Filter
# Takes in 2 arguments, a function and an iterable
# Only returns items in the list that return True

def isOdd(x):
    for n in range(2,x):
        if x % n == 0:
            return False
        else:
            return True

filterObject = filter(isOdd, range(10))
print('Prime numbers between 1-10: ', list(filterObject))

# filter applied with lambda function
filterObject2 = filter(lambda x: x % 2 == 0, range(10))

# filter on a random list without a function
randomList = [1, 'a', 0, True, False, '0']
filteredList = filter(None, randomList)
print('The filtered elements are ')
for element in filteredList:
    print(element)