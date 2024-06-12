def render_reserva_list(reservas):
    return [
        {
            "id": reserva.id,
            "user_id": reserva.user_id,
            "restaurant_id": reserva.restaurant_id,
            "reservation_date" : reserva.reservation_date,
            "num_guests": reserva.num_guests,
            "special_requests": reserva.special_requests,
            "status": reserva.status,  
        }
        for reserva in reservas
    ]


def render_reserva_detail(reserva):

    return {
        "id": reserva.id,
        "user_id": reserva.user_id,
        "restaurant_id": reserva.restaurant_id,
        "reservation_date" : reserva.reservation_date,
        "num_guests": reserva.num_guests,
        "special_requests": reserva.special_requests,
        "status": reserva.status,
    }
