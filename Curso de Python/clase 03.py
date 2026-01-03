# Operadores y expresiones

print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

# enlaces

print(9 % 6 % 2)


print(-3 ** 2)
print(-2 ** 3)
print(-(3 ** 2))



# Bucle For

for i in range(2, 8, 3):
    print("El valor de i es", i)

# Uso del range en exponenciales, siempre se lo asocia con el for y debe ser ascendente la tabla
# uso de la variable expo

power = 1
for expo in range(16):
    print("2 a la potencia de", expo, "es", power)
    power *= 2

# Bucle for con uso del range

# import time
for i in range(1,5):
    print(f"Mississippi:{i}")
    breakpoint # type: ignore
    print("Listos o no, aca voy")

    # Bloque while y else

    i = 1
while i < 5: # type: ignore
    print(i) # type: ignore
    i += 1 # type: ignore
else:
    print("else:", i) # type: ignore

# Desplazamiento de izq a derecha

var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right)

#1. Python es compatible con los siguientes operadores lógicos:

# and → si ambos operandos son verdaderos, la condición es verdadera, por ejemplo, (True and True) es True.
# or → si alguno de los operandos es verdadero, la condición es verdadera, por ejemplo, (True or False) es True.
# not → devuelve False si el resultado es verdadero y devuelve True si es falso, por ejemplo, not True es False.
# 2. Puedes utilizar operadores bit a bit para manipular bits de datos individuales. Los siguientes datos de muestra:

# x = 15, el cual es 0000 1111 en binario,
# y = 16, el cual es 0001 0000 en binario.
# Se utilizarán para ilustrar el significado de operadores bit a bit en Python. Analiza los ejemplos a continuación:

# & hace un bit a bit and (y), por ejemplo, x & y = 0, el cual es 0000 0000 en binario,
# | hace un bit a bit or (o), por ejemplo, x | y = 31, el cual es 0001 1111 en binario,
# ˜ hace un bit a bit not (no), por ejemplo, ˜ x = 240*, el cual es 1111 0000 en binario,
# ^ hace un bit a bit xor, por ejemplo, x ^ y = 31, el cual es 0001 1111 en binario,
# >> hace un desplazamiento bit a bit a la derecha, por ejemplo, y >> 1 = 8, el cual es 0000 1000 en binario,
# << hace un desplazamiento bit a bit a la izquierda, por ejemplo, y << 3 = 128, el cual es 1000 0000 en binario.

# Caso 01

x = 1
y = 0

z = ((x == y) and (x == y)) or not(x == y) # type: ignore
print(not(z))

# Caso 02

x = 4
y = 1

a = x & y
b = x | y
c = ~x  # ¡difícil!
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)

#Listas en Python





