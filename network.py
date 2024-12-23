# Хочу читать текст через нейросеть

from keras.src.layers import *
from keras.src.models import *
from keras.src.datasets import *

file = open(r"C:\Users\tyuti\IdeaProjects\Gutenberg\Ramanyana.txt", "r")

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

model = Sequential()

model.add(Flatten(input_shape=(28, 28)))
model.add(Dense(512, activation='relu'))
model.add(Dense(10, activation='sigmoid'))

model.summary()

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=5)
