# Python iterator

#old way:
myList = [1,2,3,4]
for item in myList:
    print(item)

# what is actually happening using iterators
def traverse(iterable):
    it = iter(iterable)
    while True:
        try:
            item = next(it)
            print(item)
        except StopIteration:
            break

L1 = [1,2,3]
item = iter(L1)
print(item.__next__())
print(item.__next__())
print(item.__next__())
print(item.__next__())
print(item.__next__())

# or this method
print(next(it))