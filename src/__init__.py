from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler

app = Flask(__name__)
app.config.from_object("src.config")
db = SQLAlchemy(app)

with app.app_context():
    from src.health.rest.endpoint import health
    from src.measurement.rest.endpoint import retrieve_by_pollutant
    from src.measurement.rest.endpoint import retrieve_by_country
    from src.measurement.data.dao import MeasurementDAO
    from src.measurement.domain.task import ingest_no_open_aq
    from src.measurement.domain.task import ingest_se_open_aq
    from src.measurement.domain.task import ingest_dk_open_aq

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
