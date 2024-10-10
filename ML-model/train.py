import os

from model.readData import PrepareData
from model.buildModel import BuildModel

def program():

    if os.getenv('VIRTUAL_ENV'):
        print('Using Virtualenv')
        print("___________________________")
        print("Train model")
        prepareData = PrepareData()
        samples_per_class = prepareData.prepare_data()
        buildModel = BuildModel(samples_per_class)
        buildModel.build_model()
        

    else:
        print("____________________________________________")
        print('Dumbass, you forgot to venv/Scripts/activate')
        print("____________________________________________")


if __name__ == "__main__":
    program()