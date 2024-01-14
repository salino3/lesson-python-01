
tasks = { 'task1': {'name':'buy dinner', 'description':'look for a restaurant with nice food', 'status': 'active' }, 
              'task2' :{'name':'eat dinner', 'description':'look for nice place where to eat the dinner', 'status': 'active'} }


print(tasks['task1']['name'])
print(tasks['task2']['status'])

# 

investigation = (
    {'monday': {'name': 'agua3000', 'start': 2019, 'results': 'none'}},
    {'tuesday': {'name': 'perroVSgato', 'start': 2020, 'results': 'cats are better'}},
    {'wednesday': {'name': 'hooman_fly', 'start': 2019, 'results': 'none'}} )

print(investigation[0]['monday']['name'])
print(investigation[1]['tuesday']['results'])
print(investigation[2])

# 

books = [
     
      {'book 1': [ {'title': ('Run')},  {'author': ('Diego Mercedes')}, {'literary_genre': ['Philosofy', 'Commedy']}, {'copyNumber': 2000 } ]},
      {'book 2': [ {'title': ('good Night')},  {'author': ('Lara Mercedes')}, {'literary_genre': ['Philosofy', 'Healthness']}, {'copyNumber': 1500} ]},
]

print(books[0]['book 1'][0])
print(books[0]['book 1'][1])
print(books[1]['book 2'][3]['copyNumber'])


# Simple version - no mandatory parentesis {}

books = [
    {'book 1': {'title': 'Run', 'author': 'Diego Mercedes', 'literary_genre': ['Philosophy', 'Comedy'], 'copyNumber': 2000}},
    {'book 2': {'title': 'Good Night', 'author': 'Lara Mercedes', 'literary_genre': ['Philosophy', 'Healthiness'], 'copyNumber': 1500}},
]

# Acceder a información específica
print("Title of book 1:", books[0]['book 1']['title'])
print("Author of book 1:", books[0]['book 1']['author'])
print("Copy number of book 2:", books[1]['book 2']['copyNumber'])

# 

mi_tupla = ([1, 2, 3], 'a', 'b')

# Acceder a la lista dentro de la tupla
lista_dentro_de_tupla = mi_tupla[0]

# Modificar un elemento específico dentro de la lista
lista_dentro_de_tupla[0] = 5

print(mi_tupla)  # Output: ([5, 2, 3], 'a', 'b')


# 

import copy

mi_tupla = ([1, 2, 3], 'a', 'b')

# Realizar una copia profunda de la tupla
copia_tupla = copy.deepcopy(mi_tupla)

# Modificar la lista dentro de la copia
copia_tupla[0][0] = 5

# Imprimir ambas tuplas
print(mi_tupla)       # Output: ([1, 2, 3], 'a', 'b')
print(copia_tupla)    # Output: ([5, 2, 3], 'a', 'b')

# 

# mi_tupla = (my_list: [1, 2, 3], 'a', 'b') // no possible
