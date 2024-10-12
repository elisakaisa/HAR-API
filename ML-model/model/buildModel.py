import sklearn
import numpy as np
from dotenv import load_dotenv
import os

from tensorflow import keras
import joblib

class BuildModel:

    def __init__(self, samples_per_class, X_train, y_train):
        self.weights = []
        self.samples_per_class = samples_per_class
        self.model = []
        self.X_train = X_train
        self.y_train = y_train

    def build_model(self):
        self.compute_weights()
        model = self.create_model()
        self.train_model(model)

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
       
        # Compile model
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        print(model.summary())
        return model
    
    def train_model(self, model):
         # Add early stop to prevent overfitting and save weights
        check = keras.callbacks.ModelCheckpoint('weight3s.keras', save_best_only=True, monitor='val_loss', mode='min')
        earlystopping = keras.callbacks.EarlyStopping(monitor='val_accuracy', patience=20, restore_best_weights = True)

        #TODO: figure out if this is a good add
        #  #Adding loss, optimizer and metrics values to the model.
        # model.compile(  loss='categorical_crossentropy',
        #                 optimizer='Adam',
        #                 metrics=["accuracy"])

        model.fit(self.X_train, self.y_train, batch_size = 32,
                    epochs = 200,
                    verbose = 1,
                    class_weight=self.weights,
                    validation_split = 0.2,
                    callbacks=[check, earlystopping])
        
        # save model by serialization
        load_dotenv()
        joblib.dump(model, os.getenv('MODEL_FILEPATH'))
        print("model successfully saved")