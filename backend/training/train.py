import tensorflow as tf

from tensorflow.keras import datasets, layers, models
import numpy as np

import matplotlib.pyplot as plt

import os

trainDir = '/media/cnie109/Backup Plus/HeatCheckImages-Full-cut-small-labeled'

trainingData, validationData = tf.keras.preprocessing.image_dataset_from_directory(
    trainDir,
    image_size = (128,128),
    labels = 'inferred',
    label_mode = 'categorical',
    shuffle = True,
    seed = 41,
    validation_split=0.1,
    subset = 'both'
)

input_shape = (128, 128, 3)

model = tf.keras.models.Sequential([
                                    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape = input_shape),
                                    tf.keras.layers.MaxPool2D(2,2),

                                    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
                                    tf.keras.layers.MaxPool2D(2,2),

                                    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
                                    tf.keras.layers.MaxPool2D(2,2),

                                    tf.keras.layers.Flatten(),
                                    tf.keras.layers.Dense(128, activation='relu'),
                                    tf.keras.layers.Dense(len(trainingData.class_names), activation='softmax')
])


model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(trainingData, batch_size=64, epochs=3, validation_data=validationData)

model.save("heatcheck-dense-tmp.keras")

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.show()

# model.fit(x_train, y_train, batch_size=64, epochs=5,)