from src import app

from flask import jsonify

from src.measurement.domain.service import MeasurementService


@app.route("/measurement/<pollutant>", methods=["GET"])
def retrieve_by_pollutant(pollutant: str):
    service = MeasurementService()

    entities = service.retrieve_by_pollutant(pollutant=pollutant)

    if not entities:
        return jsonify({"message": "No measurements found for this pollutant"}), 404

    return jsonify([vars(entity) for entity in entities]), 200


@app.route("/measurement/<pollutant>/<country>", methods=["GET"])
def retrieve_by_country(pollutant: str, country: str):
    service = MeasurementService()

    entities = service.retrieve_by_country(pollutant=pollutant, country=country)

    if not entities:
        return jsonify({"message": "No measurements found for this country"}), 404

    return jsonify([vars(entity) for entity in entities]), 200


@app.route("/measurement/<pollutant>/<country>/<city>", methods=["GET"])
def retrieve_by_city(pollutant: str, country: str, city: str):
    service = MeasurementService()

    entities = service.retrieve_by_city(pollutant=pollutant, country=country, city=city)

    if not entities:
        return jsonify({"message": "No measurements found for this city"}), 404

    return jsonify([vars(entity) for entity in entities]), 200
