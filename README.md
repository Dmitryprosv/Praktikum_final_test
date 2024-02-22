# Тест на проверку, что по треку заказа можно получить данные о заказе в приложении Яндекс Самокат.
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполянется командой pytest

- Последовательность действий:
 

1. Создал файл configuration.py для хранения URL сервера и всех нужных эндпоинтов
 

   В нём указал следующие переменные:
 

   URL = 'https://05f4e9e3-261b-49b4-aba0-fcb58418bf14.serverhub.praktikum-services.ru'
 

   ORDER_CREATE_PATH = '/api/v1/orders' - эндпоинт создания заказа (post) 
 

   GET_ORDER_DATA_PATH = '/api/v1/orders/track' - эндпоинт получения заказ по его номеру (get)
 

2. Создал файл data.py для хранения тела запроса
 

order_request_body = {
    "firstName": "Абдурахмангаджи",
    "lastName": "Убдурахмангаджи",
    "address": "Центральный проезд Хорошёвского Серебряного Бора 2",
    "metroStation": 204,
    "phone": "+34916123451",
    "rentTime": 2,
    "deliveryDate": "2024-02-23",
    "comment": "Привет, Абдурахмангаджи!",
    "color": [
        "BLACK"
    ]
}

 
3. Создал файл setup_order.py
 

Импортирвал библиотеку requests, а так же уже созданный файл configuration.py
 

Далее объявил 2 низкоуровневые функции:
 

   
 

   # Функция создания нового заказа
 

ddef post_new_order(order_body):
    return requests.post(configuration.URL + configuration.ORDER_CREATE_PATH, json=order_body)
 

   # Функция получения трек-номера заказа
 

def get_order_data(track):
    return requests.get(configuration.URL + configuration.GET_ORDER_DATA_PATH, params=track)
 


4. Создал файл test_response_status.py
 

   Импортировал файлы data.py и setup_order.py
 

   
 

Написал функцию для сохранения трек-номера и проверки ответ статус-кода ответа сервера.

def test_status_of_order_is_200():
    response_order = setup_order.post_new_order(data.order_request_body) 
    track = {"t": response_order.json()["track"]} 
    response = setup_order.get_order_data(track)
    assert response.status_code == 200 
 

