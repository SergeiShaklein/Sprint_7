import generators

class Url:
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru'
    CREATE_COURIER = f'{MAIN_URL}/api/v1/courier' #POST
    LOGIN_COURIER = f'{MAIN_URL}/api/v1/courier/login' #POST
    DELETE_COURIER = f'{MAIN_URL}/api/v1/courier/:id' #DELETE
    GET_COST_ORDERS_COURIER = f'{MAIN_URL}/api/v1/courier/:id/ordersCount' #GET
    COMPLETE_ORDER = f'{MAIN_URL}/api/v1/orders/finish/:id' #PUT
    CANCEL_ORDER = f'{MAIN_URL}/api/v1/orders/cancel' #PUT
    GET_LIST_ORDER = f'{MAIN_URL}/api/v1/orders' #GET
    GET_ORDER_BY_NUMBER = f'{MAIN_URL}/api/v1/orders/track' #GET
    ACCEPT_ORDER = f'{MAIN_URL}/api/v1/orders/accept/:id' #PUT
    CREATE_ORDER = f'{MAIN_URL}/api/v1/orders' #POST
    UTILS_PING_SERVER = f'{MAIN_URL}/api/v1/ping' #GET
    UTILS_SEARCH_METRO_STATION = f'{MAIN_URL}/api/v1/stations/search' #GET


class FakeDataForCourier:
    courier_fake_data = {
        'login': "Ivashka",
        'password': "1793"
    }

class ResponseBody:
    COURIER_CREATE_SUCCESS = {'ok': True}
    COURIER_CREATE_WITHOUT_LOGIN_OR_PASSWORD = {"code": 400, "message": "Недостаточно данных для создания учетной записи"}
    COURIER_WITH_REPEAT_LOGIN = {"code": 409, "message": "Этот логин уже используется"}
    COURIER_DELETED_BY_ID = {'ok': True}
    COURIER_ID_NOT_FOUND = {"code": 404, "message": "Курьера с таким id нет"}
    COURIER_WITHOUT_ID = {"code": 400, "message":  "Недостаточно данных для удаления курьера"}
    COURIER_LOGIN_SUCCESS = {"message":"id"}
    COURIER_LOGIN_WITHOUT_LOGIN_OR_PASSWORD = {"code": 400, "message":  "Недостаточно данных для входа"}
    COURIER_LOGIN_NON_EXIST_LOGIN_PASSWORD = {"code": 404, "message": "Учетная запись не найдена"}
    COURIER_GET_ORDERS = {"code": 404, "message": "Учетная запись не найдена"}
    ORDER_CREATE = {"code": 201}

class Flags:
    SUCCESS_ORDER_CREATE = 'track'
    SUCCESS_GET_ORDER_LIST = 'orders'

class DateRegistration:
    registration_data = [{'password': generators.password_generator(), 'firstName': generators.name_generator()},
                         {'login': generators.login_generator(), 'firstName': generators.name_generator()}]

class OrderBody:
    order_body = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": []
}