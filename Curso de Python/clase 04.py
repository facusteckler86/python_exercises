#import pandas();


# Listas 

##  La lista es un tipo de dato en Python que se utiliza para almacenar múltiples objetos. Es una colección ordenada y mutable de elementos separados por comas entre corchetes

from operator import length_hint
from tarfile import LENGTH_LINK, LENGTH_NAME


numbers = [10, 5, 7, 2, 1]

print("Contenido de la lista:", numbers)  # Imprimiendo contenido de la lista original.

numbers[0] = 111
print("Nuevo contenido de la lista: ", numbers)  # Contenido actual de la lista.

numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.

print("Nuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.

print (numbers[0])


# otro tipo de ejemplo de listas 

numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers)  # Imprimiendo el contenido de la lista original.

numbers[0] = 111
print("\nContenido de la lista con cambio:", numbers)  # Imprimiendo contenido de la lista con 111.

numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Contenido de la lista con intercambio:", numbers)  # Imprimiendo contenido de la lista con intercambio.

print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.

print(numbers) # Aca se imprime la lista completa

# Funcion Len()

# La longitud de una lista puede variar durante la ejecución. Se pueden agregar nuevos elementos a la lista, mientras que otros pueden eliminarse de ella. Esto significa que la lista es una entidad muy dinámica.

# Si deseas verificar la longitud actual de la lista, puedes usar una función llamada len() (su nombre proviene de length - longitud).

# La función toma el nombre de la lista como un argumento y devuelve el número de elementos almacenados actualmente dentro de la lista (en otras palabras - la longitud de la lista).

# Con el comando del() se borran objetos de una lista

# del numbers[1]
# print(len(numbers))
# print(numbers)

# print(numbers[4])
# numbers[4] = 1

###

numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers)  # Imprimiendo el contenido de la lista original.

numbers[0] = 111
print("\nContenido de la lista con cambio:", numbers)  # Imprimiendo contenido de la lista con 111.

numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Contenido de la lista con intercambio:", numbers)  # Imprimiendo contenido de la lista con intercambio.

print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.

###

del numbers[1]  # Eliminando el segundo elemento de la lista.
print("Longitud de la nueva lista:", len(numbers))  # Imprimiendo nueva longitud de la lista.
print("\nNuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.

###

# Uso de negativos, es valido y pueden ser utiles; de nuestra lista el ultimo numero a llegar es -4

numbers = [111, 7, 2, 1]
print(numbers[-1])

# Ejercicio de practica

hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

# Paso 1: escribe una línea de código que solicite al usuario
# reemplazar el número de en medio con un número entero ingresado por el usuario.

hat_list[2] = int(input("Favor de ingresar numero en la lista: "))

# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.

del hat_list[-1]
print("\nSe elima el elemento: ", hat_list)

# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.

print("\nLa longitud de la lista ahora es:", len(hat_list))

print("Lista Final:",hat_list)

####################
result = 0

for x in [3,3,5]:
    if x > 3:
        result = result - x
    else:
        result = result + x

###########################

# Agregando elementos en una lista: append() e insert()

#list.append(value) Aca se toma el valor del argumento y se coloca al final de la lista que posee el método.

# El método insert() es un poco mas completo, ya que lo puede agregar en cualquier parte de la lista, no solo al final como con append()

numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

numbers.insert(1, 333)

#

my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.append(0, i + 1) # type: ignore

print(my_list) # type: ignore

## Otro ejemplo ##

my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)

## mi tipo de lista, pero simplificada

my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)

## Orden de listas

my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)

# El uso del for

for i in range(length_hint // 2): # type: ignore
    my_list[i], my_list[LENGTH_LINK - i - 1] = my_list[LENGTH_NAME - i - 1], my_list[i]

print(my_list)

# Orden Burbuja

# Se lo usa muy poco, pero nunca para listas extensas

# Digamos que una lista se puede ordenar de dos maneras:

# ascendente (o más precisamente - no descendente) - si en cada par de elementos adyacentes, el primer elemento no es mayor que el segundo;

# descendente (o más precisamente - no ascendente) - si en cada par de elementos adyacentes, el primer elemento no es menor que el segundo.
#

my_list = [8, 10, 6, 2, 4]  # lista a ordenar

for i in range(len(my_list) - 1):  # necesitamos (5 - 1) comparaciones
    if my_list[i] > my_list[i + 1]:  # compara elementos adyacentes
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # Si terminamos aquí, tenemos que intercambiar elementos.

my_list = [8, 10, 6, 2, 4]  # lista a ordenar
swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.

while swapped:
    swapped = False  # no hay intercambios hasta ahora
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # ¡ocurrió el intercambio!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)

# Ordenamiento Burbuja - modelo interactivo


my_list = []
swapped = True
num = int(input("¿Cuántos elementos deseas ordenar?: "))

for i in range(num):
    val = float(input("Ingresa un elemento de la lista: "))
    my_list.append(val) # type: ignore

while swapped:
    swapped = False
    for i in range(len(my_list) - 1): # type: ignore
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nOrdenada:")
print(my_list) # type: ignore

## Resumen:

# método sort() para ordenar los elementos de una lista

lst = [5, 3, 1, 2, 4]
print(lst)

lst.sort()
print(lst)  # output: [1, 2, 3, 4, 5]

# También hay un método de lista llamado reverse(), que puedes usar para invertir la lista:

lst = [5, 3, 1, 2, 4]
print(lst)

lst.reverse()
print(lst)  # output: [4, 2, 1, 3, 5]










