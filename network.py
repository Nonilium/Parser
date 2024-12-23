from keras import *
from keras.src.datasets import *
from keras.src.layers import *

path_abs = r'C:\Users\tyuti\IdeaProjects\Gutenberg\Ramanyana.txt'

(x_train, y_train), (x_test, y_test) = mnist.load_data()
# open(path_abs, 'r')

model = Sequential()

model.add(Flatten(input_shape=(28, 28, 1)))

model.add(Dense(units=784, activation='relu'))
model.add(Dense(units=784, activation='relu'))
model.add(Dense(units=784, activation='relu'))

model.add(Dense(units=10))

model.compile(loss="binary_crossentropy",
              optimizer="rmsprop",
              metrics=["accuracy"])

model.fit(x_train,
          y_train,
          epochs=10)

model.save('mnist_model.keras.txt')
