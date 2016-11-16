import random
import numpy as np
from matplotlib import pylab as plt
%matplotlib inline

def Markov(text_file, horizon):
    data = []
    for line in open(text_file):
        data.append(line.strip().split())
    data = np.array(data, dtype=float)
#     print (data)

    x_label = np.array(range(0, horizon + 1))
    y_label = []
    y_label.append(1)
    choice = [1,2,3]

    for i in range(1, horizon + 1):
        y_label.append(np.random.choice(choice, replace=False, p=data[y_label[i - 1] - 1]))    
    return y_label

realization = Markov("./markov.txt", 100)
print ('Generated y axis is: ', realization)
plt.xlabel('Xi')
plt.ylabel('realization')
plt.plot(range(0,101), np.array(realization))
plt.show()

# print ('The approximated expectation for "(X0+...+Xn)/n" is: ', np.array(Markov("./markov.txt", 1000)).mean(0))
# new_realization = [i*i*pow(0.9,i) for i in Markov("./markov.txt", 1000)]
# print ('The sum of is: ',sum(np.array(new_realization)))

# single realization
# y_label = Markov("./markov.txt", 1000)
# print ('single realization:', np.array(y_label).mean(0))
# # print (y_label)
# sq = [num*num*pow(0.9,i) for i, num in enumerate(y_label)]
# print (sum(sq))
#
# realization_expectation_1 = []
# realization_expectation_2 = []
# for nums in range(1, 201):
#     y_label = Markov("./markov.txt", 1000)
#     realization_expectation_1.append(np.array(y_label).mean(0))
#     realization_expectation_2.append(sum(num*num*pow(0.9,i) for i,num in enumerate(y_label)))
# print ('expectation_1 is: ', np.array(realization_expectation_1).mean(0))
# print ('expectation_2 is: ', np.array(realization_expectation_2).mean(0))
