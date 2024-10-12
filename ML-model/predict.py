import os

from prediction.prediction import Prediction

def program():

    if os.getenv('VIRTUAL_ENV'):
        print('Using Virtualenv')
        print("___________________________")
        print("Predict model")

        # removes tensorflow warning
        os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'


        Prediction().predict()
        
        

    else:
        print("____________________________________________")
        print('Dumbass, you forgot to venv/Scripts/activate')
        print("____________________________________________")


if __name__ == "__main__":
    program()