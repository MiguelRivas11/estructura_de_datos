import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

# Crear la ventana principal
# root = tk.Tk()
# root.withdraw()  # Oculta la ventana principal

# Solicitar una entrada al usuario
messagebox.showwarning("Info","Proporcione los siguentes datos del libro")
nombre= simpledialog.askstring("Nombre","")
id= simpledialog.askinteger("ID:","")
precio= simpledialog.askfloat("Precio:","")
envio= simpledialog.askstring("Envio","(true/false)")
messagebox.showwarning("Datos",f"el nombre del libro es {nombre}\n id {id}\n precio {precio}\n envio {envio} ")



# if(num1 > num2):
#   messagebox.showwarning("Resultado",f"el numero {num1} es mayor")
# else:
#   messagebox.showwarning("resultado",f"el numero { num2} es mayor")


