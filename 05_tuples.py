
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.8, 'Tom', 'Torres', 35, 9, True)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[-10] # IndexError)

print(my_tuple.count('Tom')) # it says how many of it
print(my_tuple.index('Tom')) # what is the index of value?

# my_tuple[1] = 1.9 # no possible change the tuple`s` values

my_sum_tuple = my_tuple + my_other_tuple

print(my_sum_tuple)
print(my_sum_tuple[3:6]) # (index inclused, index not inclused)

my_tuple = list(my_tuple)
print(my_tuple) # type list
my_tuple.insert(4, 'Red')
my_tuple[-1] = False
my_tuple.append("Violet")


print(my_tuple)


my_tuple = tuple(my_tuple)

# del my_tuple # Error, it`s immutable`
# del my_tuple[2] # Error, its immutable

print(my_tuple)

