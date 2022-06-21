# Generators are functions that create objects lazily
import sys


def get_list(num_of_obj):
    return_list = []
    for i in range(num_of_obj):
        return_list.append(i)

    return return_list


def get_list_generator(num_of_obj):
    for i in range(num_of_obj):
        # Using yield instead of return
        yield i


# 20 items
[print(i) for i in get_list(10)]
print(f'The size of get_list(10) is {sys.getsizeof(get_list(20))} bytes')
print()

# With a generator
g = get_list_generator(10)
[print(i) for i in g]
print(f'The size of g is {sys.getsizeof(g)} bytes')
print()

# 1,000,000 items - huge size difference
print(f'The size of get_list(1000000) is {sys.getsizeof(get_list(1000000))} bytes')

g = get_list_generator(1000000)
print(f'The size of g is {sys.getsizeof(g)} bytes')
print()

# Generator EXPRESSIONS - by using ()
# List comprehension - by using []
lc = [i for i in range(10)]
[print(i) for i in lc]
print(f'The size of lc is {sys.getsizeof(lc)} bytes')
print()

g2 = (i for i in range(10))
[print(i) for i in g2]
print(f'The size of g2 is {sys.getsizeof(g2)} bytes')
