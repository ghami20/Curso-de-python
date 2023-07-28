from tkinter import *


def asignar_valor1():     
    valor= int(entrada_texto1.get())*1.15;
    resultado.config(text=valor)
def asignar_valor2(): 
   valor = int(entrada_texto1.get())*1.10;
   resultado.config(text=valor)
def asignar_valor3(): 
    valor= int(entrada_texto1.get())*1.05;
    resultado.config(text=valor)

#creo mi pantalla
app = Tk()
app.title("Primer programa con GUI ")

#Ventana Principal
vp = Frame(app)
vp.grid(column=2, row=2, padx=(150,150), pady=(100,100))
vp.columnconfigure(10, weight=10)
vp.rowconfigure(10, weight=10)

resultado = Label(vp, text="Ingrese sueldo")
resultado.grid(column=2, row=1, sticky=(W,E))
#mis botones y sus funciones
valor =  "Su sueldo es"
boton1 = Button(vp, text="Categoria A", command=asignar_valor1)
boton2 = Button(vp, text="Categoria B",command=asignar_valor2 )
boton3 = Button(vp, text="Categoria C", command=asignar_valor3)
boton1.grid(column=1, row=1)
boton2.grid(column=1, row=2)
boton3.grid(column=1, row=3)

#mis inputs los puedo utilizar en las funciones con el mismo nombre.
entrada_texto1 = Entry(vp, width=10, textvariable=valor)
entrada_texto1.grid(column=2, row=2)
app.mainloop()