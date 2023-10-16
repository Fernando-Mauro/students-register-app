import tkinter as tk
from tkinter import ttk
from screeninfo import get_monitors
from time import strftime
import requests
import json

# Función para agregar una nueva fila
def agregar_fila(event=None):  # Cambio en la firma de la función para aceptar el argumento event
    matricula = entrada.get()
    hora_actual = strftime("%H:%M:%S")
    
    # Realizar una solicitud HTTP para obtener el nombre del estudiante
    url = f'http://127.0.0.1:8000/api/v1/students/{matricula}'
    response = requests.get(url)
    data = response.json()[0]
    if response.status_code == 200:
        nombre = data['name']
        phone = data['phone']
    else:
        nombre = 'Desconocido'
    entrada.delete(0, "end")
    register_check =f'http://127.0.0.1:8000/api/v1/students/{matricula}/register_check'
    response = requests.get(register_check)
    datacheck = response.json()
    print(datacheck)
    type_check = datacheck['template']
    lista_registros.insert("", "end", values=(matricula, nombre, hora_actual, phone, type_check))
    entrada.focus_set()  # Hacer foco en el campo de entrada después de agregar una fila

# Crear una ventana
ventana = tk.Tk()
ventana.title("Escáner de Registros")

monitores = get_monitors()

if monitores:
    monitor = monitores[0]
    ventana.geometry(f"{monitor.width}x{monitor.height}")

# Crear un marco para la grilla
marco_grilla = ttk.Frame(ventana)
marco_grilla.pack(expand=True, fill="both")

# Configurar la geometría de la grilla
marco_grilla.grid_rowconfigure(0, weight=0)
marco_grilla.grid_columnconfigure(0, weight=1)
marco_grilla.grid_columnconfigure(1, weight=1)
marco_grilla.grid_columnconfigure(2, weight=1)

# Crear un estilo para los encabezados
columna_estilo = ttk.Style()
columna_estilo.configure("Encabezado.TLabel", foreground="black", font=("Arial", 12), anchor="center")
columna_estilo.configure("Celda.TLabel", borderwidth=2, relief="solid")

# Crear una grilla para mostrar los registros
lista_registros = ttk.Treeview(marco_grilla, columns=("Matrícula", "Nombre", "Hora", "Telefono", "Tipo"), show="headings")
lista_registros.grid(row=1, column=0, columnspan=3, sticky="nsew")
lista_registros.heading("Matrícula", text="Matrícula")
lista_registros.heading("Nombre", text="Nombre")
lista_registros.heading("Hora", text="Hora")
lista_registros.heading("Telefono", text="Telefono")
lista_registros.heading("Tipo", text="Tipo")
lista_registros.column("Matrícula", anchor="center")
lista_registros.column("Nombre", anchor="center")
lista_registros.column("Hora", anchor="center")
lista_registros.column("Telefono", anchor="center")
lista_registros.column("Tipo", anchor="center")
lista_registros.configure(style="Celda.TLabel")

# Crear un campo de entrada
entrada = tk.Entry(marco_grilla, font=("Arial", 12), bg="red")
entrada.grid(row=2, column=2, sticky="nsew", padx=5, pady=5)

# Configurar la geometría de la entrada
marco_grilla.grid_rowconfigure(1, weight=1)
marco_grilla.grid_rowconfigure(2, weight=0)
marco_grilla.grid_columnconfigure(2, weight=1)

# Configurar una función para agregar registros cuando se presiona Enter
entrada.bind("<Return>", agregar_fila)

# Hacer foco en el campo de entrada al iniciar la aplicación
entrada.focus_set()

# Iniciar la ventana
ventana.mainloop()