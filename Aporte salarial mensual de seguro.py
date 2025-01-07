#Tenemos un trabajador gana S/69.23 al dia, durante 26 dias laborables, nos pide hallar cuanto recibe de sueldo y cuanto se aporta a su seguro pensionario si se sabe que el porcentaje de aporte mensual es el 11.74% el cual esta compuesto por :
		#10% ingresa a su AFP.
		#0.38% es el Cobro por la administracion e inversion de tu fondo.
		#1.36% por Seguro de Invalidez, Sobrevivencia y Gastos de Sepelio.

# Datos proporcionados
dia = 69.23         # Monto que gana el trabajador por día
diala = 26          # Días laborables en el mes
afp = 0.10          # Porcentaje que va a la AFP
sif = 0.0038        # Porcentaje para la administración e inversión del fondo
sisgs = 0.0136      # Porcentaje para el seguro de invalidez, sobrevivencia y gastos de sepelio

# Cálculo del salario mensual
sm = dia * diala


# Cálculo de los aportes al seguro pensionario
aafp = sm * afp         # Aporte a la AFP
asif = sm * sif         # Aporte por administración e inversión
asisgs = sm * sisgs     # Aporte por seguro de invalidez, sobrevivencia y gastos de sepelio

# Cálculo del total aportado al seguro pensionario
ams = aafp + asif + asisgs


# Mostrar los resultados
print(f"\nEl salario mensual que recibe un trabajador es de S/{sm:.2f}")
print(f"Aporta a su seguro pensionario un total de S/{ams:.2f}")
print(f"Ingresa a su AFP un total de S/{aafp:.2f}")
print(f"Seguro por administración e inversión de tu fondo: S/{asif:.2f}")
print(f"Seguro de invalidez, sobrevivencia y gastos de sepelio: S/{asisgs:.2f}")