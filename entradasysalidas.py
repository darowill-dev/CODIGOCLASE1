# Entrada de datos
nombre = input("Ingrese el nombre del trabajador: ")
horas_trabajadas = float(input("Ingrese las horas trabajadas en la semana: "))
pago_por_hora = float(input("Ingrese el pago por hora: "))

# Proceso
sueldo_semanal = horas_trabajadas * pago_por_hora

# Salida de datos
print("\n--- Resultado ---")
print(f"Trabajador: {nombre}")
print(f"Horas trabajadas: {horas_trabajadas}")
print(f"Pago por hora: ${pago_por_hora:.2f}")
print(f"Sueldo semanal: ${sueldo_semanal:.2f}")
