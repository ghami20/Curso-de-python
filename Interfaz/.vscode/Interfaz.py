from tkinter import *

def HacerSuma():
    valor1 = int(entrada1.get())
    valor2 = int(entrada2.get())
    suma=valor1+valor2
    label3.config(text=suma)

app = Tk()
app.config(bg="blue")
app.title("Calculadora")
valor=""
ventana = Frame(app, padx=50, pady=50 , bg="grey")
ventana.grid(column=1, row=1, padx=200, pady=150)
label1 = Label(ventana, text="Primer numero", padx=50, bg="orange").grid(column=0,row=0)
entrada1 = Entry(ventana ,textvariable=valor )
entrada1.grid(column=0,row=1)
label2 = Label(ventana, text="Segundo numero", padx=50, bg="orange").grid(column=1,row=0)
entrada2 = Entry(ventana ,textvariable=valor )
entrada2.grid(column=1,row=1)
boton1 = Button(ventana, command=HacerSuma, text="Suma",padx=20,pady=10, bg="blue",fg="white").grid(column=2,row=0)
label3 = Label(ventana , text="espero un valor")
label3.grid(column=2,row=2)
ventana.mainloop()