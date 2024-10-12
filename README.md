# HAR-API

## Goal

Turn the model created here: https://github.com/elisakaisa/HumanActivityRecognition into an API.
The ML model should be in Python, and the API in .NET. This is because I am most confortable with machine learning in Python and with backend logic in .NET. The idea is to have some kind of a microservice-like architecture. 

## Project setup
### ML-model
Based on model used in [this project](https://github.com/elisakaisa/HumanActivityRecognition)
Folder ML-model contains the machine learning model in python. No train - test datasplit in this repo when training the model as this was done in the other repo, used the full dataset here to train the model.

### Running the project
#### To create the model: 
1. Donwload data from https://data.mendeley.com/datasets/45f952y38r/5, and save it into `/data/`
2. Set up venv
3. Add .env file in `HAR-API/ML-model` with the following values and replacing filepath with the correct path (double backslash is needed on windows)
```
MODEL_FILEPATH=<filepath>\\HAR-API\\ML-model\\model.pkl
DATA_FILEPATH=<filepath>\HAR-API\\ML-model\\data\\KU-HAR_time_domain_subsamples_20750x300.csv
```
4. Run `py -m train`
5. The model is saved into the `model.pkl` file

ML-model uses Python 3.12 as per tensorflow requirements as of 2024-10-10.

#### To predict an activity:
The model uses a 3 second batch of data (at a sampling frequency of 100Hz, this means 300 rows of data) with acceleration in all 3 directions and gyroscope in all 3 directions. The shape of the input is thus (300, 6). The model returns the predicted activity out of 10 (['Stand', 'Sit','Talk-sit', 'Talk-stand','Stand-sit', 'Lay', 'Lay-stand', 'Pick', 'Jump', 'Push-up', 'Sit-up', 'Walk', 'Walk backward', 'Walk-circle', 'Run', 'Stair-up', 'Stair-down', 'Table-tennis']) with the highest accuracy and its accuracy with the following dto
```python
class PredictionDto:
    activity: str
    accuracy: int
```

1. Create the model following the steps above
2. Have own data ready of the shape described above, or use the following method to create a fake dataset, the values should be between -1 and 1, but are typically a lot smaller (for walking / standing for instance):
```python
# Define the batch size
batch_size = 1  #want to have whole 3sec data batch classified as one activity
# Create a random array of shape (batch_size, 300, 6) with values between -1 and 1
testData = np.random.uniform(-1, 1, size=(batch_size, 300, 6))
```
3. Run `py -m predict`

## ActivityAPI
### Setup
API in ASP.NET, made in .net core 8.
### Running the api
1. run `dotnet run --launch-profile https` in a terminal
2. if a NET:ERR_CERT_INVALID error appears (typically on Chrome), just make sure the page is selected (click anywhere on the screen), and just type `thisisunsafe`. This bypasses the browser's requirement of valid certficates, and should only be used for own sites running in the local network.
3. navigate to `https://localhost:<port>/swagger`