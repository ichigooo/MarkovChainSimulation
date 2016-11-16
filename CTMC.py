import random
import numpy as np
from matplotlib import pylab as plt
%matplotlib inline

def Markov(text_file, horizon, x0=1):
    time_list = []
    transition_list = []
    transition_list.append(x0)
    data = []
    for line in open(text_file):
        data.append(line.strip().split())
    data = np.array(data, dtype=float)
#     print (data)
    scales = [1, 1/2, 1/3] # for state 1, 2, 3
    time_now = 0
    current_state = x0
    choice = [1,2,3]

    while time_now < horizon:
        # time will be staying in current state
        duration = np.random.exponential(scales[int(current_state - 1)])
        time_now += duration
        time_list.append(duration)
        # duration amount of time has passed
        # and then we need to determine which state it transits to
        current_state = np.random.choice(choice, replace=False, p=data[int(current_state - 1)])
        transition_list.append(current_state)
    transition_list = transition_list[:-1]
    return time_list, transition_list


time_list, transition_list = Markov("./ctmc.txt", 100)
# print (time_list,transition_list)
cumulative_time_list = []
for i, time in enumerate(time_list):
    if i > 0:
        cumulative_time_list.append(cumulative_time_list[i - 1] + time)
    else:
        cumulative_time_list.append(time)
plt.xlabel('Time')
plt.ylabel('State')
plt.plot(cumulative_time_list, transition_list)
plt.show()
