import numpy as np
from keras import *
from keras.src.datasets import *
from keras.src.layers import *
import ascii

print(ascii.file_ascii)

path_abs = r'C:\Users\tyuti\IdeaProjects\Gutenberg\Ramanyana.txt'

(x_train, y_train), (x_test, y_test) = mnist.load_data()
# open(path_abs, 'r')

model = Sequential()

model.add(Dense(units=1, activation='relu'))

model.add(Dense(units=32, activation='relu', input_dim=784))

model.add(Dense(units=10, activation='relu'))


model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10)
