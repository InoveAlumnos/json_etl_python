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


from datetime import datetime


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #
    print('# ---- Ejemplo con datetime ---- #')

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

    print("terminamos")
