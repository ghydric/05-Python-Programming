# syntax for slicing a list
# list_name[start:end]

# slicing list example
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
mid_days = days[2:5]
print(mid_days)

numbers = [1, 2, 3, 4, 5]
print(numbers[:3])

print(numbers[2:])

# redundant example - not best practice, just use print(numbers) for the whole list
print(numbers[:])

# Finding items in a list with the "in" operator
# item in list

numbers = [1, 2, 3, 4, 5]
4 in numbers

# item not in list
4 not in numbers # false
6 not in numbers # true



