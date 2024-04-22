#!/bin/bash

# Archivo de Python a ejecutar.
python_file="app.py"

# Busca los dispositivos y los almacena en un array.
devices=($(ls /dev/ttyACM*))

# Cambia los permisos de los dispositivos a 777 y ejecuta el archivo de Python con cada dispositivo como argumento.
for device in ${devices[@]}; do
    sudo chmod 777 "$device"
    python3 "$python_file" "$device" &
done

# Espera a que todos los procesos de Python terminen.
wait
