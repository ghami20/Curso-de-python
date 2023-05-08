import sys
from tkinter import *
#Las funcioens se activan en cada boton
def hacer_sumas():
 try:
  valor1 = int(entrada_texto1.get())
  valor2 = int(entrada_texto2.get())
  result = valor1 + valor2
  resultado.config(text=result)
 except ValueError:
  resultado.config(text="Introduce un numero")
def hacer_resta():
 try:
  valor1 = int(entrada_texto1.get())
  valor2 = int(entrada_texto2.get())
  result = valor1 - valor2
  resultado.config(text=result)
 except ValueError:
  resultado.config(text="Introduce un numero")
def hacer_multi():
 try:
  valor1 = int(entrada_texto1.get())
  valor2 = int(entrada_texto2.get())
  result = valor1 * valor2
  resultado.config(text=result)
 except ValueError:
  resultado.config(text="Introduce un numero")
def hacer_divis():
 try:
  valor1 = int(entrada_texto1.get())
  valor2 = int(entrada_texto2.get())
  if valor2!=0:

    result = valor1 / valor2
    resultado.config(text=result)
 except ValueError:
    resultado.config(text="Introduce un numero")

#creo mi pantalla
app = Tk()
app.title("Calculadora simple")

#Ventana Principal
vp = Frame(app)
vp.grid(column=0, row=0, padx=(150,150), pady=(100,100))
vp.columnconfigure(10, weight=10)
vp.rowconfigure(10, weight=10)

resultado = Label(vp, text="Valor")
resultado.grid(column=2, row=4, sticky=(W,E))
#mis botones y sus funciones
boton1 = Button(vp, text="SUMA", command=hacer_sumas)
boton2 = Button(vp, text="RESTA", command=hacer_resta)
boton3 = Button(vp, text="MULTIPLICACIÓN", command=hacer_multi)
boton4 = Button(vp, text="DIVISIÓN", command=hacer_divis)
boton1.grid(column=1, row=1)
boton2.grid(column=1, row=2)
boton3.grid(column=1, row=3)
boton4.grid(column=1, row=4)
valor = ""
#mis inputs los puedo utilizar en las funciones con el mismo nombre.
entrada_texto1 = Entry(vp, width=10, textvariable=valor)
entrada_texto1.grid(column=2, row=1)
entrada_texto2 = Entry(vp, width=10, textvariable=valor)
entrada_texto2.grid(column=2, row=2)


app.mainloop()