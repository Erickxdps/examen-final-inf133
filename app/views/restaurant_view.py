def render_restaurant_list(restaurantes):
    return [
        {
            "id": restaurante.id,
            "name": restaurante.name,
            "address": restaurante.address,
            "city": restaurante.city,
            "phone": restaurante.phone,
            "description": restaurante.description,
            "rating" :restaurante.rating,
        }
        for restaurante in restaurantes
    ]


def render_restaurant_detail(restaurante):

    return {
        "id": restaurante.id,
        "name": restaurante.name,
        "address": restaurante.address,
        "city": restaurante.city,
        "phone": restaurante.phone,
        "description": restaurante.description,
        "rating": restaurante.rating,
    }
