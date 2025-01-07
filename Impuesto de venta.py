#Diseñar un algoritmo que lea por consola el valor de una factura, en este caso aplicaremos un IGV 18% (Peru).


# Entrada de datos
monto_factura = float(input("Digite el Monto de la factura "))
impuesto_aplicar = float(input("Digite el monto del impuesto "))

# Calculos de impuesto
impuesto_vemta = monto_factura * (impuesto_aplicar / 100)

# Calculo total con impuesto
total_factura = monto_factura + impuesto_vemta

# Mostrar Resultados
print(f"\nEl impuesto fue de: {impuesto_vemta:.2f}")
print(f"El monto total de la factura es de: {total_factura:.2f}")
