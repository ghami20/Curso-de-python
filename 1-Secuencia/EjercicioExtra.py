cant= int(input("Ingrese cantidad de cajas: "));
cd= cant*10
total= cant*5.80
print("Total de CDs: ",cd);
print("Total a pagar: $",total);
pago= int(input("Pago con: $"));
vuelto= pago-total
print("El vuelto es: $",vuelto);