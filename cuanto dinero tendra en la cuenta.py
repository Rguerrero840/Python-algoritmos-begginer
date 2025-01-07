# Un hombre desea saber cuanto dinero se genera por concepto de intereses en relación a la cantidad que tiene en inversión en el banco.
# El decidirá reinvertir los intereses siempre y cuando estos no excedan a $7000, y en ese caso diseña un algoritmo para saber cuanto dinero tendrá finalmente en su cuenta.


# Entrada de datos
monto_inicial = float(input("Digite la cantidad inicial: "))
tasa_interes = float(input("Tasa de interes: "))

# Calculo de interes
interes_generado = monto_inicial * (tasa_interes / 100)
nuevo_saldo = monto_inicial + interes_generado

if interes_generado <= 7000:
    print(f'Los intereses generados son de {interes_generado:.2f} su nuevo saldo es de {nuevo_saldo:.2f}')