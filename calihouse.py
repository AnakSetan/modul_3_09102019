import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split



#-----------------------------------------------------------------
dataCh = fetch_california_housing()
# print(dir(dataCh))
# print(dataCh['feature_names'])
# print(dataCh['data'].shape)
# print(dataCh['feature_names'])
# print(dataCh['target'][0])
#-------------------------------------------------------------------
#Buat Data Frame
dfCh = pd.DataFrame(
    dataCh['data'],
    columns = dataCh['feature_names']
)
# # print(dfCh)
dfCh['Price']=dataCh['target']
# print(dfCh)
# corr = dfCh.corr()
#Buat grafif kolerasi
#--------------------------------------------------------------------
# plt.imshow(dfCh.corr())
# plt.colorbar()
# plt.yticks(np.arange(9),dfCh.columns)
# plt.show()

# Splitting datasets : 90% training + 10% testing
#---------------------------------------------------------------------
# dataCh = fetch_california_housing()

# train_test_split(dataX, dataY, test_size = .1)
x = dfCh[['MedInc','HouseAge','AveRooms','AveBedrms','Population','AveOccup','Latitude','Longitude']]
y = dfCh['Price']
x_train, x_test,y_train,y_test = train_test_split(x,y,test_size = .1)
# print(x_test.iloc[0])
#---------------------------------------------------------------------LINEAR REGRESSION
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train,y_train)
# print(model.predict(x_test))
# print(model.predict([x_test.iloc[0]]))
#---------------------------------------------------------------------SCORE
print(model.score(x_train,y_train)*100, '%') # dalam % x 100
print(model.score(x_test, y_test)*100,'%')