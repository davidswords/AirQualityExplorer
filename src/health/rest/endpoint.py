from src import app

from flask import jsonify


@app.route("/health")
def health():
    return jsonify("healthy!"), 200
