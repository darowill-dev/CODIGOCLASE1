# Evaluar si un alumno aprueba cada materia y el curso completo

materias = ["Matemáticas", "Física", "Programación"]
aprobadas = 0

for materia in materias:
    calificacion = float(input(f"Ingrese la calificación de {materia}: "))

    if calificacion >= 6:
        print(f"Aprobaste {materia}")
        aprobadas += 1
    else:
        print(f"Reprobaste {materia}")

if aprobadas == 3:
    print("¡Felicidades! Aprobaste todas las materias.")
elif aprobadas == 0:
    print("Reprobaste todas las materias. Necesitas mejorar.")
else:
    print(f"Aprobaste {aprobadas} de 3 materias.")
