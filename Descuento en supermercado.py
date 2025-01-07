#Diseñar un algoritmo que permita aplicar un descuento en el supermercado de tal forma permita visualizar el monto a pagar despues de aplicar dicho procedimiento.



# Entrada de datos
precio_sin_descuento = float(input ("Digite el monto de la compra "))
descuento = float(input("Digite el descuento a aplicar "))

# Calculo de descuento
descuento_aplicar = (descuento / 100) * precio_sin_descuento 

# Calculo de precio final
precio_final = precio_sin_descuento - descuento_aplicar

# Mostrar resultados
print(f"\nEl descuento es de: {descuento_aplicar:.2f}")
print(f"El monto total a pagar es de: {precio_final:.2f}")
