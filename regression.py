import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error

diabetes=datasets.load_diabetes()
#print(diabetes.keys())#dict_keys(['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename'])

#print(diabetes.data)
diabetes_x = np.array([[1],[2],[3]])
#print(diabetes_x)
diabetes_x_train = diabetes_x
diabetes_x_test = diabetes_x

diabetes_y_train = np.array([3,2,4])
diabetes_y_test = np.array([3,2,4])

model = linear_model.LinearRegression()
model.fit(diabetes_x_train,diabetes_y_train)

#draw line by train
diabetes_y_predict=model.predict(diabetes_x_test)
print('mean squared error :',mean_squared_error(diabetes_y_test,diabetes_y_predict))

print('weights:',model.coef_)
print('intercept:',model.intercept_)

plt.scatter(diabetes_x_test,diabetes_y_test)
plt.plot(diabetes_x_test,diabetes_y_predict)
plt.show()



