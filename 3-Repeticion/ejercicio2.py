import random
sueldosTotal=int(input("sueldos "))
cont1=0
cont2=0

for i in range(sueldosTotal): 
    sueldo = random.randint(0,100)
    if(sueldo>25 and sueldo<50):
        cont1+=1
    if(sueldo>50 and sueldo<75):
        cont2+=1
    