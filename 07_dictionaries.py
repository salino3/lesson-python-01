
# dict - relation key: value

my_dictionary = dict()

my_other_dictionary = {}

print(my_dictionary)
print(type(my_other_dictionary))# type dict

my_other_dictionary = {"Name": "Bryan", "Surname": "Smith", "Age": 45, 1:"Python"}

# print(my_other_dictionary[0]) # KeyError: 0


my_dictionary = {
    "Name": "Bryan",
    "Surname": "Smith",
    "Age": 45,
    "languages": {"Python", "Swift", "Kotlin"},
    1: 1.80, 
    }

print(my_other_dictionary)
print(my_dictionary)
print(len(my_other_dictionary))
print(len(my_dictionary["languages"]))
print(len(my_dictionary))

print('-------------------')

my_dictionary["Name"] = "Mario"

print(my_dictionary)
print(my_dictionary[1])
my_dictionary["Address"] = "Av. Andalucía"
print(my_dictionary)

print('-------------------')

del my_dictionary["Address"] 

print(my_other_dictionary)
print(my_dictionary)

# it look for using 'key'
print("Mario" in my_dictionary)
print("Luigi" in my_dictionary)
print("Name" in my_dictionary)

print(my_dictionary.items())
print(my_dictionary.keys())
print(my_dictionary.values())
print("Mario" in my_dictionary.values())
print(my_dictionary.fromkeys("Address"))
print(my_dictionary.fromkeys(("Address", 1)))

# the same rsult with both
my_new_dict = my_dictionary.fromkeys(("Address", 1, "Country"))
my_new_dict = dict.fromkeys(("Address", 1, "Country"))
print(my_new_dict)

print('-------------------')

my_list = ["Name", 1, "Country"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dictionary)
print(my_new_dict)

# every key start with same value
my_new_dict = dict.fromkeys(my_dictionary, ["Hello", 'Good'])
print(my_new_dict)

# they keep the keys as a values
print(list(my_new_dict))
print(list(my_other_dictionary))
print(set(my_other_dictionary))
print(tuple(my_other_dictionary))

print('------------------')
print(list(my_new_dict.values()))
print(list(my_other_dictionary.values()))
print(set(my_other_dictionary.values()))
print(tuple(my_other_dictionary.values()))

print('---------------')
my_new_dict = dict.fromkeys(my_dictionary, 'Madrid')
print(my_new_dict)

print(list(dict.fromkeys(list(my_new_dict.values()))))

# dict.fromkeys(): Create a new dictionary using the elements in the list as keys. 
# this indeed deletes duplicates, because in a dictionaries the keys must be unics.

my_new_values = my_other_dictionary.values() # ['Madrid']
print(type(my_new_values)) # <class 'dict_values'>
print(my_new_values)
