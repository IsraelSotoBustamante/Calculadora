"Practica 1,Botones"

"Se llama a la biblioteca y las herramientas a utilizar"
from tkinter import Button, Label, Tk

"Se crea la ventana y se le asigna un nombre"
class VentanaEjemplo:
    def __init__(self, master):
        self.master = master

        "Texto de la parte superior de la interfaz"
        master.title("Una simple interfaz gráfica")

        self.etiqueta = Label(master, text="Esta es la primera ventana!")
        self.etiqueta.pack()

        "Botones, se declaran los objetos, se les asigna un texto y un comando a ejecutar"
        self.botonSaludo = Button(master, text="Saludar", command=self.saludar)
        self.botonSaludo.pack()

        self.botonCerrar = Button(master, text="Cerrar", command=master.quit)
        self.botonCerrar.pack()

    def saludar(self):
        print("Buen dia!!")
        
root = Tk()
miVentana = VentanaEjemplo(root)
root.mainloop()
