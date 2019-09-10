# Flask w/ model Machine Learning --------------------------------------06/09/2019

import pandas as pd
import numpy as np
from flask import Flask, request, render_template,jsonify
import joblib
import requests
# import json

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home_1.html')

@app.route('/ml')
def ml():
    medinc = 4.240700
    houseage = 40
    averooms = 5.694362
    avebedrms = 1.032641
    population = 1851
    aveoccup = 2.746291
    latitude = 34.16
    longitude = -117.99
    hasil = modelLoad.predict([[
        medinc,houseage, averooms,avebedrms,population,aveoccup,latitude,longitude
]])[0]
    return str(hasil)

@app.route('/predict', methods = ['GET','POST'])
def predict ():
    if request.method == 'POST':
        body = request.json
        #8 variable
        medinc = body ['medinc']
        houseage = body ['houseage']
        averooms = body ['averooms']
        avebedrms = body ['avebedrms']
        population = body ['population']
        aveoccup = body ['aveoccup']
        latitude = body ['latitude']
        longitude = body ['longitude']
        #model prediction
        hasil = modelLoad.predict([[
            medinc,houseage,averooms,avebedrms,population,
            aveoccup,latitude,longitude
        ]])[0]
        return jsonify({
            'medinc' : str(body ['medinc']),
            'houseage' : str(body ['houseage']),
            'averooms' : str(body ['averooms']),
            'avebedrms' : str(body ['avebedrms']),
            'population' : str(body ['population']),
            'aveoccup' : str(body ['aveoccup']),
            'latitude' : str(body ['latitude']),
            'longitude' : str(body ['longitude']),
            'prediksi' : hasil,
            'status' : 'Anda nge-POST'
        })
    elif request.method == 'GET':
        return jsonify({
            'status':'Anda nge-GET'
        })
    else :
        return jsonify({
            'status':'ANDA NGAPAIN ?'
        })
#------------------
@app.route('/predictform', methods = ['POST','GET'])
def predictform():
    if request.method == 'POST':
        result = request.form
        print(result)
    return 'OK OC'
if __name__ == '__main__':
    modelLoad = joblib.load('modeljoblib')
    app.run(debug=True )