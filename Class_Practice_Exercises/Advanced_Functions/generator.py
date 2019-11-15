# Generators
# cannot have a return statement in generator.
# yield works as a return statement letting the "next"
# function know where each item ends
# more memory efficient than iter

def myGenerator():
    print('First item')
    yield 10

    print('Second item')
    yield 20

    print('Last item')
    yield 30

gen = myGenerator()
print(next(gen))
print(next(gen))
print(next(gen))