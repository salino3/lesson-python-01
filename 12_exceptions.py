
numberOne, numberTwo = 5, 1

numberTwo = str(numberTwo)
# print(numberOne + numberTwo) # Error

try:
  print(numberOne + numberTwo)
  print("No Error")
except:
  print("There is a Error")

## it needs 'except' for continuous but 'finally' is executed
# try:
#   print(numberOne + numberTwo)
#   print("No Error")
# finally:
#   print('Continuous... (finally)')
  
print('---------------')

try:
  print(numberOne + int(numberTwo))
  print("No Error")
except:
  print("There is a Error")
# 'else' executes if 'except' doesn't executes
else:
  print('This is the \'else\'')
finally:
  print('Continuous...')
  
print('---------------')

try:
  print(numberOne + numberTwo)
  print("No Error")
except:
  print("Error corrected!")
  print(int(numberOne) + int(numberTwo))
  # 'else' executes if 'except' doesn't executes
else:
  print('This is the \'else\'')
finally:
  print('Continues...')
  

print('--------------------')
# Exceptions for types - TypeError


try:
  print(numberOne + numberTwo)
  print("No Error")
except TypeError: # it stops the code only with a type error
  print("There is a Type Error")
except ValueError: # it stops the code only with a value error
  print("There is a Value Error")


print('---------------------')
# Catch the information of exception

try:
  print(numberOne + numberTwo)
except ValueError as error:
  print(error)
# except TypeError as error:
#   print(error)
except Exception as my_random_error:
  print("Exception ->", my_random_error)


print("Finish...")














