import allure
import data
from conftest import *

class TestLoginCourier:
    @allure.title('Тест на успешную авторизацию курьера, ручка: /api/v1/courier/login')
    def test_success_login_courier(self, create_duplicate_courier):
        response = requests.post(f'{Url.LOGIN_COURIER}', json=create_duplicate_courier[1])
        assert response.json() != ''
        assert response.status_code == 200

    @allure.title('Тест на неудачную авторизацию с пустым полем login, ручка: /api/v1/courier/login')
    def test_login_courier_without_login(self, create_duplicate_courier):
        response_data = {'login': '', 'password': create_duplicate_courier[3]}
        response = requests.post(f'{Url.LOGIN_COURIER}', json=response_data)
        assert response.json() == data.ResponseBody.COURIER_LOGIN_WITHOUT_LOGIN_OR_PASSWORD
        assert response.status_code == 400

    @allure.title('Тест на неудачную авторизацию с пустым полем password, ручка: /api/v1/courier/login')
    def test_login_courier_without_password(self, create_duplicate_courier):
        response_data = {'login': create_duplicate_courier[2], 'password': ''}
        response = requests.post(f'{Url.LOGIN_COURIER}', json=response_data)
        assert response.json() == data.ResponseBody.COURIER_LOGIN_WITHOUT_LOGIN_OR_PASSWORD
        assert response.status_code == 400

    @allure.title('Тест на неудачную авторизацию с несуществующей парой login-password, ручка: /api/v1/courier/login')
    def test_login_courier_with_fake_login_and_password(self):
        response_data = data.FakeDataForCourier.courier_fake_data
        response = requests.post(f'{Url.LOGIN_COURIER}', json=response_data)
        assert response.json() == data.ResponseBody.COURIER_LOGIN_NON_EXIST_LOGIN_PASSWORD
        assert response.status_code == 404