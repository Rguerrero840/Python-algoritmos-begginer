#Un alumno desea saber cual sera su calificacion final en la materia de Matematicas, dicha calificacion se compone por 3 porcentajes,
# a su vez cada porcentaje tiene cierta cantidad de notas, primero diremos los siguiente
	#La nota de los 3 primeros examenes parciales tiene un peso de 55%.
    #La nota del examen final tiene un peso de 30%.
	#La nota del trabajo final tiene un peso de 15%.


# Datos
peso_examenes_parciales = 0.55  # 55% para los tres exámenes parciales
peso_examen_final = 0.30       # 30% para el examen final
peso_trabajo_final = 0.15      # 15% para el trabajo final

# Entrada de datos
nota_primer_examen = float(input("Ingrese la nota obtenida en el primer examen por el estudiante: "))
nota_segundo_examen = float(input("Ingrese la nota obtenida en el segundo examen por el estudiante: "))
nota_tercer_examen = float(input("Ingrese la nota obtenida en el tercer examen por el estudiante: "))
nota_final_examen = float(input("Ingrese la nota obtenida en el examen final por el estudiante: "))
nota_trabajo_final = float(input("Ingrese la nota obtenida en el trabajo final por el estudiante: "))

# Calculo de notas 
calificacion_primer_examen = nota_primer_examen * (peso_examenes_parciales / 3)  # El 55% se divide entre los tres exámenes
calificacion_segundo_examen = nota_segundo_examen * (peso_examenes_parciales / 3)
calificacion_tercer_examen = nota_tercer_examen * (peso_examenes_parciales / 3)
calificacion_final_examen = nota_final_examen * peso_examen_final
calificacion_trabajo_final = nota_trabajo_final * peso_trabajo_final

# Calculo de nota final
nota_final = calificacion_primer_examen + calificacion_segundo_examen + calificacion_tercer_examen + calificacion_final_examen + calificacion_trabajo_final

# Mostrar resultados
print(f"\nLa nota final es de: {nota_final:.2f}")