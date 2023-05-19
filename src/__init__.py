from flask import Flask

app = Flask(__name__)

with app.app_context():
    from src.health.rest.endpoint import health
    from src.measurement.rest.endpoint import retrieve_measurement_from_country
