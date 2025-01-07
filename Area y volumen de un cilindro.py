#Determina su area y volumen de un cilindro, aplicando un radio ingresando su valor por teclado y tambien su altura.

import math

# Entrada de Datos, Radio y Altura
radio = float(input ("Digite el radio del Cilindro "))
altura = float(input ("Digite la altura del Cilindro "))

# Calcular el area del cilindro A = 2πr² + 2πrh
area = 2 * math.pi * radio**2 + 2 * math.pi * radio * altura

# Calcular el volumen del cilindro V = πr²h
volumen =  math.pi * radio**2 * altura

# Mostrar Resultados
print(f"\nEl área superficial del Cilindro es: {area:.2f} unidades cuadradas.")
print(f"El volumen del Cilindro es: {volumen:.2f} unidades cúbicas.")
