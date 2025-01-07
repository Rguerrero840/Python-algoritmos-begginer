#Realizar un algoritmo de tipo de cambio de moneda del dia costarricense

# Entrada de datos
valor_dolar = float(input("Digite el tipo de cambio actual: "))
monto_cambio = float(input("Digite el monto que desea convertir: "))


# Calculo de dolares
colones_a_dolares = monto_cambio / valor_dolar


# Mostrar resultados
print(f"\nEl tipo de cambio es de: {colones_a_dolares:.2f} dolares")
