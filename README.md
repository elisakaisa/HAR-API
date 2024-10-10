# HAR-API

## Goal

Turn the model created here: https://github.com/elisakaisa/HumanActivityRecognition into an API.
The ML model should be in Python, and the API in .NET. Why? Because I want to.

## Project setup
### ML-model
Based on model used in [this project](https://github.com/elisakaisa/HumanActivityRecognition)
Folder ML-model contains the machine learning model in python. No train - test datasplit in this repo when training the model as this was done in the other repo, using the full dataset here.

To create the model: 
1. Donwload data from https://data.mendeley.com/datasets/45f952y38r/5, and save it into `/data/`
2. Set up venv
3. Run `py train.py` to train the model
4. The model is saved into the `model.pkl` file

ML-model uses Python 3.12 as per tensorflow requirements as of 2024-10-10.
