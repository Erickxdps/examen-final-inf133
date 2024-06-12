from flask import Blueprint, request, jsonify # type: ignore
from app.models.reserva_model import Reserva
from app.views.reserva_view import render_reserva_list, render_reserva_detail
from app.utils.decorators import jwt_required, role_required

reserva_bp = Blueprint("reserva", __name__)

@reserva_bp.route("/reservations", methods=["GET"])
@jwt_required
@role_required(roles=["admin", "user"])
def get_reservas():
    reservas = Reserva.get_all()
    return jsonify(render_reserva_list(reservas))

@reserva_bp.route("/reservations/<int:id>", methods=["GET"])
@jwt_required
@role_required(roles=["admin", "user"])
def get_reserva(id):
    reserva = Reserva.get_by_id(id)
    if reserva:
        return jsonify(render_reserva_detail(reserva))
    return jsonify({"error": "Reserva no encontrada"}), 404

@reserva_bp.route("/reservations", methods=["POST"])
@jwt_required
@role_required(roles=["admin"])
def create_reserva():
    data = request.json
    user_id = data.get("user_id")
    restaurant_id = data.get("restaurant_id")
    reservation_date = data.get("reservation_date")
    num_guests = data.get("num_guests")
    special_requests = data.get("special_requests")
    status = data.get("status")
    
    if user_id is None or restaurant_id is None or reservation_date is None or num_guests is None or special_requests is None or status is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    reserva = Reserva(user_id=user_id, restaurant_id=restaurant_id,
                    reservation_date=reservation_date, num_guests=num_guests,
                    special_requests=special_requests, status=status)
    reserva.save()

    return jsonify(render_reserva_detail(reserva)), 201

@reserva_bp.route("/reservations/<int:id>", methods=["PUT"])
@jwt_required
@role_required(roles=["admin"])
def update_reserva(id):
    reserva = Reserva.get_by_id(id)

    if not reserva:
        return jsonify({"error": "Reserva no encontrada"}), 404

    data = request.json
    user_id = data.get("user_id")
    restaurant_id = data.get("restaurant_id")
    reservation_date = data.get("reservation_date")
    num_guests = data.get("num_guests")
    special_requests = data.get("special_requests")
    status = data.get("status")
    
    reserva.update(user_id=user_id, restaurant_id=restaurant_id,
                    reservation_date=reservation_date, num_guests=num_guests,
                    special_requests=special_requests, status=status)
    return jsonify(render_reserva_detail(reserva))

@reserva_bp.route("/reservations/<int:id>", methods=["DELETE"])
@jwt_required
@role_required(roles=["admin"])
def delete_reserva(id):
    reserva = Reserva.get_by_id(id)

    if not reserva:
        return jsonify({"error": "Reserva no encontrada"}), 404
    
    reserva.delete()
    
    return "", 204
