#Una empresa quiere comprar varias piezas de la misma clase a una fábrica. Dependiendo del valor total de la compra, 
#decidirá cómo pagarlo. El plan de pago depende del monto total de la compra de la siguiente manera:
#Si el valor total de la compra es mayor a $500,000:
#La empresa usará el 50% de su propio dinero.
#Pedirá un préstamo al banco por el 30% del valor de la compra.
#Y el 20% restante lo pagará con un crédito de la fábrica.
#Si el valor total de la compra es menor o igual a $500,000:
#La empresa usará el 70% de su propio dinero.
#Pedirá un préstamo al banco por el 25% del valor de la compra.
#Y el 5% restante lo pagará con un crédito de la fábrica.


# Datos
porcentaje_dinero_propio_alta = 0.50
porcentaje_prestamo_banco_alta = 0.30
porcentaje_credito_fabrica_alta = 0.20

porcentaje_dinero_propio_baja = 0.70
porcentaje_prestamo_banco_baja = 0.25
porcentaje_credito_fabrica_baja = 0.05

# Entrada de datos
valor_compra = float(input('Ingrese el monto total de la compra: '))


# Condicion determinar el plan de pago
if valor_compra > 500000:
    # Para compras mayores a $500,000
    dinero_propio = valor_compra * porcentaje_dinero_propio_alta
    prestamo_banco = valor_compra * porcentaje_prestamo_banco_alta
    credito_fabrica = valor_compra * porcentaje_credito_fabrica_alta

    # Imprimir resultados
    print(f'El valor de la compra es de: {valor_compra:.0f}')
    print(f'Dinero que se puede usar para pagar es de {dinero_propio:.2f}')
    print(f'Se le pedirá al banco {prestamo_banco:.2f}')
    print(f'El crédito de la fábrica es de {credito_fabrica:.2f}')
else:
    # Para compras menores o iguales a $500,000
    dinero_propio = valor_compra * porcentaje_dinero_propio_baja
    prestamo_banco = valor_compra * porcentaje_prestamo_banco_baja
    credito_fabrica = valor_compra * porcentaje_credito_fabrica_baja

    # Imprimir resultados
    print(f'El valor de la compra es de: {valor_compra:.0f}')
    print(f'Dinero que se puede usar para pagar es de {dinero_propio:.2f}')
    print(f'Se le pedirá al banco {prestamo_banco:.2f}')
    print(f'El crédito de la fábrica es de {credito_fabrica:.2f}')
