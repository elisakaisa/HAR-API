import pandas as pd

class PrepareData:

    def __init__(self):
        i = 1

    def prepare_data(self):
        self.read_files()


    def read_files(self):
        # name columns of the dataframe
        column_names = []
        for i in range(300):
            name = 'ax_' + str(i) 
            column_names.append(name)
        for i in range(300):
            name = 'ay_' + str(i)
            column_names.append(name)
            
        for i in range(300):
            name = 'az_' + str(i)
            column_names.append(name)
            
        for i in range(300):
            name = 'gx_' + str(i)
            column_names.append(name)

        for i in range(300):
            name = 'gy_' + str(i)
            column_names.append(name)
            
        for i in range(300):
            name = 'gz_' + str(i)
            column_names.append(name)

        column_names.append('class')
        column_names.append('length')
        column_names.append('serial number')

        #TODO: deal with filePath in nice way
        filePath = 'C:/Users/elisa/source/repos/HAR-API/ML-model/data/KU-HAR_time_domain_subsamples_20750x300.csv'
            
        df = pd.read_csv(filePath,  header = None, names = column_names)
        print(df.info)
        return df