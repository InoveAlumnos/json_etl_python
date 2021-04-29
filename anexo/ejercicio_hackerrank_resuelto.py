import json
import requests
import numpy as np
import re
import matplotlib.pyplot as plt


def fetch(page_number, location_id):
    # Armar la URL de cual cual se descargará datos
    url = "https://jsonmock.hackerrank.com/api/transactions/search?txnType=debit&page={}".format(page_number)

    # Descarggar tdatos
    response = requests.get(url)
    dataset = response.json()
    json_response = dataset["data"]

    # Filtrar aquellos datos que pertenezcan a la location deseada
    filtrado = [{"userId": x["userId"] , "amount": x["amount"]} for x in json_response if x["location"]["id"] == location_id]
    return filtrado


def transform(dataset):
    data = {}

    # Almacenar en un diccionario el acumulado
    # de gastos de cada usuario
    for i in range(len(dataset)):
        variable = dataset[i]
        userid = variable['userId']
        amount_str = variable['amount']
        amount = float(re.sub(r'[^\d\-.]', '', amount_str))

        if (userid in dataset ) == False:
            data[userid] = 0

        data[userid] =  data[userid] + amount

    # Armar la lista de usuarios y debitos
    data_list = [[key, value] for key,value in data.items()]
    return data_list


def report(data):   
    # Bar Plot
    x = [x[0] for x in data]
    y = [x[1] for x in data]

    fig, ax = plt.subplots()
    fig.suptitle('Transactions Filtered by Location')
    x_ticks = np.linspace(1,len(x), len(x))
    ax.bar(x_ticks, y)
    ax.grid(c = 'silver', ls = 'dotted')
    ax.set_facecolor('aliceblue')
    ax.set_ylabel('Debits $')
    ax.set_xlabel('UserId')
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x)
    plt.show()


if __name__ == "__main__":
    page_number = 1
    location_id = 7

    dataset = fetch(page_number, location_id)
    data = transform(dataset)
    report(data)
