import numpy as np
from keras import *
from keras.src.datasets import *
from keras.src.layers import *


(x_train, y_train), (x_test, y_test) = open('Ramanyana.txt', 'r')

model = Sequential()

model.add(Dense(1, activation='relu'))

model.add(Dense(32, activation='relu', input_dim=(28, 28, 1)))

model.add(Dense(100, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(100, activation='relu'))

model.compile(loss='mse', optimizer='adam')

model.summary()
