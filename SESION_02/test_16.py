"""
Requisitos

1. Crear 2 variables enteras, 2 variables flotantes, 1 variable string, 1 variable string con contenido solamente numerico, 1 variable boolean
2. Obtener y mostrar la suma de una variable entera con la variable strin numérica (realizar conversiones si es necesario)
3. Obtener y mostrar la suma de las 2 variables enteras mas la variable string numérica y la variable flotante
4. Obtener y mostrar el modulo de la variables esteras: %
5. Obtner y mostrar el resultado entero o l parte entera de las 2 variables int: //
6. Obtener la potencia usando una de las variables flotantes como base y la variable entera como potencia
"""

var_int1 = 50
var_int2 = 30
var_float1 = 25.5
var_float2 = 40.7
var_str1 = "Loco"
var_str2 = "15"
var_bool = True

suma_1 = var_int1 + int(var_str2)
suma_2 = var_int1 + var_int2 + int(var_str2) + var_float1
suma_3 = var_int1 % var_int2
suma_4 = var_int1 // var_int2
potencia = pow(var_float1, var_int1)

print(suma_1)
print(suma_2)
print(suma_3)
print(suma_4)
print(potencia)