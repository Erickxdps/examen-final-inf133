from flask import Blueprint, request, jsonify
from app.models.user_model import User
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

user_bp = Blueprint("user", __name__)

@user_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    roles = data.get("roles")

    if not username or not password:
        return jsonify({"error": "Se requieren nombre de usuario y contraseña"}), 400

    nombre_existente = User.find_by_username(username)
    email_existente = User.find_by_username(username)
    
    if nombre_existente:
        return jsonify({"error": "El nombre de usuario ya esta en uso"}), 400
    if email_existente:
        return jsonify({"error": "El email ya esta en uso"}), 400
    nuevo_usuario = User(username, password, roles)
    nuevo_usuario.save()
    return jsonify({"message": "Usuario creado exitosamente"}), 201


@user_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = User.find_by_username(username)
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(
            identity={"username": username, "roles": user.roles}
        )
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401