import pandas as pd
import numpy as np
from sklearn.datasets import fetch_olivetti_faces
import matplotlib.pyplot as plt

#buat data
dataOf = fetch_olivetti_faces()
# print(dir(dataOf))

# print(dataOf['target'])
# print(dataOf.data[0])# 4096
# print(dataOf.images[10].shape) #64 x 64
fig = plt.figure('Wajah Orang ke-0')
# orangke = str(input('Masukkan nomor orang : '))
for i in range(len(orangke)):
    orangke = 3
    plt.subplot(2,len(orangke),i+1)
    plt.imshow(dataOf.images[i + (10 * (orangke-1))], cmap= 'gray')
plt.show()