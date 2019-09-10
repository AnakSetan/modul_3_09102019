import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_lfw_people

dataP = fetch_lfw_people(min_faces_per_person=3, resize=4)
# print(dir(dataP))
# print(dataP['target'][0])
# plt.imshow(dataP['images'][1])
for i in range(10):
    plt.subplot(2,5,i+1)
    plt.imshow(dataP['images'][i], cmap= 'gray')
    plt.title(dataP['target_names'][dataP['target'][i]])
plt.show()