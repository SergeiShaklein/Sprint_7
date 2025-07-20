import allure
import data
from conftest import *

class TestCreateOrder:
    @allure.title('Тест на создание заказа с цветом BLACK, с цветом BLACK или GREY и без указания цвета, ручка: /api/v1/orders')
    @pytest.mark.parametrize('colour', [['BLACK'], ['BLACK', 'GREY'], ['']])
    def test_selection_color_scooter(self, colour):
        order_body = data.OrderBody.order_body
        order_body["color"] = colour
        response = requests.post(f'{Url.CREATE_ORDER}', json=order_body)
        assert data.Flags.SUCCESS_ORDER_CREATE in response.json()
        assert response.status_code == 201