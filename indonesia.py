import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_excel('indo_12_1.xls',skiprows = 3, skipfooter = 2, na_values=['-'])
df.rename(columns={'Unnamed: 0':'Provinsi'},inplace = True)
# print(df)

df = df.set_index('Provinsi')
df = df.transpose()
# print(df.index)#masih berbentuk object
x = list(df.index)#mengubah bentuk menjadi list
# print(x)
# df1 = pd.DataFrame(x[1:])
df1=pd.DataFrame(x)
df2 = df1.append({0:2050},ignore_index=True)
# print(df1)
model = linear_model.LinearRegression()
model.fit(df1,df['INDONESIA'])
print(model.coef_)
print(model.intercept_)

plt.plot(
    df1,df['INDONESIA'],'r-',
    df2, model.predict(df2),'b--'
)
plt.grid(True)
plt.title('Prediksi Populasi Indonesia s/d Thn. 2050')
plt.xlabel('Tahun')
plt.ylabel('Populasi')
plt.show()