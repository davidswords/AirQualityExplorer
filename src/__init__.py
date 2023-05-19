from flask import Flask

app = Flask(__name__)

with app.app_context():
    from src.health.rest.endpoint import health
