# Ejercicios de práctica [Python]
A esta altura del curso el alumno posee ya una serie de habilidades muy vinculadas entre si las cuales son:
- Análisis, filtrado y trabajo de información.
- Capacidad para utilizar formatos de datos de transacciones, APIs, Apps.
- Poder mostrar los resultados en un gráfico y generar un reporte o un trablero de control.

EL propósito de este ejercicio es que el alumno ponga a prueba estas facultades ya que este momento del curso es un momento bisagra, lo próximo que se verá de aquí en más son herramientas o procesos para mejorar estos 3 pilares (bases de datos, exponer una API, generar reportes web).

# MELI API [Python]
Haremos uso de la API pública de mercadolibre para analizar alquileres y departamentos, muy similar a lo que ya estuvieron practicando pero dándole el enfoque de una problemática real.

# Enunciado
El objetivo es consumir los datos que provee la siguiente URL:\
url = 'https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20Mendoza%20&limit=50'

Notar que en el medio de la URL se está especificando que queremos obtener los Departamentos y Alquileres en la Ciudad de "__Mendoza__". Esto pueden modificarlo para jugar y obtener diferentes resultados.

Cuando realicen encuestas a esta URL recibiran un JSON como el siguiente

```
{
  "site_id": "MLA",
  "query": "Departamentos Alquilers Mendoza ",
  "paging": {},
  "results": [
    {},
    {},
    {},
    {},
    {},
    ...
}
```

Lo que nos interesa son los datos que se encuentran dentro de la lista de "__results__". Para poder acceder a esos datos deberan primero realizar el request de la misma forma que se realizó en clase, y luego con el JSON que obtenemos del request, encontraremos la lista de deparamentos y alquileres dentro de:
```
json_response["results"]
```
En "results" tendrá una lista de diccionarios donde cada fila contiene los datos de un departamento, esa lista la pueden iterar para recorrer los resultados obtenidos de la API. Recomendamos primero chusmear la URL en su explorador web.

## Primera etapa, el consumo de datos (fetch)
Deben usar el módulo request como se vió en clase para consumir la URL provista en el enunciado. Deben crear una función llamada "fetch" que por ahora no recibirá ningún parámetro pero deberá devolver el dataset de datos.
```
dataset = fetch()
```
La función "fetch" debe leer la lista de departamentos/alquileres y filtrar aquellas publicaciones cuyo "__"currency_id"__" no esté en pesos "ARS". Deben utilizar comprension de listas para poder hacer el filtrado de la lista de alquileres en una nueva en donde solo haya alquileres en pesos.\
El dataset que retorna "fetch" debe ser una lista de diccionarios con la siguiente información por cada alquiler:
```
{"price": ..., "condition": ...}
```
dataset es una lista que contiene una fila como la anterior mostrada por cada departamento en alquiler que estuviea en pesos.\
En el dataset solos nos interesa que almacenen el precio de cada departamento y la condición (si es nuevo o usado o no especificado).\
Recomendamos ejecutar en su explorador la URL y investigar por su cuenta los datos en cada fila de "results" para entender como se llamanan las "keys" y los tipos de "values" que posee cada una.

Ejemplo de como se irá construyendo nuestro dataset
```
{"price": 1250, "condition": "used"}
{"price": 3100, "condition": "not_specified"}
{"price": 2500, "condition": "not_specified"}
```

## Transformación de la información (transform)
Se debe realizar una función que reciba como parámetro el dataset creado en el punto anterior y transforme ese dataset (lista de diccionarios) en una lista con datos consolidados. Esta función recibe como parámetro el dataset y retorne una listas. Además recibe como parámetro un rango de precio "min" y "max" en pesos:
```
data = transform(dataset, min, max)
```

La función "transform" recibe un rango de precio mínimo "min" y máximo "max" en pesos. El objetivo es recibir el dataset y partirlo en tres listas distintas utilizando comprensión de listas:
- Se debe crear una lista que solo tenga aquellos departamentos del dataset que los precios estén por debajo del parámetro "min".
- Se debe crear una lista que solo tenga aquellos departamentos del dataset que los precios estén entre el parámetro "min" y el parámetro "max".
- Se debe crear una lista que solo tenga aquellos departamentos del dataset que los precios estén por arriba del parámetro "max".

Una vez que esten formadas las tres listas, se debe contar cuantos elementos hay en cada una. Se debe retornar una lista que contenga estos valores calculados (la cantidad de elementos en cada lista):
```
return [min_count, min_max_count, max_count]
```

## Reporte (report)
Una vez que "transform" les haya transformado los datos y retornado cuantos alquileres hay dentro de cada rango, se debe realizar un gráfico de torta que nos de la idea de como se reparten los precios de los alquileres según los parámetros "min" y "max" que usted haya propuesto. El gráfico se debe realizar por la función "report" que recibe como parámetro la lista "data" que retorna "transform"
```
report(data)
```

## Esquema del ejercicio
Deben crear su archivo de python y crear las funciones mencionadas en este documento. Deben crear la sección "if _name_ == "_main_" y ahí crear el flujo de prueba de este programa:
```
if __name__ == "__main__":
    min = ....
    max = ....

    dataset = fetch()
    data = transform(dataset, min, max)
    report(data)

```

## Para jugar
Cuando finalicen el ejercicio pueden realizar las siguientes modificaciones:
- Que la función fetch reciba por parámetro la ciudad que se desea buscar en la URL.
- Jugar con algunos datos extra que hay en el JSON como la cantidad de ambients, y realizar gráficos o comparaciones (sean creativos ^_^).

