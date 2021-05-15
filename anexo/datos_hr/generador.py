import sqlite3
from datetime import datetime

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

data = []

fig = plt.figure()
line, = plt.plot(data)

def update(frame):
    now = datetime.now()

    conn = sqlite3.connect('hr_neurokit.db')
    c = conn.cursor()

    slots = [now.second -i for i in reversed(range(5))]
    
    #slots = [now.second -1, now.second]

    for i,slote in enumerate(slots):
        if slote < 0:
            slots[i] += 60
    
    data = []
    for slote in slots:
        c.execute('SELECT * FROM heartrate WHERE time =?', (slote,))
        data_slot = c.fetchall()
        data += data_slot
    
    conn.close()

    x = []
    y = []
    for d in data:
        x.append(d[0] / d[5])
        y.append(d[2])

    line.set_data(x, y)
    fig.gca().relim()
    fig.gca().autoscale_view()

    return line,

animation = FuncAnimation(fig, update, interval=1000)

plt.show()
