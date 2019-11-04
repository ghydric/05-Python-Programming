# tuples

# initiate a tuple
my_tuple = (1, 2, 3, 4, 5)

print(my_tuple)

#printing items in a tuple
names = ('Holly', 'Warren', 'Ashley')

#for n in names
#    print(n)
for n in range(len(names)):
    print(names[n])

list = [2, 4, 5, 1, 6]
type(list)
tuple(list)
type(list)

# tuples are immutable so this will throw an error:
names.append('Matt')