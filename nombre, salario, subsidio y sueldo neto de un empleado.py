# Diseñar un algoritmo que lea el nombre de un empleado, su salario básico por hora, el numero de horas trabajadas en un mes. Nos pide lo siguiente:
# Calcular su salario mensual adicionalmente el subsidio de transporte, si su sueldo es mayor o igual a 2 salarios mínimos legal vigente. 
# Tener en cuenta que el salario mínimo es 930 soles y el subsidio por transporte es 50 soles
# Mostrar: el nombre del empleado, su salario mensual, el subsidio de transporte y su sueldo neto.

# Datos
subsidio = 50
salario_minimo = 930

# Entrada de Datos
nombre_empleado = str(input("Digite el nombre del empleado: "))
hora_salario = float(input("Digite cuanto gana por hora el empleado: "))
horas_trabajas_mes = int(input("Digite las horas trabajadas en el mes del empleado: "))

# Calculos
salario_mes = hora_salario * horas_trabajas_mes

# Mostrar datos
print(f'\nNombre del empleado: {nombre_empleado}')
print(f'Su salario es de: {salario_mes:.2f}')


# Condicion
if salario_mes >= 2 * salario_minimo:
    print(f"El subsidio de transporte es de {subsidio} soles")
    salario_neto = salario_mes + subsidio
    print(f'Su salario neto es de: {salario_neto:.2f}')




