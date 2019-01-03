# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 16:08:12 2019

@author:Naijie Chang
"""

from minisom import MiniSom

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r'F:\xiaoqinghe\dataset4test.csv', delimiter=',', )
data = df[df.columns[1:12]]

# data normalization
data = np.apply_along_axis(lambda x: x/np.linalg.norm(x), 1, data)

# Initialization and training
som = MiniSom(8, 8, input_len=11, sigma=1, learning_rate=0.5, 
              neighborhood_function='triangle', random_seed=10)
#som.random_weights_init(data)
som.pca_weights_init(data)
print("Training...")
som.train_random(data, 4000)  # random training
print("\n...ready!")

plt.figure(figsize=(7, 7))
# Plotting the response for each pattern in the dataset4test dataset
plt.pcolor(som.distance_map().T, cmap='bone_r')  # plotting the distance map as background
plt.colorbar()

#target = np.genfromtxt('dataset4test.csv', delimiter=',', usecols=(4), dtype=str)
#t = np.zeros(len(target), dtype=int)
#t[target == 'setosa'] = 0
#t[target == 'versicolor'] = 1
#t[target == 'virginica'] = 2
#
# use different colors and markers for each label
markers = ['o', 's', 'D']
colors = ['C0', 'C1', 'C2','C3', 'C4', 'C5']
for cnt, xx in enumerate(data):
    w = som.winner(xx)  # getting the winner
    print('w:',w)
    # palce a marker on the winning position for the sample xx
#    plt.plot(w[0]+.5, w[1]+.5, markers[0], markerfacecolor='None',
#             markeredgecolor=colors[t[cnt]], markersize=12, markeredgewidth=2)
plt.axis([0, 7, 0, 7])
#plt.savefig('resulting_images/som_dataset4test.png')
plt.show()
