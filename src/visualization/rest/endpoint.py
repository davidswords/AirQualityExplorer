import branca as branca
import folium

from flask import render_template

from src import app
from src.measurement.domain.service import MeasurementService


@app.route("/")
def map():
    start_coords = (62.278600, 12.340200)
    folium_map = folium.Map(location=start_coords, zoom_start=6)
    return render_template("map.html", map=folium_map._repr_html_())


@app.route("/map/<pollutant>", methods=["GET"])
def pollutant_map(pollutant: str):
    # Get measurements for the pollutant
    service = MeasurementService()
    entities = service.retrieve_by_pollutant(pollutant=pollutant)

    # Calculate min and max values for the colormap normalization
    values = []
    for entity in entities:
        if entity.latitude and entity.longitude and entity.value >= 0:
            values.append(entity.value)
    min_value, max_value = min(values), max(values)

    app.logger.info(min_value)
    app.logger.info(max_value)
    app.logger.info(values)

    # Create a colormap for the data
    colormap = branca.colormap.LinearColormap(
        colors=["green", "yellow", "red"], vmin=min_value, vmax=max_value
    ).to_step(5)
    colormap.caption = f"Air quality for {pollutant}"

    # Create a map centered at some location
    m = folium.Map(location=[62.278600, 12.340200], zoom_start=6)

    # Add a marker for each measurement
    for entity in entities:
        if entity.latitude and entity.longitude and entity.value >= 0:
            marker_color = colormap(entity.value)
            folium.CircleMarker(
                location=[entity.latitude, entity.longitude],
                radius=10,
                popup=f"{entity.city}, {entity.country}: {entity.value}",
                color=marker_color,
                fill=True,
                fill_color=marker_color,
            ).add_to(m)

    # Add the colormap to the map
    m.add_child(colormap)

    # Render the map to HTML and return it
    map_html = m._repr_html_()

    return render_template("map.html", map=map_html, pollutant=pollutant)

