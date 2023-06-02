from tkinter import *

def ventanaCapturaDatos( ):

    def devolverDatos():

        textoCaja=entryTexto.get()
        texto.set(textoCaja)
        root.destroy()


    root=Tk()
    root.title("Calculadora simple")

    miFrame=Frame(root)
    miFrame.pack()
    
    texto=float()

    entryTexto=Entry(miFrame, justify=CENTER ,textvariable=texto)
    entryTexto.grid(row=0, column=0, padx=5, pady=5)

    botonAceptar=Button(miFrame, text="Aceptar", command=lambda:devolverDatos())
    botonAceptar.grid(row=1, column=0, sticky="e", padx=5, pady=5)

    root.mainloop()

    return texto.get()

print("Llamamos a la ventana de entrada de datos")

texto=ventanaCapturaDatos()

print("El texto que has introducido es:")
print(texto)