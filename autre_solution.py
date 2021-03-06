# -*- coding: utf-8 -*-
"""Autre_Solution

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qmiDnT1AaVhqII7lVrv-_LWbO2dlX9vZ

Nouvelle méthode d'approximation d'une fonction 2D f:x->cos(2*x)+4
via un réseaux de neurone utilisation du package sklearn vs keras
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split

"""Package importés ok
Génération des données à étudier pour l'approximation de la fonction f
"""

np.random.seed(3)
n = 2000
x = np.random.uniform(0, 10, size = n)
y = 2*np.cos(x) + 4
X = np.reshape(x ,[n, 1]) 
y = np.reshape(y ,[n ,])
X_train, X_test, y_train, y_test = train_test_split(X, y,random_state=1)

regr = MLPRegressor(random_state=1, max_iter=500).fit(X_train, y_train)
pred_y_1=regr.predict(X_test)
len(pred_y_1)

"""Learning the neural network regressor"""

clf = MLPRegressor(alpha=0.1, hidden_layer_sizes = (12,), max_iter = 50000, 
                 activation = 'logistic', verbose = 'True', learning_rate = 'adaptive')
a = clf.fit(X, y)

"""Réseau de neuronnes à 10 noeuds perte de précision assez environ 0.2915"""

x_ = np.linspace(0, 20, 160) # define axis

pred_x = np.reshape(x_, [160, 1]) # [160, ] -> [160, 1]
print(len(x_))
print(len(pred_x))
#y_=[2*np.cos(i)+4 for i in x]
pred_y = clf.predict(pred_x) # predict network output given x_
fig = plt.figure() 
plt.plot(x_, 2*np.cos(x_)+4, color = 'b') # plot original function
plt.plot(x_, pred_y, '-') # plot network output