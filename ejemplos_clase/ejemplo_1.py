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

    # Creamos un diccionario
    # con los datos de persona max:
    max_data = {
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

    # Creamos un diccionario
    # con los datos de persona emma:
    emma_data = {
                 "nombre": "Emma",
                 "apellido": "Thompson",
                 "hijos": []
                 }

    print('Imprimir el diccionario de emma')
    print(emma_data)

    # dumps --> 
    #           Dump significa "serializar" o transformar
    #           La "s" de dumps viene de string
    #           Permite convertir un diccionario a JSON String
    
    # Transformar a JSON string con identación 4 (ident=4)
    print('Convertir el dicicionario a JSON string e imprimir en pantalla')
    emma_json_string = json.dumps(emma_data, indent=4)
    print(emma_json_string)

    max_json_string = json.dumps(max_data, indent=4)
    print(max_json_string)

    # Creamos un diccionario que contiene la información
    # de ambas personas en conjunto
    personas = {"max": max_data, "emma": emma_data}

    print('Imprimir el diccionario conjunto de max + emma')
    print(personas)

    print('Convertir el diccionario a JSON string e imprimir en pantalla')
    personas_json_string = json.dumps(personas, indent=4)
    print(personas_json_string)

    # Podemos realizar el proceso inverso
    # A partir de un JSON string podemos crear un diccionario
    # de python para modificarlo / operarlo

    # loads --> 
    #           Load significa "deserializar" o destransformar
    #           La "s" de loads viene de string
    #           Permite convertir un JSON String a diccionario
    print('Convertir un JSON string a diccionario')
    hermano_max = json.loads(max_json_string)

    # Ahora podemos modificar el diccionario del hermano max
    # Por ejemplo, podemos modificar su nombre
    hermano_max["nombre"] = "Luke"

    # Podemos decir que el hermano de max (Luke)
    # no tiene hijos colocando una lista vacia de hijos
    hermano_max["hijos"] = []

    print("terminamos")


def json_serialize():
    # Generar un diccionario y almacenarlo
    # en un archivo JSON (dump)

    estudiante = {
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

    # Para poder almacenar el diccionario en un archivo JSON
    # 1) Primero debemos crear el archivo JSON con open
    # 2) Utilizar dump para indicarle que diccionario (estudiante)
    #    deseamos guardar en nuestra variable archivo (jsonfile)
    with open('estudiante.json', 'w') as jsonfile:
        json.dump(estudiante, jsonfile, indent=4)

    print("terminamos")


def json_deserialize():
    # Leer un archivo JSON y actualizarlo

    # Para poder leer el diccionario en un archivo JSON
    # 1) Primero debemos abrir el archivo JSON con open
    # 2) Utilizar load para indicarle que archivo (jsonfile)
    #    deseamos leer
    with open('estudiante.json', 'r') as jsonfile:
        estudiante = json.load(jsonfile)

    # Ahora todo el contenido del archivo JSON está en "estudiante"
    # Podemos modiicarlo, por ejemplo indicando
    # que ha completado la asignatura de matematica pendiente

    # Para eso tenemos que entender como está armada
    # la estructura de datos del diccionario "estudiante"

    print('Imprimir el diccionario estudiante como un JSON String')
    estudiante_json_string = json.dumps(estudiante, indent=4)
    print(estudiante_json_string)

    # Si deseamos modificar la el estado asignatura metemática
    # debemos acceder a la estructura de datos paso a paso
    # desde lo más afuera del diccionario hasta su interior

    # Obserando el print en consola o 
    # con el debugging podemos ver:
    # 1) Primero debemos acceder a la clave "materias",
    #    Esto nos retorna como "value" una lista de materias
    # 2) Accedemos a la posición "0" de la lista,
    #    que corresponde a la materia "matematica"
    #    Esto nos retorna otro diccionario
    # 3) Accedemos a la calve "estado" para modificar
    #    el valor a finalizado

    estudiante["materias"][0]["estado"] = "finalizado"

    # Ahora que el diccionario estudiante está modificado
    # podemos guardarlo en el mismo archivo de antes


    # Para poder almacenar el diccionario en un archivo JSON
    # 1) Primero debemos crear el archivo JSON con open
    # 2) Utilizar dump para indicarle que diccionario (estudiante)
    #    deseamos guardar en nuestra variable archivo (jsonfile)
    with open('estudiante.json', 'w') as jsonfile:
        json.dump(estudiante, jsonfile, indent=4)

    print("¡Archivo JSON modificado!")
    print("terminamos")



if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #
    print('# ---- Ejemplos con JSON ---- #')
    json_create()
    json_serialize()
    json_deserialize()

    print("terminamos")
