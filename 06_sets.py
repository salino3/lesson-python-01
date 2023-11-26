
my_set = set()

my_other_set = {}

print(my_set)
print(type(my_set)) # type set

print(my_other_set)
print(type(my_other_set)) # type dict - dictionary

# my_other_set = {'Milan','Roma', 'Madrid', 'roma', 'roma',  'Madrid'}

my_other_set = {'Milan','Roma', 'Madrid'}


print(my_other_set)
print(type(my_other_set))  # type set

print(len(my_other_set))

my_other_set.add('Hola')
my_other_set.add('Milan')

print(my_other_set) # set is not ordered structure, set doen't repeat values

print('Milan' in my_other_set)
print('Milano' in my_other_set)

my_other_set.remove('Milan')
print(my_other_set)

# del my_other_set
# print(len(my_other_set)) # Error

# del my_other_set[1]
# print(my_other_set) # Error

my_other_set.clear()
print(len(my_other_set))

my_set = {'Mario', 56, True}
my_list = list(my_set)
print(my_list)


my_other_set = {False, 'Joe', 67}

print(my_other_set)

# my_new_ser = my_set + my_other_set # Error
my_new_ser = my_set.union(my_other_set)

print(my_new_ser.union({'Javascript'}).union(my_list).union('Typescript'))
print(my_set)

my_set.add('Joe')

# from first one remove matches value of second one
print(my_new_ser.difference(my_set))
