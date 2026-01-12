from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from extensions import bcrypt, db
from models import User

auth_bp = Blueprint("auth_bp", __name__, url_prefix="/auth")


bcrypt = Bcrypt()
auth_bp = Blueprint("auth_bp", __name__, url_prefix="/auth")


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username:
        return jsonify({"msg": "USERNAME FIELD IS REQUIRED"}), 400
    if not password:
        return jsonify({"msg": "PASSWORD FIELD IS REQUIRED"}), 400

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"msg": "USERNAME DOES NOT EXISTS"}), 404
    if not bcrypt.check_password_hash(user.password, password):
        return jsonify({"msg": "WRONG PASSWORD! "}), 401

    access_token = create_access_token(identity=str(user.id))

    return jsonify({"msg": "LOGIN SUCCESSFUL", "access_token": access_token}), 200


@auth_bp.route("/protect", methods=["GET"])
@jwt_required()
def protect():
    user_id = get_jwt_identity()
    return jsonify({"msg": f"Hello user {user_id}, you are logged in!"}), 200

