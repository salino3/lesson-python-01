# Variables - always in lowercase - convention

my_string_var = "My string variable"
print(my_string_var)

my_int_var = 5
print(my_int_var)

my_int_to_var = str(my_int_var)
print(my_int_to_var)
print(type(my_int_to_var))

my_bool_var = False
print(my_bool_var)

print('------------')
# concatenation of variables with print
print(my_string_var, str(my_int_var), 'Hola', my_bool_var)
# print(type(print(my_string_var, str(my_int_var), 'Hola', my_bool_var))) # it doesn't work # NoneType
# print(type(my_string_var, str(my_int_var), 'Hola', my_bool_var)) # it doesn't work

print("This is the value: ", my_bool_var)

# system function
print('------------')

print(len(my_string_var))
# print(len(my_int_var))


# Variables in one line
name, surname, alias, age = "Bryan", "Torres", 'Dev', 35.2
print(type(age))
print(name, age, surname, alias, "my age is: " + str(age))


# first_name = input("What\'is your name?\n")
# I can modify variables with input()
name = input("What\'is your name?\n")
age = input('How old are you?\n')

print ('My name is ' + name + ' and I\'m ' + age + ' years old')
