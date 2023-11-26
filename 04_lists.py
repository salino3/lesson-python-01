
my_list = list()
my_others_list = []


print(my_list)
print(len(my_list))
print(my_others_list)
print(len(my_others_list))
print('-------------------')

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_others_list = [35, 1.77, "Bryan", "Doe"]



print(my_others_list)
print(type(my_others_list))
print(my_others_list[0])
print(my_others_list[1])
print(my_others_list[2])
print(my_others_list[-1])
print(my_others_list[-3])
# print(my_others_list[4]) # in this case:  IndexError: list index out of range
# print(my_others_list[-5]) # in this case:  IndexError: list index out of range
print(my_others_list.count("Bryan")) # count occurrences in the list

# unpacked variables - it needs all elements

# no good practice
age, height, name, surname = my_others_list
print(name)

name, height, age, surname = my_others_list[2], my_others_list[1], my_others_list[0], my_others_list[3]
print(name)

print(my_list + my_others_list + my_list)

my_others_list.append("My Comapny") # push it in list at the end

my_others_list.insert(1, "Blue") # (index, value)


print(my_others_list)

my_others_list.remove("Blue") # (value) first one match the value

print(my_others_list)

my_others_list[1] = "Green"
my_others_list[1] = "Red"

print(my_others_list)

my_pop_item = my_others_list.pop() # () remove the last one, (index) remove this one in the list
my_pop_item2 = my_others_list.pop(3)
print(my_pop_item) # I can print the value I deleted
print(my_pop_item2) # I can print the value I deleted

print(my_others_list)

del my_list[2] # delete
print(my_list)


print('-----------------')

my_new_list = my_list.copy() # it must be a list

my_list.clear() # to reset the list

print(my_list)
print(my_new_list)
my_new_list.reverse() # outside print()
print(my_new_list)
print(my_others_list[::-1])

# my_others_list.sort() # only same types
print(my_new_list.sort())

print(my_new_list[1:2])
print(my_new_list[1:3])


my_list = "Hi Python"
my_list

# Now is not a list, it's a variable
print(my_list)


numbers_list = [4, 2, 8, 1, 7]
numbers_list.sort(reverse=True)
print(numbers_list)


def custom_key(element):
    return element % 3

list = [4, 2, 8, 1, 7]

list.sort(key=custom_key) # using result as rule for ordering the elements

print(list)

# ------

def custom_key_complex(element, value):
    return element % value

list.sort(key=lambda x: custom_key_complex(x, 3)) # using result as rule for ordering the elements
print(list)

my_strings = ["banana", "apple", "orange", "grape", "kiwi"]
my_strings.sort()

print(my_strings) # output: ['apple', 'banana', 'grape', 'kiwi', 'orange']

# del my_strings # Error

# print(my_strings) # Error
