import folium
from flask import Flask, render_template,abort,redirect

app = Flask(__name__)
#page maps
@app.route('/')
def home():
    map = folium.Map(
        location= [-6.302403, 106.652248],
        zoom_start= 15
    )
    folium.Marker(
    [-6.302403, 106.652248],
    popup= '<b>Purwadhika</b>',
    tooltip= 'I am Here !!'
    ).add_to(map)
    map.save('templates/map.html')
    return render_template('home.html')
#page ke dua
@app.route('/map')
def map():  
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True)
