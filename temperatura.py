print("=== Conversor de Temperatura ===")
print("1. Celsius a Fahrenheit")
print("2. Fahrenheit a Celsius")
print("3. Salir")

opcion = int(input("Selecciona una opción (1-3): "))

if opcion == 1:
    celsius = float(input("Introduce temperatura en °C: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")
elif opcion == 2:
    fahrenheit = float(input("Introduce temperatura en °F: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F = {celsius:.2f}°C")
elif opcion == 3:
    print("Saliendo del programa...")
else:
    print("Opción inválida. Intenta de nuevo.")
