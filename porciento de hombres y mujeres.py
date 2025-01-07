#En un salon de clase nos pide diseñar un algoritmo que permita determinar el porcentaje de varones y el porcentaje de mujeres
#Cantidad de Niños 78 - Niñas 43.//

# Entrada de datos: Cantidad de niños y niñas
niños = float(input("Introduce la cantidad de Niños "))
niñas = float(input("Introduce la cantidad de Niñas "))

# Calcular el total de alumnos
total = niños + niñas

# Calcular el porcentaje de niños y niñas
porcen_niños = (niños / total) * 100
porcen_niñas = (niñas / total) * 100

# Mostrar los resultados
print(f"\nEl total de alumnos es: {total:.0f}")
print(f"El porcentaje de Niños es: {porcen_niños:.2f}%")
print(f"El porcentaje de Niñas es: {porcen_niñas:.2f}%")

