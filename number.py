import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.datasets import load_digits

dataDg = load_digits()
# print(dataDg)
# print(dir(dataDg))
#Input Number as you want !
y = str(input('Masukkan Nomor : '))
for i in range(len(y)):
    plt.subplot(1, len(y), i+1)
    plt.imshow(dataDg['images'][int(y[i])])
    plt.title('ini : {}'.format(dataDg['target'][int(y[i])]))
plt.show()
