m3=int(input("Cual es la cantidad de m3 consumidos? "));
extra=0
total_pagar=15.80
if m3 <= 150:
    print("Debe abonar $15.80")
else :
    extra= m3-150
    total_pagar=total_pagar+extra*1.50
    print("Debe abonar extra: ", extra, "\n y su total a pagar es: ", total_pagar)
    
    