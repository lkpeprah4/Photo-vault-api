from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask import request,jsonify,Blueprint
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_bcrypt import Bcrypt
from .models import db, User

db=SQLAlchemy()
brcypt=Bcrypt()