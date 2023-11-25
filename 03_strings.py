
## Strings

my_str = "My String "
my_other_str = 'My other String'

print(len(my_str))
print(len(my_other_str))

my_new_line_str = "This is a String \n with line jump!" # lenght '\n' and '\t value as one 
my_escape_string = "\\t escape string"

print(len(my_new_line_str))
print(len(my_escape_string))
print(my_escape_string)

## To format - better performance

# %s %d %f %. 

name, surname, age = "Brayan", "Moure", 25.0

print("My name is {} {} and I\'m {} years old" .format(name, surname, age))
print("My name is %s %s and I\'m %d years old" %(name, surname, age))
print(f"My name is {name} {surname} and I\'m {age} years old")

# unpacked characters

language = "Python"
a, b = language, language
a_word, b_word, c_word, d_word, e_word, f_word = language

print(a, b)
print(a_word, b_word, c_word, d_word, e_word, f_word) # P y t h o n

# Division
language_slice = language[1:4]
print(language_slice)

print('----------')

language_slice = language[1:]
print(language_slice)

language_slice = language[:4]
print(language_slice)
language_slice = language[-2:]
print(language_slice)

language_slice = language[:-4]
print(language_slice)

language_slice = language[-2]
print(language_slice)

print('-----------------')

language_slice = language[1:6:2] # [start:stop:step] step delete just one character
print(language_slice)

# exercise

string_numbers = "12345678901234567890"

slice_modified = string_numbers[2:20:4] 
print(slice_modified)

string_numbers2 = int(slice_modified[0]) + 1
slice_modified2 = string_numbers[3:20:string_numbers2 ]

divide_a1 = slice_modified[0]
divide_a2 = slice_modified[1]
divide_a3 = slice_modified[2]
divide_a4 = slice_modified[3]


divide_b1 = slice_modified2[0]
divide_b2 = slice_modified2[1]
divide_b3 = slice_modified2[2]
divide_b4 = slice_modified2[3]



resultado_combinado_numbers = divide_a1 + divide_b1 + divide_a2 + divide_b2 + divide_a3 + divide_b3 + divide_a4 + divide_b4

print(resultado_combinado_numbers) 

# exercise 2

word = "abcdefghijklmnopqrst"

slice_modified = word[2:20:4]
slice_modified2 = word[3:20:4]

divide_a1 = slice_modified[0]
divide_a2 = slice_modified[1]
divide_a3 = slice_modified[2]
divide_a4 = slice_modified[3]

divide_b1 = slice_modified2[0]
divide_b2 = slice_modified2[1]
divide_b3 = slice_modified2[2]
divide_b4 = slice_modified2[3]

resultado_combinado = divide_a1 + divide_b1 + divide_a2 + divide_b2 + divide_a3 + divide_b3 + divide_a4 + divide_b4

print(resultado_combinado)

# --------------

reversed_word = language[::-1]
print(reversed_word)






