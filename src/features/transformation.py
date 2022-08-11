import numpy as np

from src.data.read_clean_data import mape

y1 = np.array([1,2,3,4,5])
y2 = np.array([2,3,4,5,6])

print(np.round(mape(y1, y2),2))

