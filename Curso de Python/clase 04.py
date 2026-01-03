#import pandas();


# Listas 

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







