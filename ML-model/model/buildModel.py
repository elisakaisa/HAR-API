import sklearn
import numpy as np

from tensorflow import keras

class BuildModel:

    def __init__(self, samples_per_class):
        self.weights = []
        self.samples_per_class = samples_per_class
        self.model = []

    def build_model(self):
        self.compute_weights()
        self.create_model()

    def compute_weights(self):
        self.weights = sklearn.utils.class_weight.compute_class_weight(class_weight = 'balanced', classes = np.unique(self.samples_per_class), y = self.samples_per_class)

        # convert weights to a dictionary
        self.weights = dict(zip(np.unique(self.samples_per_class), self.weights))
        print(self.weights)

    def create_model(self):
        #300 time steps in 3 seconds (100Hz), 6 features
        input_shape = (300, 6)

        model = keras.Sequential()
        model.add(keras.Input(shape=input_shape))
        model.add(keras.layers.Conv1D(filters=64, kernel_size=5, activation='relu'))
        model.add(keras.layers.Dropout(0.5)) # dropout some weights to prevent overfitting
        model.add(keras.layers.MaxPooling1D(pool_size=5))
        model.add(keras.layers.Flatten())
        model.add(keras.layers.Dense(100, activation='relu'))
        model.add(keras.layers.Dense(50, activation='relu'))
        model.add(keras.layers.Dense(18, activation='softmax'))

        # Add early stop to prevent overfitting and save weights
        check = keras.callbacks.ModelCheckpoint('weight3s.keras', save_best_only=True, monitor='val_loss', mode='min')
        earlystopping = keras.callbacks.EarlyStopping(monitor='val_accuracy', patience=20, restore_best_weights = True)

        # Compile model
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        print(model.summary())
        return model
    
