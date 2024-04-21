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

import time
for i in range(1,5):
    print(f"Mississippi:{i}")
    breakpoint
    print("Listos o no, aca voy")

    # Bloque while y else

    i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

# Desplazamiento de izq a derecha

var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right)