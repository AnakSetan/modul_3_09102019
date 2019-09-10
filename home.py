import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import seaborn as sb

df = pd.read_csv('housing.csv', index_col=False)
# print(df)
df = df.fillna(method='ffill')
corr = df.corr()
print(corr)
#yang tidak mendekati 100% ialah : Housing median age, median income, latitude
# sb.heatmap(corr)
model = linear_model.LinearRegression()
model.fit(df[['longitude','latitude','housing_median_age','total_rooms','total_bedrooms','population','households','median_income','median_house_value']], df['median_house_value'])
print(model.coef_)
print(model.intercept_)
#---------------------------
plt.subplot(3,2,1)
plt.scatter(
    df['total_rooms'],df['median_house_value']
)
plt.xlabel('Total Rooms')
plt.ylabel('Median House Value')
plt.title('Total Rooms vs Median House Value')
# plt.legend()
# plt.show()
#---------------------------
plt.subplot(3,2,2)
plt.scatter(
    df['population'],df['median_house_value']
)
plt.xlabel('Population')
plt.ylabel('Median House Value')
plt.title('Population vs Median House Value')
#---------------------------
plt.subplot(3,2,3)
plt.scatter(
    df['median_income'],df['median_house_value']
)
plt.xlabel('Median Income')
plt.ylabel('Median House Value')
plt.title('Median Income vs Median House Value')
#---------------------------
plt.subplot(3,2,4)
plt.scatter(
    df['total_bedrooms'],df['median_house_value']
)
plt.xlabel('Total Bedrooms')
plt.ylabel('Median House Value')
plt.title('Total Bedrooms vs Median House Value')
#--------------------------
plt.subplot(3,2,5)
plt.scatter(
    df['households'],df['median_house_value']
)
plt.xlabel('Households')
plt.ylabel('Median House Value')
plt.title('Households vs Median House Value')
#-------------------------
plt.subplot(3,2,6)
plt.scatter(
    df['longitude'],df['median_house_value']
)
plt.xlabel('Longitude')
plt.ylabel('Median House Value')
plt.title('Longitude vs Median House Value')
plt.show()