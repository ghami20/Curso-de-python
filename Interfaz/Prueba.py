
def validar(nota):
    print("Entra a la funcion validar nota")
    if nota>0 and nota<=10:
        return True
    else:
        print("nota invalida")
        return False
    
def ValidarAprobado(nota):
    print("Entra a la funcion validar aprobado")
    if nota >4: 
        return True
    else: 
        return False
def ValidarAsist(asistencia):
    print("Entra a la funcion validar asistencia")
    if asistencia>80:
        return True
    else: 
        return False


nota = int(input("Ingrese nota: "));

asistencia= int(input("Ingrese el promedio de asistencia: "));

    
if(validar(nota) and ValidarAsist(asistencia) and ValidarAprobado(nota) ):
    print("Terminó el curso!")
else: 
    print("No aprobo el curso")