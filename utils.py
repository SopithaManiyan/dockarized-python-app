#utils.py

'''This is to place utility functions here, 
such as data loading functions or any other helpers that we can add in the future.'''

import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)
