import pandas as pd
import numpy as np

class PrepareData:

    def __init__(self):
        self.df = []
        self.data = []
        self.data1s = []

    def prepare_data(self):
        self.read_files()
        self.transform_data()
        self.get_samples_per_class()


    def read_files(self):
        # name columns of the dataframe
        # Create column names for multiple prefixes
        prefixes = ['ax', 'ay', 'az', 'gx', 'gy', 'gz']
        column_names = [f"{prefix}_{i}" for prefix in prefixes for i in range(300)]

        # Append additional columns
        column_names += ['class', 'length', 'serial number']

        #TODO: deal with filePath in nice way
        filePath = 'C:/Users/elisa/source/repos/HAR-API/ML-model/data/KU-HAR_time_domain_subsamples_20750x300.csv'
            
        self.df = pd.read_csv(filePath,  header = None, names = column_names)
        print(self.df.info)


    def transform_data(self):
        # Define the column ranges for accelerometer and gyroscope data
        sensors = {'ax': (0, 300), 'ay': (300, 600), 'az': (600, 900),
                'gx': (900, 1200), 'gy': (1200, 1500), 'gz': (1500, 1800)}

        # Extract data for each axis
        data = [self.df.iloc[:, start:end].values for start, end in sensors.values()]

        # Combine the extracted data into a 3D array
        self.data = np.array(data)
        print(self.data.shape)


    def transform_to_one_sec_data(self):
        #TODO: refactor this mess, chose btw 1 sec & 3sec data

        # 1st second
        ax1 = self.df.iloc[:,:100].values
        ay1 = self.df.iloc[:,300:400].values
        az1 = self.df.iloc[:,600:700].values
        
        gx1 = self.df.iloc[:,900:1000].values
        gy1 = self.df.iloc[:,1200:1300].values
        gz1 = self.df.iloc[:,1500:1600].values
        
        # 2nd second
        ax2 = self.df.iloc[:,100:200].values
        ay2 = self.df.iloc[:,400:500].values
        az2 = self.df.iloc[:,700:800].values

        gx2 = self.df.iloc[:,1000:1100].values
        gy2 = self.df.iloc[:,1300:1400].values
        gz2 = self.df.iloc[:,1600:1700].values

        # 3rd second
        ax3 = self.df.iloc[:,200:300].values
        ay3 = self.df.iloc[:,500:600].values
        az3 = self.df.iloc[:,800:900].values

        gx3 = self.df.iloc[:,1100:1200].values
        gy3 = self.df.iloc[:,1400:1500].values
        gz3 = self.df.iloc[:,1700:1800].values

        # combine values
        temp1 = np.array([ax1,ay1,az1,gx1,gy1,gz1])
        temp2 = np.array([ax2,ay2,az2,gx2,gy2,gz2])
        temp3 = np.array([ax3,ay3,az3,gx3,gy3,gz3])
        data1s = np.hstack((temp1, temp2, temp3))
        data1s.shape
        data1s = np.transpose(data1s,(1,2,0))
        data1s.shape



    def get_samples_per_class(self):
        # Count samples per class and convert to NumPy arrays
        class_samples = {}
        class_numpy_arrays = {}

        for class_label in range(18):
            class_samples[class_label] = self.df[self.df['class'] == class_label]
            class_numpy_arrays[class_label] = class_samples[class_label]['class'].to_numpy()

        # Concatenate all NumPy arrays into a single array
        all_together = np.concatenate(list(class_numpy_arrays.values()))

        print(all_together)