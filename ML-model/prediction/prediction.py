import joblib
import numpy as np
import os
from dotenv import load_dotenv

from dto.predictionDto import PredictionDto

class Prediction:

    def __init__(self):
        #TODO: replace this with actual request
        # Define the batch size (this replaces None for now)
        batch_size = 1  #want to have whole 3sec data batch classified as one activity

        # Create a random array of shape (batch_size, 300, 6) with values between -1 and 1
        self.testData = np.random.uniform(-0.02, 0.02, size=(batch_size, 300, 6))

    def predict(self, data):
        load_dotenv()
        model = joblib.load(os.getenv('MODEL_FILEPATH'))

        # transform obtained data
        dataTransformed = data.reshape(1, 300, 6)
        
        y_pred = model.predict(dataTransformed)

        classes_names = ['Stand', 'Sit', 'Talk-sit', 'Talk-stand','Stand-sit', 'Lay', 'Lay-stand',
            'Pick', 'Jump', 'Push-up', 'Sit-up', 'Walk', 'Walk backward',
            'Walk-circle', 'Run', 'Stair-up', 'Stair-down', 'Table-tennis']

        activityPrediction = classes_names[np.argmax(y_pred)]
        most_likely_predictions = np.max(y_pred)

        prediction = PredictionDto(
            activity=activityPrediction,
            accuracy=most_likely_predictions
        )

        # print("Predicted activity:")
        # print(prediction)

        return prediction