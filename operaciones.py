# Programa que simula un menú de operaciones matemáticas

print("Seleccione una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = int(input("Ingrese la opción (1-4): "))
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if opcion == 1:
    resultado = num1 + num2
    print(f"La suma es: {resultado}")
elif opcion == 2:
    resultado = num1 - num2
    print(f"La resta es: {resultado}")
elif opcion == 3:
    resultado = num1 * num2
    print(f"La multiplicación es: {resultado}")
elif opcion == 4:
    if num2 != 0:
        resultado = num1 / num2
        print(f"La división es: {resultado}")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Opción no válida.")
