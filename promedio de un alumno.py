#Defina un algoritmo que permita calcular la nota final de un alumno, teniendo en cuenta que ha realizado 3 evaluaciones y que cada evaluacion esta sometida a un peso , el cual es:
		#La primera nota tiene un peso de 25%
		#La segunda nota tiene un peso de 45%
        #La tercera nota tiene un peso de 30%


# Datos
peso_primera_nota = 0.25
peso_segunda_nota = 0.45
peso_tercera_nota = 0.30


# Entrada de datos
periodo_uno = float(input("Digite la nota obtenida en el primer periodo por el estudiante: "))
periodo_dos = float(input("Digite la nota obtenida en el segundo periodo por el estudiante: "))
periodo_tres = float(input("Digite la nota obtenida en el tercer periodo por el estudiante: "))

# Evaluacion de datos
primera_nota = periodo_uno * peso_primera_nota
segunda_nota = periodo_dos * peso_segunda_nota
tercera_nota = periodo_tres * peso_tercera_nota

# Cálculo de la nota final
nota_final = primera_nota + segunda_nota + tercera_nota

# Mostrar Resultados
print(f"La nota final es de: {nota_final:.2f}")