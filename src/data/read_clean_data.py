import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

def read_raw_data():
    pass

def mape(y_true: np.array,
        y_pred: np.array):
    """
    Calculates the Mean Absolute Percentage Error of y_pred with respect to y_true
    
    """
    return 100 * np.mean(np.abs(y_true - y_pred)/y_true)

def mae(y_true: np.array,
        y_pred: np.array):
    """
    Calculates the Mean Absolute Error of y_pred with respect to y_true
    
    """
    assert np.shape(y_pred) == np.shape(y_true), 'the shapes of the two arrays must be the same'
    return np.mean(np.abs(y_true - y_pred))