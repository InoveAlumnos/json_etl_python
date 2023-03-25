# Ejercicios de práctica [Python]
A esta altura del curso el alumno posee ya una serie de habilidades muy vinculadas entre si las cuales son:
- Análisis, filtrado y trabajo de información.
- Capacidad para utilizar formatos de datos de transacciones, APIs, Apps.
- Poder mostrar los resultados en un gráfico y generar un reporte o un trablero de control.

EL propósito de este ejercicio es que el alumno ponga a prueba estas facultades ya que este momento del curso es un momento bisagra, lo próximo que se verá de aquí en más son herramientas o procesos para mejorar estos 3 pilares (bases de datos, exponer una API, generar reportes web).

# HackerRank [Python]
Esta página posee ejercicios para poner a prueba a los programadores, muy utilizada en el ámbito profesional para evaluar posibles candidatos. En esta oportunidad hemos agarrado un ejercicio interesante de esta plataforma y almodado un poco para utilizar como ejercicio en esta oportunidad.

# Enunciado
El objetivo es consumir los datos que provee la siguiente URL:\
https://jsonmock.hackerrank.com/api/transactions/search?txnType=debit&page=1

Notar que al final de la URL aparece "__page=1__", en realidad esta URL admite que sea recorrida de la "__page=1__" hasta la page "__page=16__" ya que los datos están divididos en 16 consultas.\
En cada consulta recibiran datos como el siguiente (un extracto de ellos):

```
{
 "page":"1",
 "per_page":10,
 "total":155,
 "total_pages":16,
 "data":[{
          "id":1,
          "userId":1,
          "userName":"John Oliver",
          "timestamp":1549536882071,
          "txnType":"debit",
          "amount":"$1,670.57",
          "location":{
                      "id":7,
                      "address":"770, Deepends, Stockton Street","city":"Ripley",
                      "zipCode":44139
                      },
          "ip":"212.215.115.165"
         },
         {
          "id":2,
          "userId":2,
          #.....
         }
         #.....
        ]
}
```

Lo que nos interesa de estos datos son el "__userId__", el consumo realizado en la variable "__amount__" y el location "__location__".

## Primera etapa, el consumo de datos (fetch)
Deben usar el módulo request como se vió en clase para consumir la URL provista en el enunciado. Recordar que la URL puede tener hasta 16 páginas, por lo que cuando realicen el request deben construir el string según la página que desean leer, un ejemplo para ello:
```
url = https://jsonmock.hackerrank.com/api/transactions/search?txnType=debit&page={}.format(page_number)
```
Deben crear una función llamada "fetch" que reciba como parámetro el número de la página que desean leer y el "location_id".\
```
dataset = fetch(page_number, location_id)
```
La función fetch debe leer la página deseada y filtrar la información que les llega utilizando comprension de listas, ya que el dataset que retorna fetch debe ser aquellos "__userId__" cuyo "__location['id']__" coincida con el pasado como parámetro a la función.\
El dataset que retorna fetch debe ser una lista de diccionarios con la siguiente información por cada JSON:
```
{"userId": ..., "amount": ...}
```
dataset es una lista que contiene una fila como la anterior mostrada por cada conjunto de JSON que lea. Ejemplo: supongamos que el JSON que recibieron del request es (a modo de ejemplo resumido):\
```
{
 "page":"5",
 "data":[{
          "userId":3,
          "amount":"$1,670.57",
          "location":{
                      "id":7,
                      },
         },
         {
          "userId":1,
          "amount":"$1,250.00",
          "location":{
                      "id":7,
                      },
         },
         {
          "userId":3,
          "amount":"$100.00",
          "location":{
                      "id":7,
                      },
         },
         
         #.....
        ]
}
```

Suponiendo que esos son los primeros 3 JSON contenidos en mi "data" retornado por request, donde en los 3 casos el location['id'] =7, si yo estaba buscando location_id = 7 mis primeras 3 filas de mi dataset serán:
```
{"userId": 3, "amount": "$1,670.57"}
{"userId": 1, "amount": "$1,250.00"}
{"userId": 3, "amount": "$100.00"}
```

## Transformación de la información (transform)
Se debe realizar una función que reciba como parámetro el dataset creado en el punto anterior y transforme ese dataset (lista de diccionarios) en una lista con datos consolidados. Este función recibe como parámetro el dataset y retorna una lista "data":
```
data = transform(dataset)
```

La función transform realiza la contabilidad de cuanto monto total en débito realizó cada usuario (userID) en total. Por ejemplo, en el caso anterior donde nuestro dataset comenzaba con:

```
{"userId": 3, "amount": "$1,670.57"}
{"userId": 1, "amount": "$1,250.00"}
{"userId": 3, "amount": "$100.00"}
```

Si nuestro dataset solo tuviera esas 3 filas, debo sumar los dos débitos que realizó userID (consolidarlo) y mi lista final debe ser algo como la siguiente:
```
[
[3, 1770.57] # 1770.57 = 1670.57 + 100
[1, 1250]
]
```

La lista que retorna "transform" como resultado es una lista de listas, en donde cada fila es la consolidación del débito de cada usuario. Difucultades para superar en este punto:
- Los números están en texto y comienza con "$" y tienen puntos y comas, antes de poder sumarlos deben convertirlos a float con la siguiente línea:
```
amount = float(re.sub(r'[^\d\-.]', '', amount_str))  # amount_str es el valor en string con el $ tomado del dataset
```
- Deben poder consolidar la suma de cada usuario pero de buenas a primeras no saben cuantos usuarios existen o cuantos habrán. Les dejamos para que piensen como resolver esta problemática.

## Reporte (report)
Una vez que "transform" les haya transformado los datos en una lista de "[usuario, debito_total]", deben crear una función "report" que reciba como parámetro esos datos:
```
report(data)
```
Dentro de "report" deben utilizar comprension de listas para obtener una lista que represente a los valores de "X" como el ID de cada usuario, y una comprensión de listas que represente a los valores de "Y" como el valor de debito_total de cada uno:
```
X = [ ... for x in data]
Y = [ ... for x in data]
```

Graficar los valores "X" e "Y" con el gráfico que más les parezca que puede representar que usuario ha realizado más consumo en débitos.

## Esquema del ejercicio
Deben crear su archivo de python y crear las funciones mencionadas en este documento. Deben crear la sección "if _name_ == "_main_" y ahí crear el flujo de prueba de este programa:
```
if __name__ == "__main__":
    dataset = fetch(page_number, location_id)
    data = transform(dataset)
    report(data)

```


