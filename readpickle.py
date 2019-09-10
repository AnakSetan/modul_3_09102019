#load model ML : Pickle

import pickle

with open('modelPickle.pkl','rb') as modelku :
    modelLoad = pickle.load(modelku)
print(modelLoad.predict([[
    2.852900,35.000000,4.933180,1.009217,1053.000000,2.426267, 40.770000,-124.160000
]]))

#load model ML : Joblib
import joblib
modelLoad = joblib.load('modelJoblib')

print(modelLoad.predict([[
    2.852900,35.000000,4.933180,1.009217,1053.000000,2.426267, 40.770000,-124.160000
]]))