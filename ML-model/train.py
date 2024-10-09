import os

from model.readData import PrepareData

def program():

    if os.getenv('VIRTUAL_ENV'):
        print('Using Virtualenv')
        print("___________________________")
        print("Train model")
        prepareData = PrepareData()
        prepareData.prepare_data()

    else:
        print("____________________________________________")
        print('Dumbass, you forgot to venv/Scripts/activate')
        print("____________________________________________")


if __name__ == "__main__":
    program()