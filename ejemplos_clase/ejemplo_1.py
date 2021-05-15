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


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #
    print('# ---- Ejemplos con JSON ---- #')
    json_create()
    json_serialize()
    json_deserialize()

    print("terminamos")
