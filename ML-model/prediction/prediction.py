import joblib
import numpy as np

class Prediction:

    def __init__(self):
        #TODO: replace this with actual request
        # Define the batch size (this replaces None for now)
        batch_size = 1  # or any other size you need

        # Create a random array of shape (batch_size, 300, 6) with values between -1 and 1
        self.testData = np.random.uniform(-0.02, 0.02, size=(batch_size, 300, 6))

    def predict(self):
        model = joblib.load('C:/Users/elisa/source/repos/HAR-API/ML-model/model.pkl')
        y_pred = model.predict(self.testData)

        classes_names = ['Stand', 'Sit', 'Talk-sit', 'Talk-stand','Stand-sit', 'Lay', 'Lay-stand',
            'Pick', 'Jump', 'Push-up', 'Sit-up', 'Walk', 'Walk backward',
            'Walk-circle', 'Run', 'Stair-up', 'Stair-down', 'Table-tennis']
        activityPredictions = [classes_names[i] for i in np.argmax(y_pred, axis=1)]
        most_likely_predictions = [(classes_names[np.argmax(pred)], np.max(pred)) for pred in y_pred]
        # Use np.unique to get unique elements and their counts
        unique_classes, counts = np.unique(activityPredictions, return_counts=True)

        # Find the index of the most common class
        most_common_index = np.argmax(counts)
        activityPrediction = unique_classes[most_common_index]

        print("Predicted activity:")
        print(activityPrediction)
        print(most_likely_predictions)