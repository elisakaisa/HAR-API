# HAR-API

## Goal

Turn the model created here: https://github.com/elisakaisa/HumanActivityRecognition into an API.
The ML model should be in Python, and the API in .NET. This is because I am most confortable with machine learning in Python and with backend logic in .NET. The idea is to have some kind of a microservice-like architecture. The python part of the project should ciommunicate though gRPC with the C# part.

## Project setup
### ML-model
Based on model used in [this project](https://github.com/elisakaisa/HumanActivityRecognition)
Folder ML-model contains the machine learning model in python. No train - test datasplit in this repo when training the model as this was done in the other repo, used the full dataset here to train the model.

### Python server
Communicates with C# API though gRPC. Uses an API- key as authentication method. This api key can be added in .env file. This simple API key setup mimics a real-life API key setup, although a token or allowing only IP addresses of .NET API would be more secure.

#### gRPC communication
The request message should be an array of float32 serialized into bytes. The data used has 6 decimals, and a float32 provides the fastest alternative without dataloss.
The response is a dto called PredictionDto, containing the activity as a string, and the accuracy as a float32.

### Running the project(s)
For running all of the parts of the python project, one should be in the folder `ML-model` and not i the root folder.

#### To create the model: 
1. Donwload data from https://data.mendeley.com/datasets/45f952y38r/5, and save it into `/data/`
2. Set up venv
3. Add filepaths in .env file in `HAR-API/ML-model` with a similar setup as instructed further below
4. Run `py -m train`
5. The model is saved into the `model.pkl` file

ML-model uses Python 3.12 as per tensorflow requirements as of 2024-10-10.

#### To predict an activity:
The model uses a 3 second batch of data (at a sampling frequency of 100Hz, this means 300 rows of data) with acceleration in all 3 directions and gyroscope in all 3 directions. The shape of the input is thus (300, 6). The model returns the predicted activity out of 10 (['Stand', 'Sit','Talk-sit', 'Talk-stand','Stand-sit', 'Lay', 'Lay-stand', 'Pick', 'Jump', 'Push-up', 'Sit-up', 'Walk', 'Walk backward', 'Walk-circle', 'Run', 'Stair-up', 'Stair-down', 'Table-tennis']) with the highest accuracy and its accuracy with the following dto
```python
class PredictionDto:
    activity: str
    accuracy: float
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

#### Run the gRPC server
Uses the packages `grpcio` and `grpcio-tools`.
1. Run `py server.py`
2. The server can be easily tested out running `py testclient.py` simultaneously (not updated since API key was instroduced, use .NET API)

If the `activityPredictor.proto` file is modified, the following command should be run the regenerate the pb2_grpcs and pb2 files in the python project:
```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. activityPredictor.proto
```
A similar command should be run to regenerate the corresponding C# files as well. The filepaths may have to be updated in both cases.
```
protoc -I=. --csharp_out=. --grpc_out=. --plugin=protoc-gen-grpc=grpc_csharp_plugin activityPredictor.proto
```

## ActivityAPI
### Setup
API in ASP.NET, made in .net core 8.
### Running the api
1. run `dotnet run --launch-profile https` in a terminal (not from root folder but in `ActivityApi`)
2. if a NET:ERR_CERT_INVALID error appears (typically on Chrome), just make sure the page is selected (click anywhere on the screen), and just type `thisisunsafe`. This bypasses the browser's requirement of valid certficates, and should only be used for own sites running in the local network.
3. navigate to `https://localhost:<port>/swagger`

## .env file setup
Located in `ML-model\`
On windows, double backslash is needed for filepaths
```
MODEL_FILEPATH=<filepath>\\HAR-API\\ML-model\\model.pkl
DATA_FILEPATH=<filepath>\HAR-API\\ML-model\\data\\KU-HAR_time_domain_subsamples_20750x300.csv
API_KEY=<apikey>
```


## Next steps
- run python server in docker
- actually pass a file instead of random just before GET method
- add authorization / authentication in API (simple setup done for gRPC communication)
- error handling
- unit tests
- improvements on ML model


wiueghfiuwheiofudjoq9ij3eixdhbw3ui4ztg oisdjfgoiwjrsbdfiuwhoir