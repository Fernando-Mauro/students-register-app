import serial
import time
import os
import requests
import threading
import sys
import re  # Importa el módulo de expresiones regulares.
from dotenv import load_dotenv
load_dotenv()

# Abre el puerto USB. Asegúrate de tener los permisos adecuados.
name = sys.argv[1]
ser = serial.Serial(name)  # El nombre del puerto es dinámico.

# Define una función para enviar la petición de manera asíncrona.
def send_request(enrollment, token):

    url = f'https://phplaravel-1207729-4275370.cloudwaysapps.com/api/v1/students/{enrollment}/register_check'
    print(url)
    headers = {'Authorization': f'Bearer {token}'}
    try:
        requests.get(url, headers=headers)
    except Exception as e:
        print(f"Error al enviar la petición: {e}")

try:
    codigo_qr = ""  # Inicializa la cadena del código QR.
    while True:
        # Lee un byte del puerto USB.
        bytesRead = ser.readline()
        enrollment = bytesRead.decode('utf-8').strip()  # Elimina los espacios en blanco, saltos de línea, etc.
        enrollment = enrollment[:10]  # Toma solo los primeros 10 caracteres.

        # Verifica si el enrollment es válido.
        if not re.match(r'^(?:[0-9]{2}[abAB][0-9]{7,8}|[sS][aA][0-9]{7})$', enrollment):
            continue  # Si no es válido, continúa con la siguiente iteración del ciclo.

        # Obtiene la URL y el token del archivo .env.
        # url = os.getenv('URL')
        token = os.getenv('TOKEN')
        # Envía la petición de manera asíncrona.
        # print(enrollment)
        threading.Thread(target=send_request, args=(enrollment, token)).start()
        
        # time.sleep(0.1)

except KeyboardInterrupt:
    ser.close()
