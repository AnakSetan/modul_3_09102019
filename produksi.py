import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#load sklearn dataset
dataCH = fetch_california_housing()
dfCH = pd.DataFrame(
    dataCH['data'],
    columns = dataCH['feature_names']
)
dfCH['Price'] = dataCH['target']

#Split datasets : 90% training + 10% testing
x = dfCH[['MedInc','HouseAge','AveRooms','AveBedrms','Population','AveOccup','Latitude','Longitude']]
y = dfCH['Price']
x_train, x_test,y_train,y_test = train_test_split(x,y,test_size = .1)

#linear reg model
model = LinearRegression()
print(model.fit(x_train,y_train))

#Prediction
print(model.predict([x_test.iloc[0]]))

#score accuracy
print(model.score(x_train,y_train)*100,'%')
print(model.score(x_test,y_test)*100, '%')

#save Model Machine Learning : Pickle
# import pickle
# with open('modelPickle.pkl', 'wb') as modelku:
#     pickle.dump(model,modelku)
print(x_test.iloc[0])
print(model.predict([x_test.iloc[0]]))
print(model.predict([[
    2.852900,35.000000,4.933180,1.009217,1053.000000,2.426267, 40.770000,-124.160000
]]))

#--------------------------------------Bentuk JobLIB
# import joblib
# joblib.dump(model,'modelJoblib')