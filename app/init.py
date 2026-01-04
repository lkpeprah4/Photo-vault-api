from flask import Flask
from app.extensions import db
from app.config import config

def create_app():
    app=Flask(__name__)
    app.config.from_object(config)


    db.init_app(app)
    return app