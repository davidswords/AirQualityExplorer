from datetime import datetime

from src import app

from flask import jsonify


@app.route("/measurement/<country>", methods=["GET"])
def retrieve_measurement_from_country(country: str):
    return (
        jsonify(
            [
                {
                    "id_": "216bb524",
                    "created_at": datetime.utcnow(),
                    "updated_at": datetime.utcnow(),
                    "archived": False,
                    "recorded_at": datetime.utcnow(),
                    "city": "Trondheim",
                    "country": "NO",
                    "pollutant": "PM2.5",
                    "value": "2.5",
                },
            ]
        ),
        200,
    )
