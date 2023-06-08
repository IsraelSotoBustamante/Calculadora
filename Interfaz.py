"Practica 2, Intefaz Grafica"
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def ventanaCapturaDatos():
    """
    Abre una ventana para capturar datos de entrada del usuario.

    Returns:
        str: El texto introducido por el usuario.
    """
    def devolverDatos():
        """
        Función que se ejecuta al hacer clic en el botón "Aceptar".
        Obtiene el texto introducido por el usuario y cierra la ventana.
        """
        textoCaja = entryTexto.get()
        texto.set(textoCaja)
        root.destroy()

    root = Tk()
    root.title("Entrada de datos")

    miFrame = Frame(root)
    miFrame.pack()

    texto = StringVar()

    entryTexto = Entry(miFrame, justify=CENTER, textvariable=texto)
    entryTexto.grid(row=0, column=0, padx=5, pady=5)

    botonAceptar = Button(miFrame, text="Aceptar", command=lambda: devolverDatos())
    botonAceptar.grid(row=1, column=0, sticky="e", padx=5, pady=5)

    root.mainloop()

    return texto.get()

print("Llamamos a la ventana de entrada de datos")
texto = ventanaCapturaDatos()
print("El texto que has introducido es:")
print(texto)
