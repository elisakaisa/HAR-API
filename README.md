# HAR-API

## Goal

Turn the model created here: https://github.com/elisakaisa/HumanActivityRecognition into an API.
The ML model should be in Python, and the API in .NET. Why? Because I want to.

## Project setup
### ML-model
Based on model used in [this project](https://github.com/elisakaisa/HumanActivityRecognition)
Folder ML-model contains the machine learning model in python. No train - test datasplit in this repo when training the model as this was done in the other repo, used the full dataset here to train the model.

To create the model: 
1. Donwload data from https://data.mendeley.com/datasets/45f952y38r/5, and save it into `/data/`
2. Set up venv
3. Run `py -m train` to train the model or `py -m predict` to predict an activity
4. The model is saved into the `model.pkl` file

ML-model uses Python 3.12 as per tensorflow requirements as of 2024-10-10.

The model uses a 3 second batch of data (at a sampling frequency of 100Hz, this means 300 rows of data) with accelration in all 3 directions and gyroscope in all 3 directions. The shape of the input is thus (300, 6)