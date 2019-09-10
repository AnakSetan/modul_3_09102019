from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

gbr = Image.open('it.jpg').convert('L') # RGBA CMYK
# print(np.array(gbr))
arrGbr = np.array(gbr)
print(arrGbr.shape)
# plt.imshow(arrGbr, cmap= 'gray')
# plt.show()
out = Image.fromarray(arrGbr, 'L')
# out.save('it.png')
out.show()