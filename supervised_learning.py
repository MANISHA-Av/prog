import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error,r2_score

boston = load_boston()
#print(boston.data.shape)#(506, 13)
bos = pd.DataFrame(boston.data)
#print(bos.head())
bos.columns = boston.features_names
print(bos)
