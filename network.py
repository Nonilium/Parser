import numpy as np
from tensorflow.keras.models import *
from tensorflow.keras.layers import *

from tensorflow.keras.layers import Dense

model = Sequential()

model.add(Dense(1, input_shape=(1,), activation='sigmoid'))
