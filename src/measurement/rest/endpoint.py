from src import app

from flask import jsonify

from src.measurement.domain.service import MeasurementService


@app.route("/measurement/<country>", methods=["GET"])
def retrieve_measurement_from_country(country: str):
    service = MeasurementService()

    entities = service.retrieve_by_country(country=country)

    if not entities:
        return jsonify({"message": "No measurements found for this country"}), 404

    return jsonify([vars(entity) for entity in entities]), 200
