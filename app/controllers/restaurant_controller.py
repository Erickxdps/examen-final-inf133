from flask import Blueprint, request, jsonify # type: ignore
from app.models.restaurant_model import Restaurante
from app.views.restaurant_view import render_restaurant_list, render_restaurant_detail
from app.utils.decorators import jwt_required, role_required

restaurante_bp = Blueprint("restaurante", __name__)

@restaurante_bp.route("/restaurants", methods=["GET"])
@jwt_required
@role_required(roles=["admin", "customer"])
def get_restaurantes():
    restaurantes = Restaurante.get_all()
    return jsonify(render_restaurant_list(restaurantes))


@restaurante_bp.route("/restaurants/<int:id>", methods=["GET"])
@jwt_required
@role_required(roles=["admin", "customer"])
def get_restaurante(id):
    restaurante = Restaurante.get_by_id(id)
    if restaurante:
        return jsonify(render_restaurant_detail(restaurante))
    return jsonify({"error": "Restaurante no encontrado"}), 404


@restaurante_bp.route("/restaurants", methods=["POST"])
@jwt_required
@role_required(roles=["admin"])
def create_restaurante():
    data = request.json
    name = data.get("name")
    address = data.get("address")
    city = data.get("city")
    phone = data.get("phone")
    description = data.get("description")
    rating = data.get("rating")
    if name is None or address is None or city is None or phone is None or description is None or rating is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    restaurante = Restaurante(name=name, address=address, city=city, phone=phone, description=description, rating=rating)
    restaurante.save()
    return jsonify(render_restaurant_detail(restaurante)), 201


@restaurante_bp.route("/restaurants/<int:id>", methods=["PUT"])
@jwt_required
@role_required(roles=["admin"])
def update_restaurante(id):
    restaurante = Restaurante.get_by_id(id)
    if not restaurante:
        return jsonify({"error": "Restaurante no encontrado"}), 404

    data = request.json
    name = data.get("name")
    address = data.get("address")
    city = data.get("city")
    phone = data.get("phone")
    description = data.get("description")
    rating = data.get("rating")
    restaurante.update(name=name, address=address, city=city, phone=phone, description=description, rating=rating)
    return jsonify(render_restaurant_detail(restaurante))

@restaurante_bp.route("/restaurants/<int:id>", methods=["DELETE"])
@jwt_required
@role_required(roles=["admin"])
def delete_restaurante(id):
    restaurante = Restaurante.get_by_id(id)
    if not restaurante:
        return jsonify({"error": "Restaurante no encontrado"}), 404
    restaurante.delete()
    return "", 204
