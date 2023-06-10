# classifier.py
# Lin Li/26-dec-2021
#
# Use the skeleton below for the classifier and insert your code here.

import numpy as np

class Classifier:
    def __init__(self):
        pass
    
    def reset(self):
        self.x_train = None;
        self.y_train = None;
    
    def fit(self, data, target):
        # reshape the data from a 1D array to a 2D array
        reshaped_data = []
        data, reshaped_data = np.array(data), np.array(reshaped_data)
        reshaped_data = data.reshape(-1, 1)
        #initialise the data and targets datasets
        self.x_train = data;
        self.y_train = target;

    def predict(self, data, legal = None):
        # reshape the data from a 1D array to a 2D array
        data = np.array(data)
        data = data.reshape(1, -1)
        
        # calculatet he euclidena distance from the new data point to each other data points in the dataset.
        eu_distances = [np.sqrt(np.sum((data - x_feature)**2)) for x_feature in self.x_train]
        
        # find the N nearest neighbors to the new datapoint
        # N = 12 currently
        k_index = np.argsort(eu_distances)[:12]
        k_predictions = [self.y_train[i] for i in k_index]
        # find the result that is most common
        prediction = max(set(k_predictions), key=k_predictions.count)
        return prediction