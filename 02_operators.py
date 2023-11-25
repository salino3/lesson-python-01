
print(3 + 4)
print(10 % 3) # 1
print(10 % 2) # 0
print(10 ** 2) # 100
print(20 // 3) # 6 - floor division 


print("Hi" + " how are you?")
print('I\'m good thanks')
# print('five' + 9) # error

print('five ' + str(10))

# it must be a integer number and int type - 5.0 is not admitted
print('Hello ' * 5) # Hello Hello Hello Hello Hello
print('Hello ' * (5 * 3)) 
# print('Hello ' * (7 / 2)) # TypeError: can't multiply sequence by non-int of type 'float'


## Comparative operators

print('. Comparative operators ----------------')
print(3 < 4)
print(3 > 4)
print(3 <= 4)
print(3 >= 4) 
print(4 >= 4) 
print(3 == 4)
print(3 != 4)
print(3 == 4)

print(5 > 4 >= 4)
print((5 + 5) == (5 * 2))
print((3 == 4) == (4 >= 4))

print('. Alfabetic orden ----------')

# alphabetical orden for ASCII
print("Hola" <  "Python")
print("Hola" >  "Python")
print("Hola" <= "Python")
print("Hola" >= "Python") 
print("Hola" >= "Python") 
print("Hola" == "Python")
print("Hola" != "Python")
print("Hola" == "Python")
print("Hola" == "Good")
print("Hola" == "Hola")
print("Hola" >= "Good")
print("Hola" <= "Good")
print("Hola" <= "Zoom")

# Lenght
print(len("Hola") <= len("Zoom"))


## Logic operators

print('. Logic operators -----------')

print(3 > 4 and 'Hola' < 'Python')
print(3 < 4 and 'Hola' < 'Python')
print(3 > 4 or 'Hola' < 'Python')
print(3 > 4 or ('Hola' < 'Python' and 4 == 4))
print(not(3 > 4))

