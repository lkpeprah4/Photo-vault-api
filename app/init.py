from flask import Flask
from app.extensions import db
from app.config import config

def create_app():
    app=Flask(__name__)
    app.config.from_object(config)


    db.init_app(app)
    return app


    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["JWT_SECRET_KEY"] = "super-secret-key"

    # initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # register blueprint
    app.register_blueprint(auth_bp)

    return app
