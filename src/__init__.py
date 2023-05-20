from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object("src.config")

db = SQLAlchemy(app)

with app.app_context():
    from src.health.rest.endpoint import health
    from src.measurement.rest.endpoint import retrieve_measurement_from_country
    from src.measurement.data.dao import MeasurementDAO

    db.create_all()
