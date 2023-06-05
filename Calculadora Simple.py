"Practica 3, Calculadora Simple"
import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_add():
    first_number = entry.get()
    global f_num
    global math_operation
    math_operation = "addition"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_subtract():
    first_number = entry.get()
    global f_num
    global math_operation
    math_operation = "subtraction"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_multiply():
    first_number = entry.get()
    global f_num
    global math_operation
    math_operation = "multiplication"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_divide():
    first_number = entry.get()
    global f_num
    global math_operation
    math_operation = "division"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, tk.END)
    if math_operation == "addition":
        entry.insert(tk.END, f_num + float(second_number))
    elif math_operation == "subtraction":
        entry.insert(tk.END, f_num - float(second_number))
    elif math_operation == "multiplication":
        entry.insert(tk.END, f_num * float(second_number))
    elif math_operation == "division":
        if float(second_number) != 0:
            entry.insert(tk.END, f_num / float(second_number))
        else:
            entry.insert(tk.END, "Error: Division by zero")

# Crear la ventana principal
window = tk.Tk()
window.title("Calculadora")

# Crear el campo de entrada
entry = tk.Entry(window, width=35, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Crear los botones numéricos
button_1 = tk.Button(window, text="1", padx=20, pady=10, command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", padx=20, pady=10, command=lambda: button_click(2))
button_3 = tk.Button(window, text="3", padx=20, pady=10, command=lambda: button_click(3))
button_4 = tk.Button(window, text="4", padx=20, pady=10, command=lambda: button_click(4))
button_5 = tk.Button(window, text="5", padx=20, pady=10, command=lambda: button_click(5))
button_6 = tk.Button(window, text="6", padx=20, pady=10, command=lambda: button_click(6))
button_7 = tk.Button(window, text="7", padx=20, pady=10, command=lambda: button_click(7))
button_8 = tk.Button(window, text="8", padx=20, pady=10, command=lambda: button_click(8))
button_9 = tk.Button(window, text="9", padx=20, pady=10, command=lambda: button_click(9))
button_0 = tk.Button(window, text="0", padx=20, pady=10, command=lambda: button_click(0))

# Crear los botones de operaciones
button_add = tk.Button(window, text="+", padx=19, pady=10, command=button_add)
button_subtract = tk.Button(window, text="-", padx=20, pady=10, command=button_subtract)
button_multiply = tk.Button(window, text="*", padx=20, pady=10, command=button_multiply)
button_divide = tk.Button(window, text="/", padx=20, pady=10, command=button_divide)

# Crear el botón igual
button_equal = tk.Button(window, text="=", padx=46, pady=10, command=button_equal)

# Crear el botón de borrado
button_clear = tk.Button(window, text="C", padx=19, pady=10, command=button_clear)

# Ubicar los botones en la ventana
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=0)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

button_equal.grid(row=4, column=1, columnspan=2)
button_clear.grid(row=5, column=0, columnspan=4)

# Iniciar el bucle principal de la aplicación
window.mainloop()
