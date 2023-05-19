from datetime import datetime

from src import app

from flask import jsonify


@app.route("/measurement/<country>", methods=["GET"])
def retrieve_measurement_from_country(country: str):
    return (
        jsonify(
            [
                {
                    "id_": "216bb524-896f-42d2-8d07-9aa68cd2ea8d",
                    "created_at": datetime.utcnow(),
                    "updated_at": datetime.utcnow(),
                    "archived": False,
                    "recorded_at": datetime.utcnow(),
                    "city": "Trondheim",
                    "country": "NO",
                    "pollutant": "PM2.5",
                    "value": "2.5",
                },
                {
                    "id_": "07ae69c4-c24e-4acd-a5a7-176fe3996aeb",
                    "created_at": datetime.utcnow(),
                    "updated_at": datetime.utcnow(),
                    "archived": False,
                    "recorded_at": datetime.utcnow(),
                    "city": "Bergen",
                    "country": "NO",
                    "pollutant": "PM10",
                    "value": "2.5",
                },
                {
                    "id_": "f058d4b5-ceeb-45ae-b7f1-60d9a9dba004",
                    "created_at": datetime.utcnow(),
                    "updated_at": datetime.utcnow(),
                    "archived": False,
                    "recorded_at": datetime.utcnow(),
                    "city": "Oslo",
                    "country": "NO",
                    "pollutant": "SO2",
                    "value": "2.5",
                },
                {
                    "id_": "6049c1d2-356c-4f04-adc8-6cdb05021087",
                    "created_at": datetime.utcnow(),
                    "updated_at": datetime.utcnow(),
                    "archived": False,
                    "recorded_at": datetime.utcnow(),
                    "city": "Tromsø",
                    "country": "NO",
                    "pollutant": "NO2",
                    "value": "2.5",
                },
            ]
        ),
        200,
    )
