import tkinter as tk
from tkinter import ttk
from screeninfo import get_monitors
from time import strftime

def agregar_registro():
    texto = entrada.get()
    if texto:
        hora_actual = strftime("%H:%M:%S")  # Obtiene la hora actual en formato HH:MM:SS
        lista_registros.insert(0, (texto, "", hora_actual))  # Agrega una tupla con matrícula, nombre (en blanco) y hora
        entrada.delete(0, "end")

# Crear una ventana
ventana = tk.Tk()
ventana.title("Escáner de Registros")

monitores = get_monitors()

if monitores:
    monitor = monitores[0]  # Tomamos el primer monitor, puedes ajustar esto según tus necesidades
    ventana.geometry(f"{monitor.width}x{monitor.height}")

# Crear un marco para los encabezados
marco_encabezados = tk.Frame(ventana)
marco_encabezados.grid(row=0, column=0, columnspan=3, sticky="nsew")

# Etiquetas para las columnas (Matrícula, Nombre, Hora)
tk.Label(marco_encabezados, text="Matrícula").grid(row=0, column=0)
tk.Label(marco_encabezados, text="Nombre").grid(row=0, column=1)
tk.Label(marco_encabezados, text="Hora").grid(row=0, column=2)

# Configurar la geometría de la ventana
ventana.grid_rowconfigure(0, weight=1)  # Fila para la lista de registros
ventana.grid_rowconfigure(1, weight=0)  # Fila para el campo de entrada
ventana.grid_columnconfigure(0, weight=1)  # Columna 0 (Matrícula)
ventana.grid_columnconfigure(1, weight=1)  # Columna 1 (Nombre)
ventana.grid_columnconfigure(2, weight=1)  # Columna 2 (Hora)

# Crear una lista para mostrar los registros
lista_registros = tk.Listbox(ventana, selectmode=tk.SINGLE, borderwidth=2, relief="solid")
lista_registros.grid(row=1, column=0, columnspan=3, sticky="nsew")
lista_registros.config(height=20)  # Altura de la lista de registros (en píxeles)

# Crear un campo de entrada
entrada = tk.Entry(ventana, font=("Arial", 16))  # Puedes ajustar la fuente y el tamaño
entrada.grid(row=2, column=0, columnspan=3, sticky="nsew")

# Configurar la cantidad de filas que abarca el campo de entrada en la cuadrícula
ventana.grid_rowconfigure(2, weight=0)  # Fila 2 (campo de entrada)

# Configurar una función para agregar registros cuando se presiona Enter
entrada.bind("<Return>", lambda event: agregar_registro())

# Iniciar la ventana
ventana.mainloop()
