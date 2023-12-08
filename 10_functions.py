
# my_function() # Traceback (most recent call last):
  #   File "C:\Users\Usuario1\Desktop\Python\lesson-python-01\10_functions.py", line 1, in <module>
  #     my_function()
  # NameError: name 'my_function' is not defined

## function can not be executed before created

# def - define
def my_function():
    print("This is a function!")

# it's possible to rename de function


my_function()
my_function()

def sum_two_values(first: int, second: int):
    print(first + second)

def sum_two_values2(first: int, second: int):
    if not (isinstance(first, int) and isinstance(second, int)):
        print("Error: Both values must be 'integer'")
    else:
        print(first + second)


sum_two_values(2, 4)
sum_two_values("2", "4") # it works anyway

sum_two_values2(2, "4") 

print('------------------')



## 

value_of_fn = sum_two_values2(2, 12) 

print(value_of_fn) # None


print('----------------------')

def sum_with_return(a, b):
    return a + b

value_of_fn = sum_with_return("3", str(7))

print(value_of_fn)

print(sum_with_return("3", str(7)))

print('---------------')


def print_name(name, surname):
    print(f"My name is {name} {surname}")
    print("My name is %s %s" %(name, surname))


print_name(surname =  "Smith", name = "Bryan")
     
      

def print_name_with_defult(name, surname, alias = ""):
    print("My name is %s %s %s" %(name, surname, alias))

print_name_with_defult("Joe", "Torres", "PythonDev")
print_name_with_defult("Joe", "Torres")

print('-------------------')

def print_texts(*text): # numbers of parameters dynamic, like arguments in javascript
    print(text)

print_texts("Hola", 4, 'tyu')

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())

print(print_upper_texts('good', "Tom", "Google", "red"))

##

def ejemplo_funcion( *args, **kwargs): # (they are tuples, the are dictionaries)
    print("positional arguments:", args)
    print("Keyword arguments:", kwargs)

# Llamada a la función con argumentos posicionales y de palabra clave
ejemplo_funcion(1, {2: "Hello"}, 3, nombre="John", edad=25, address = "Av. Andalucía")

      

