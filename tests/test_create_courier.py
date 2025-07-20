import allure
import data
from conftest import *


class TestCreateCourier:
    @allure.title('Тест на создание нового курьера, ручка: api/v1/courier')
    def test_create_new_courier(self, create_courier):
        response = requests.post(f'{Url.CREATE_COURIER}', json=create_courier[0])
        assert response.json() == data.ResponseBody.COURIER_CREATE_SUCCESS
        assert response.status_code == 201

    @allure.title('Тест: нельзя создать двух одинаковых курьеров, ручка: api/v1/courier')
    def test_create_duplicate_courier(self, create_duplicate_courier):
        response = requests.post(Url.CREATE_COURIER, json=create_duplicate_courier[0])
        assert response.json() == data.ResponseBody.COURIER_WITH_REPEAT_LOGIN
        assert response.status_code == 409

    @allure.title('Тест: чтобы создать курьера, нужно передать в ручку все обязательные поля, ручка: api/v1/courier')
    @pytest.mark.parametrize("data_create", data.DateRegistration.registration_data)
    def test_create_courier_missing_fields(self, data_create):
        response = requests.post(Url.CREATE_COURIER, json=data_create)
        assert response.json() == data.ResponseBody.COURIER_CREATE_WITHOUT_LOGIN_OR_PASSWORD
        assert response.status_code == 400