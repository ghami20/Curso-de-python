

from tkinter import *

app = Tk()
app.title("Aplicacion grafica en python")
etiqueta = Label(app, text="Hola mundo!!!")
boton = Button(app, text="OK!!")

etiqueta.pack()
boton.pack()
app.mainloop() 