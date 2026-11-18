contador_est = 0
acumulado_notas = 0
total_aprobados = 0
total_reprobados = 0
cantidad_estudiantes = int(input("Digite el numero de estudiantes a evaluar: "))
while contador_est < cantidad_estudiantes:
    calificacion = float(input("Digite la nota del estudiante: "))
    if calificacion < 0 or calificacion > 5.0:
        print("Nota no valida")
    else:
        if calificacion >= 3.0:
            print("Aprobado")
            total_aprobados = total_aprobados + 1
        else:
            print("Reprobado")
            total_reprobados = total_reprobados + 1
    contador_est = contador_est + 1
    acumulado_notas = acumulado_notas + calificacion
media_general = acumulado_notas / cantidad_estudiantes
print("El numero de estudiantes evaluados fueron:", cantidad_estudiantes)
print("Aprobados:", total_aprobados)
print("Reprobados:", total_reprobados)
print("Promedio:", media_general)
