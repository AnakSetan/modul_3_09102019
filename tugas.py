import pandas as pd
import numpy as np
import folium
import json
import requests
from flask import Flask, render_template,redirect,abort

app = Flask(__name__)
#homeeeeee
@app.route('/')
def home ():
    dc = {
        'normal':'grey',
        'bug':'darkgreen',
        'flying':'lightgray',
        'dark':'black',
        'dragon':'beige',
        'grass':'green',
        'electric':'lightgreen',
        'fire':'red',
        'water':'blue',
        'poison':'purple',
        'ghost':'darkpurple',
        'steel':'cadetblue',
        'ground':'lightred',
        'ice':'white',
        'fairy':'pink',
        'psychic':'dark',
        'rock':'orange',
        'fighting':'darkred'
    }
    df = pd.read_csv('pokemon-spawns.csv')
    map = folium.Map(
        location= [df.iloc[0]['lat'],df.iloc[0]['lng']],
        zoom_start= 20
    )
    for i in range(len(df.iloc[100:150])):
        x = str(df.iloc[i]['name']).lower()
        url = f'https://pokeapi.co/api/v2/pokemon/{x}/'
        data = requests.get(url)
        if data.status_code == 200:
            statik= data.json()
            y = statik['sprites']['front_default']
            z = statik['types'][0]['type']['name']
            folium.Marker(
                [(df.iloc[i]['lat']),(df.iloc[i]['lng'])],
                popup= statik['types'][0]['type']['name'],
                tooltip = (f"<img width = 100 height = 100 src = {y}>")+(df.iloc[i]['name']),
                icon=folium.Icon(color=str(dc[z]))
                ).add_to(map)
    map.save('templates/tugas.html')
    return render_template('tugas.html')

if __name__ == '__main__':
    app.run(debug=True)