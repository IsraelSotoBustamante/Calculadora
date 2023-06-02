from tkinter import *
from math import *

ventana=Tk()
ventana.geometry("392x600")

#Dimensiones
ancho_boton=11
alto_boton=3

class ventana:
    def __init__(self, master):
        self.master = master

        master.title("Calculadora Simple")

        #Botones
Boton0=Button(ventana,text="0",width=ancho_boton,height=alto_boton).place(x=17,y=180)
Boton1=Button(ventana,text="1",width=ancho_boton,height=alto_boton).place(x=107,y=180)
Boton2=Button(ventana,text="2",width=ancho_boton,height=alto_boton).place(x=197,y=180)
Boton3=Button(ventana,text="3",width=ancho_boton,height=alto_boton).place(x=287,y=180)
Boton4=Button(ventana,text="4",width=ancho_boton,height=alto_boton).place(x=17,y=240)
Boton5=Button(ventana,text="5",width=ancho_boton,height=alto_boton).place(x=107,y=240)
Boton6=Button(ventana,text="6",width=ancho_boton,height=alto_boton).place(x=197,y=240)
Boton7=Button(ventana,text="7",width=ancho_boton,height=alto_boton).place(x=287,y=240)
Boton8=Button(ventana,text="8",width=ancho_boton,height=alto_boton).place(x=17,y=300)
Boton9=Button(ventana,text="9",width=ancho_boton,height=alto_boton).place(x=287,y=300)
BotonS=Button(ventana,text="+",width=ancho_boton,height=alto_boton).place(x=17,y=360)
BotonR=Button(ventana,text="-",width=ancho_boton,height=alto_boton).place(x=107,y=360)
BotonM=Button(ventana,text="*",width=ancho_boton,height=alto_boton).place(x=197,y=360)
BotonD=Button(ventana,text="/",width=ancho_boton,height=alto_boton).place(x=287,y=360)

Salida=Entry(ventana,font=('arial',20,'bold'),width=22,bd=20,insertwidth=4,bg="powder blue",justify="right").place(x=10, y=60)
        
root = Tk()
miVentana = ventana(root)
root.mainloop()
