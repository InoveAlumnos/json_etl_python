#!/usr/bin/env python
'''
JSON ETL [Python]
Ejemplos de clase
---------------------------
Autor: Inove Coding School
Version: 2.0

Descripcion:
Programa creado para mostrar ejemplos prácticos de los visto durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "2.0"

import json
import requests

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def extract(url):
    # Extraer el JSON de la URL pasada
    # como parámetro
    response = requests.get(url)
    data = response.json()
    return data


def transform(data):
    # Transformar los datos en dos vectores
    # para graficar
    x = [d['time'] for d in data]
    y = [d['signal'] for d in data]
    return x, y


def load(x ,y):
    # El código a continuación es especial
    # para animaciones de gráficos de línea
    line.set_data(x, y)
    fig.gca().relim()
    fig.gca().autoscale_view()
    return line,


def update_animation(frame):
    # Leer la data del sensor en la nube
    url = 'http://inove.pythonanywhere.com/monitor/sensor'
    data = extract(url)

    # Transformar la información para graficar
    x, y = transform(data)

    # Graficar la anumación
    return load(x, y)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #
    print('# ---- Ejemplos con JSON ETL ---- #')

    # Crear el gráfico
    data = []

    fig = plt.figure()
    line, = plt.plot(data)

    # Graficar
    animation = FuncAnimation(fig, update_animation, interval=1000)
    plt.show()

    print("terminamos")
