total_venta = float(input("Ingrese el total de la venta: "))
tipo_de_venta = input(
    "\nIngrese ingrese el tipo de venta, C (pagos al contado), T (para pagos con Tarjeta)): "
)

if tipo_de_venta == "C":
    total_venta =  total_venta*0.90;
elif tipo_de_venta == "Contado":
    total_venta = total_venta - (total_venta * 10 / 100)
print("\nEl total de la venta es: $", total_venta)