# Diseñe un algoritmo que lea el nombre del estudiante, el valor de la matrícula en un diplomado y la respuesta a la pregunta: ¿Es egresado de la universidad? 
# Si la respuesta es 'sí', aplique un descuento del 25% sobre el valor de la matrícula. 
# Finalmente, muestre el nombre del estudiante y el valor final a pagar por la matrícula después de aplicar el descuento, si corresponde.

# Datos
descuento_porciento = 0.25
respuesta_egresado = 'si'

# Entrada de datos
nombre_estudiante = str(input('Ingrese el nombre del estudiante: '))
valor_matricula = float(input('Ingrese el monto de la matricula: '))
pregunta = str(input('¿Es egresado de la universidad? : '))

# Mostrar datos
print(f'\nEl nombre del estudiante es {nombre_estudiante}')
print(f'El monto de la matricula {valor_matricula:.2f}')

# Condicion
if pregunta == respuesta_egresado:
    print('Se le aplica un 25 porciento de descuento en la matricula.')
    descuento_matricula = valor_matricula * descuento_porciento
    print(f'El descuento es de: {descuento_matricula:.2f}')
    valor_final = valor_matricula - descuento_matricula
    print(f'El valor final de la matricula es de: {valor_final:.2f}')



