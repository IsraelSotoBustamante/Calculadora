"Practica 1,Botones"

from tkinter import Button, Label, Tk

class VentanaEjemplo:
    def __init__(self, master):
        """
        Clase que define una ventana de ejemplo con una interfaz gráfica simple.

        Args:
            master (Tk): El objeto raíz Tkinter.

        Atributos:
            master (Tk): El objeto raíz Tkinter.
            etiqueta (Label): Etiqueta de texto en la ventana.
            botonSaludo (Button): Botón para saludar.
            botonCerrar (Button): Botón para cerrar la ventana.
        """
        self.master = master

        master.title("Una simple interfaz gráfica")

        self.etiqueta = Label(master, text="Esta es la primera ventana!")
        self.etiqueta.pack()

        self.botonSaludo = Button(master, text="Saludar", command=self.saludar)
        self.botonSaludo.pack()

        self.botonCerrar = Button(master, text="Cerrar", command=master.quit)
        self.botonCerrar.pack()

    def saludar(self):
        """
        Método que se ejecuta al hacer clic en el botón "Saludar".
        Imprime un saludo por la consola.
        """
        print("¡Buen día!")

root = Tk()
miVentana = VentanaEjemplo(root)
root.mainloop()
