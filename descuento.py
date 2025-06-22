# Programa que aplica un descuento según la cantidad comprada

cantidad = int(input("Ingrese la cantidad de productos: "))
precio_unitario = 50
total_sin_descuento = cantidad * precio_unitario

if cantidad >= 10:
    descuento = 0.2  # 20% de descuento
elif cantidad >= 5:
    descuento = 0.1  # 10% de descuento
else:
    descuento = 0  # sin descuento

total_con_descuento = total_sin_descuento * (1 - descuento)

print(f"Total sin descuento: ${total_sin_descuento}")
print(f"Descuento aplicado: {descuento*100}%")
print(f"Total a pagar: ${total_con_descuento}")
