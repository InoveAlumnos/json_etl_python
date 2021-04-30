# pip install neurokit2
# https://dominiquemakowski.github.io/post/simulate_ecg/
# https://pypi.org/project/neurokit2/

import neurokit2 as nk
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

data = []

fig = plt.figure()
line, = plt.plot(data)

data = list(nk.ecg_simulate(duration=4, sampling_rate=100, heart_rate=60))
data += list(nk.ecg_simulate(duration=4, sampling_rate=100, heart_rate=60))
data += list(nk.ecg_simulate(duration=4, sampling_rate=100, heart_rate=80))
data += list(nk.ecg_simulate(duration=4, sampling_rate=100, heart_rate=100))
data += list(nk.ecg_simulate(duration=4, sampling_rate=100, heart_rate=60))

count = 0
step = int(len(data) / 10)

def update(frame):
    try:
        i = count*step
    except:
        count = 0
        i = 0
    f = (count+1) * step
    x_data = data[i:f]

    line.set_data(x_data)
    fig.gca().relim()
    fig.gca().autoscale_view()

    count += 1
    return line,

animation = FuncAnimation(fig, update, interval=1000)

plt.show()






#plt.plot(data)
#plt.show()

#nk.signal_plot(simulated_ecg, sampling_rate=200)  # Visualize the signal
