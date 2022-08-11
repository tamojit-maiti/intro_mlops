import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

def mape(y_true: np.array,
        y_pred: np.array):
    """
    Calculates the Mean Absolute Percentage Error of y_pred with respect to y_true
    
    """
    return 100 * np.mean(np.abs(y_true - y_pred)/y_true)