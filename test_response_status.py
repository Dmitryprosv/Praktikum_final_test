# Дмитрий Просветов, 13-я когорта. Дипломный проект. Инженер по тестированию плюс
import setup_order
import data


def test_status_of_order_is_200():
    response_order = setup_order.post_new_order(data.order_request_body)  # Запрос на создание заказа
    track = {"t": response_order.json()["track"]}  # Сохраняем трек-номер заказа
    response = setup_order.get_order_data(track)
    assert response.status_code == 200  # Проверка кода ответа 200
