puntaje = 0

pregunta1 = input("¿Cuál es la raíz cuadrada de 144? ")
# si se cumple la primer condición o la segunda, es valido
if pregunta1 == "12" or pregunta1.lower() == "doce":
    puntaje += 1
    print("Bien")
else:
    print("Error")
pregunta2 = input("\n¿Quién fundó Buenos Aires? ")
if pregunta2.lower() == "juan de garay"  or pregunta2.lower() == "mendoza" :
    puntaje += 1
    print("Bien")
else:
    print("Error")
pregunta3 = input("\n¿Cuál es la capital de Francia? ")
if pregunta3.lower() == "paris":
    puntaje += 1
else:
    print("Mal");

print("Respuestas correctas: ",puntaje)