from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler
from flasgger import Swagger

from src.measurement.rest.spec import definitions

app = Flask(__name__, template_folder="visualization/templates")
app.config.from_object("src.config")
db = SQLAlchemy(app)
swagger = Swagger(
    app,
    template={
        "swagger": "2.0",
        "info": {
            "title": "AirQualityExplorer API",
            "description": " A Flask API for fetching, processing, and visualizing real-time air quality data.",
            "version": "1.0",
        },
        "definitions": definitions,
    },
)

with app.app_context():
    from src.health.rest.endpoint import health
    from src.measurement.rest.endpoint import retrieve_by_pollutant
    from src.measurement.rest.endpoint import retrieve_by_country
    from src.measurement.rest.endpoint import retrieve_by_city
    from src.measurement.data.dao import MeasurementDAO
    from src.measurement.domain.task import ingest_no_open_aq
    from src.measurement.domain.task import ingest_se_open_aq
    from src.measurement.domain.task import ingest_dk_open_aq
    from src.visualization.rest.endpoint import map

    db.create_all()

    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.add_job(
        id="Scheduled Ingestion NO OpenAQ",
        func=ingest_no_open_aq,
        trigger="interval",
        seconds=5,
    )
    scheduler.add_job(
        id="Scheduled Ingestion SE OpenAQ",
        func=ingest_se_open_aq,
        trigger="interval",
        seconds=5,
    )
    scheduler.add_job(
        id="Scheduled Ingestion DK OpenAQ",
        func=ingest_dk_open_aq,
        trigger="interval",
        seconds=5,
    )
    scheduler.start()
