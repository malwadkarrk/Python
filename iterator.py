# define a list
my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)

#prints 4
print(next(my_iter))

#prints 7
print(next(my_iter))

## next(obj) is same as obj.__next__()

#prints 0
print(my_iter.__next__())

#prints 3
print(my_iter.__next__())

# Using for loop
for i in my_list:
    print(i)

# Using while loop

iter_obj = iter(my_iter)
while True:
    try:
        i = next(iter_obj)
    except StopIteration:
        break
