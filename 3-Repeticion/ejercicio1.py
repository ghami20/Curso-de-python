distancia=int(input("Cual es la distacia de ida? "));
tiempoestancia=int(input("cuantos dias se va a quedar? "));
distancia=distancia*2
preciobillete=distancia*3.70

if distancia >800 and tiempoestancia>7:
    print ("se aplica el descuento!!")
    preciobillete=preciobillete*0.70
else:
    print("no se aplica descuento D:")

print("el precio del billete es: ", preciobillete)