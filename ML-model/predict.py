import os

from prediction.prediction import Prediction

def program():

    if os.getenv('VIRTUAL_ENV'):
        print('Using Virtualenv')
        print("___________________________")
        print("Predict model")
        Prediction().predict()
        
        

    else:
        print("____________________________________________")
        print('Dumbass, you forgot to venv/Scripts/activate')
        print("____________________________________________")


if __name__ == "__main__":
    program()