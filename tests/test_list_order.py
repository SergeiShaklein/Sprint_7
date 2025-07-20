import allure
import data
from conftest import *

class TestGetListOrder:
    @allure.title('Тест на проверку, что в тело ответа возвращается список заказов, ручка: /api/v1/orders')
    def test_get_order_list(self):
        response = requests.get(f'{Url.GET_LIST_ORDER}')
        assert data.Flags.SUCCESS_GET_ORDER_LIST in response.json()
        assert response.status_code == 200