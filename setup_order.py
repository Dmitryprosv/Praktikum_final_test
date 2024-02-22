import configuration
import requests


def post_new_order(order_body):  # функция создания заказа
    return requests.post(configuration.URL + configuration.ORDER_CREATE_PATH, json=order_body)


def get_order_data(track):  # Функция получения трек-номера заказа
    return requests.get(configuration.URL + configuration.GET_ORDER_DATA_PATH, params=track)
