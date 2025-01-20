# Pasar de grados Celsius a Fahrenheit y viceversa.


# Entrada de Datos
temperatura = float(input('Ingrese la temperatura: '))
escala = input('Ingrese la escala de la temperatura (C/F): ')

# Función para convertir de Celsius a Fahrenheit
if escala == 'C':
    fahrenheit = (temperatura * 9/5) + 32
    print(f'{temperatura}°C es igual a {fahrenheit:.2f}°F')
elif escala == 'F':
    celsius = (temperatura - 32) * 5/9
    print(f'{temperatura}°F es igual a {celsius:.2f}°C')
else:
    print('Escala no válida')