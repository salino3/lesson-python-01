
# While

my_condition = 0


while my_condition < 10:
    print(my_condition)
    my_condition += 1

print('-------------------')

my_condition = 0 

while my_condition < 10:
    print(my_condition)
    my_condition += 2

else:
    print('my_condition it\'s igual or major than 10')

if my_condition == 10:
    print('My condition is igual to 10')


print('-------------------')

while my_condition < 20:
    my_condition += 2
    print(my_condition)
    if my_condition == 15:
        print('my condition is 15')
        break
        
    print('My condition is less than 20')


print('-----------------------------')

# For

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

print('-------------------')
my_tuple = (35, 1.8, 'Tom', 'Torres', 35, 9, True)

for element in my_tuple:
    print(element)

print('-------------------')
my_other_set = {'Milan','Roma', 'Madrid', 89}

for element in my_other_set:
    print(element)

print('-------------------')
my_dictionary = {
    "Name": "Bryan",
    "Surname": "Smith",
    "Age": 45,
    "languages": {"Python", "Swift", "Kotlin"},
    1: 1.80, 
   }

for element in my_dictionary:
    print(element) # it prints the keys
    if element == "Age":
        break
    print('it executes')
else:
    print('the loops "For" is ended')

print('-------------------')
for element in my_dictionary.values():
    print(element) # it prints the values


print('----------------')

for element in my_dictionary:
    print(element) # it prints the keys
    if element == "Age":
        continue # break and return to 'for'
    print('it executes')
else:
    print('the loops "For" is ended')



