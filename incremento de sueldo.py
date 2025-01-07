#Defina un algoritmo que permita calcular el nuevo salario de un trabajador si a este le incrementaron su sueldo x % adicional a su sueldo anterior.

# Entrada de datos
salario_actual = float(input("Digite el salario actual del trabajador: "))
porcentaje_incremento = float(input("Digite el porcentaje que desea incrementar: "))

# Calculo de datos
monto_incremento = salario_actual * (porcentaje_incremento / 100)
nuevo_sueldo = monto_incremento + salario_actual

# Mostrar Resultados
print(f"\nEl incremento salarial es de: {monto_incremento:.2f}")
print(f"El nuevo salario es de: {nuevo_sueldo:.2f}")