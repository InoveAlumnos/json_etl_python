#!/usr/bin/env python
'''
JSON ETL [Python]
Ejemplos de clase
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para mostrar ejemplos prácticos de los visto durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.3"

import json
import requests
from datetime import datetime

import matplotlib.pyplot as plt
import matplotlib.axes


def json_create():
    # Ejemplos de como se construyen los JSON
    max_json = {
              "nombre": "Max",
              "apellido": "Power",
              "hijos": [
                    {
                     "firstName": "Alice",
                     "age": 6
                    },
                    {
                     "firstName": "Bob",
                     "age": 8
                    }
                    ]
              }

    emma_json = {
                 "nombre": "Emma",
                 "apellido": "Thompson",
                 "hijos": []
                 }

    json_test = {"max": max_json, "emma": emma_json}

    print('Imprimir json como un objeto')
    print(emma_json)

    print('Convertir JSON a json_string e imprimir en pantalla')
    json_string = json.dumps(emma_json, indent=4)
    print(json_string)

    print('Imprimir json como un objeto')
    print(json_test)

    print('Convertir JSON a json_string e imprimir en pantalla')
    json_string = json.dumps(json_test, indent=4)
    print(json_string)


def json_serialize():
    # Generar un json y almacenarlo en archivo (dump)

    estudiante1 = {
                  "nombre": "Max",
                  "apellido": "Power",
                  "materias": [
                      {
                       "asignatura": "matematica",
                       "estado": "en curso"
                      },
                      {
                       "asignatura": "lengua",
                       "estado": "finalizado"
                      }
                      ]
                   }

    with open('mi_json.json', 'w') as jsonfile:
        data = [estudiante1]
        json.dump(data, jsonfile, indent=4)


def json_deserialize():
    # Leer json y actualizarlo
    estudiante2 = {
                  "nombre": "Jean",
                  "apellido": "Gray",
                  "materias": [
                      {
                       "asignatura": "matematica",
                       "estado": "finalizado"
                      },
                      {
                       "asignatura": "lengua",
                       "estado": "finalizado"
                      }
                      ]
                   }

    with open('mi_json.json', 'r') as jsonfile:
        current_data = json.load(jsonfile)
        current_data.append(estudiante2)

    with open('mi_json.json', 'w') as jsonfile:
        json.dump(current_data, jsonfile, indent=4)

    with open('mi_json.json', 'r') as jsonfile:
        json_data = json.load(jsonfile)

    print('Mostrar el contenido del archivo mi_json')
    print(json.dumps(json_data, indent=4))


def json_request():
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    # Se puede obtener el objeto JSON de dos formas distintas
    data = json.loads(response.text)
    data = response.json()
    print('Imprimir los datos traídos de la nube')
    print(json.dumps(data, indent=4))

    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    data = response.json()

    for user in data:
        if user['userId'] > 2:
            # No mostrar más de 2 usuarios
            # para no ocupar toda la pantalla con mensajes
            break
        print('El usuario {} completó {}? {}'.format(user['userId'],
                                                      user['title'],
                                                      user['completed']
                                                      ))


def fetch_data():
    url = 'http://inove.pythonanywhere.com/finanzas'
    response = requests.get(url)
    dataset = response.json()

    # Del dataset solo me quedo con la columna de los minutos.
    # y el precio de cierre de la acción.
    # Filtro aquellas filas que no posean precio.
    filter_data1 = [{'time_str': x['minute'], 'price': x['close']} for x in dataset if x.get('close') is not None]

    # El tiempo está en formato texto, utilizo los métodos de datetime para
    # pasarlos a objectos tipo datetime

    filter_data2 = [{'time': datetime.strptime(x['time_str'], '%H:%M'),
                     'price': x['price']
                     }
                    for x in filter_data1
                    ]

    list_first_time = filter_data2[0]['time']

    filter_data3 = [{'x': ((x['time'] - list_first_time).seconds / 60),
                     'y': x['price']
                     }
                    for x in filter_data2
                    ]
    return filter_data3


def plot_xy(dataset, title=''):
    x = [data['x'] for data in dataset]
    y = [data['y'] for data in dataset]

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(x, y, c='darkcyan')
    ax.grid()
    ax.set_title(title)
    plt.show()


def ejemplo_completo():
    # Ejemplo de como tomar información de una API
    # Limpiar y generar el set de datos
    # Graficar los resultados
    dataset = fetch_data()
    plot_xy(dataset, 'Acciones Apple')


def ejemplos_datetime():
    # Distintas formas de construir un objeto fecha
    date1 = datetime(year=2019, month=6, day=15, hour=20, minute=45, second=25)
    date2_str = '2019-06-16 20:45:25'
    date2 = datetime.strptime(date2_str, '%Y-%m-%d %H:%M:%S')

    print('Fechas:')
    print(date1.year, date1.month, date1.day)
    print(date2.year, date2.month, date2.day)

    one_day = date2 - date1
    print('Diferencia de días:', one_day.days)
    print('Diferencia de minutos:', one_day.total_seconds() / 60)

    today = datetime.now()
    tomorrow = today + one_day

    tomorrow_str = tomorrow.strftime('%d-%m-%Y | %H:%M')
    print(tomorrow_str)

    date1_seconds = date1.hour*3600 + date1.minute*60 + date1.second
    print('Date1 seconds:', date1_seconds)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #
    # ---- Ejemplos con JSON ---- #
    json_create()
    json_serialize()
    json_deserialize()
    json_request()
    # ---- Ejemplo Integrador ---- #
    ejemplo_completo()
    # ---- Ejemplo con datetime ---- #
    ejemplos_datetime()
