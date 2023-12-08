
class MyEmptyPerson:
    pass # pass when it doesn't return anything 


print(MyEmptyPerson())

class Person: 
    def __init__(self, name, surname, alias = "Sin alias"):
        self.name = name
        self.second_name = surname
        self.full_name = f"{name} {surname} ({alias})"
    
    def walk (self):
        print(f"{self.full_name} is walking")

class Pet: 
    def __init__(self, name, secondName):
        self.name = 'Micky'
        self.secondName = 'Mouse'
        self.full_name = name + ' ' + self.secondName

    def __str__(self):
        return f"Pet name {self.name}, secondName {self.secondName}"


#

person1 = Person("Mario", "Smith")
person2 = Person("Fran", "Torres", "Paco")
pet1 = Pet("Girolamo", "Mattei")

print(person1.name)
print(person1.second_name)

print(f"My name is {person1.name} {person1.second_name}")


print(pet1.full_name)
print(person1.walk()) # None
person1.walk()
person2.walk()

print('----------------------')

person2.full_name = "Héctor el loco"
person2.walk()


print('----------------')


class Worker: 
    def __init__(self, name, surname, alias = "Sin alias"):
        self.__name = name # private property
        self.__second_name = surname # private property
        self.full_name = f"{self.__name} {surname} ({alias})" # public property

    def get_name (self):
        return self.__name
    
    def change_name(self, new_name):
         self.__name = new_name
        
    
    def walk (self):
        print(f"{self.full_name} is walking")


worker1 = Worker("Giorgia", "Lara")


print(worker1.full_name)
# print(worker1.__name) # this property is private
print(worker1.get_name())
worker1.change_name("Hilan")
print(worker1.get_name())





