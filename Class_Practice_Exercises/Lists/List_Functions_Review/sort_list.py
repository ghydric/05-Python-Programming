# list.sort() method on lists
# (mutates the list)
my_list = [9, 1, 0, 2, 8, 6, 7, 4, 5, 3]
print('Original order:', my_list)
my_list.sort()
print('Sorted order:', my_list)

# sorted function does not mutate the original list (temporary)
my_list2 = [9, 1, 0, 2, 8, 6, 7, 4, 5, 3]
print('Before sorted: ', my_list2)
print(sorted(my_list2))
print('After sorted:', my_list2)