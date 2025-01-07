# Diseña un algoritmo que lea 2 números y visualice si son positivos.

# Entrada de Datos
numero1 = int(input('Digite un numero: '))
numero2 = int(input('Digite un numero: '))

#Condicion
if numero1 > 0 and numero2 > 0:
    print(f'El primer numero es: {numero1:.0f}')
    print(f'El segundo numero es: {numero2:.0f}')