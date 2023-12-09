## add __pycache__ to .gitignore, but then python create  this folder and his files in thw cloud when it needs them

# file name
import my_module
from my_module import printAll as printAllValues
# from 10_functions import sum_two_value #> it is not possible, the name file start with a number

# function imported
my_module.sumValues(5, 3, 7)

# sumValues(5, 3, 7) # Error
my_module.sumValues('', "Good night!")

my_module.printAll(3, 5, 6 + 9, "Hi!")

printAllValues(3, 5, 6 + 9, "Hi!")



import math
import random
from math import pi # slightly better performance

print(pi)

number = math.pow(2, 8)
print(number)

print('---------------------')

print(math.log2(20))

number = math.log2(20)
print(number ** 2)

print(math.sqrt(20))








