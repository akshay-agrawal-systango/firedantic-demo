import os
from flask import Flask
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app
from firedantic import configure
from .encoders import CustomJSONEncoder


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py', silent=True)
    return app

app = create_app()

app.json_encoder = CustomJSONEncoder


cred = credentials.Certificate("serviceAccountKey.json")
initialize_app(cred)


client = firestore.client()
configure(client, prefix="firedantic-test-")


@app.route("/")
def index():
    return "index page"

