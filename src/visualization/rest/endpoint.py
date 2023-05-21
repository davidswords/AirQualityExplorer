import folium

from flask import render_template

from src import app


@app.route('/')
def map():
    start_coords = (62.278600, 12.340200)
    folium_map = folium.Map(location=start_coords, zoom_start=6)
    return render_template('map.html', map=folium_map._repr_html_())
