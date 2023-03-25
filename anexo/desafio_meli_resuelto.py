import json
from matplotlib import colors

import requests

import matplotlib.pyplot as plt

from requests.api import get

def fetch():
    
    url = 'https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20Mendoza%20&limit=50'
    response = requests.get(url)
    json_response = response.json()

    dataset = [{'price':x.get("price"), 'condition':x.get("condition")} for x in json_response["results"]
                 if x["currency_id"] == "ARS"]
    print(dataset)
    
    return dataset


def transform(dataset, min, max):
    list_min = [x for x in dataset if x["price"] < min]
    list_min_max = [x for x in dataset if x["price"] >= min and x["price"] <= max]
    list_max = [x for x in dataset if x["price"] > max]
    print("Lista por debajo del precio minimo:",list_min)
    print("Lista en rango del precio:",list_min_max)
    print("Lista mayor al precio maxim0:",list_max)
    
    data = {'Menor al precio mínimo':len(list_min),
             'En rango':len(list_min_max), 'Mayor al precio máximo':len(list_max)}
    
    return data


def report(data):
    fig = plt.figure()
    fig.suptitle('RESULTADOS SEGUN PARAMETROS ESCOGIDOS',color="darkblue")
    
    ax = fig.add_subplot()
    ax.set_facecolor("gray")
    explode = (0, 0.1, 0)
    colores = ("royalblue","lime","darkorange")
    ax.pie(data.values(), labels=data.keys(), explode=explode, autopct='%1.1f%%',colors=colores)
    ax.axis('equal')
    plt.show()
    




if __name__ == "__main__":
    
    print('Graficador de resultados de búsqueda')
    
    print('indique precio mínimo')
    min = int(input())
    print('indique precio máximo')
    max = int(input())
    

    dataset = fetch()

    data = transform(dataset, min, max)
    
    report(data)