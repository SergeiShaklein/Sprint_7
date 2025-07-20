import pytest
import requests
from data import Url
import generators


@pytest.fixture
def create_courier():
    login = generators.login_generator()
    password = generators.password_generator()
    name = generators.name_generator()
    create_courier_body = {"firstName": name, "login": login, "password": password}
    login_courier_body = {"login": login, "password": password}
    courier_login = requests.post(f'{Url.LOGIN_COURIER}', json=login_courier_body)
    yield [create_courier_body, login_courier_body]
    requests.delete(f'{Url.DELETE_COURIER}{courier_login.json().get("id")}')


@pytest.fixture
def create_duplicate_courier():
    login = generators.login_generator()
    password = generators.password_generator()
    name = generators.name_generator()
    create_courier_body = {"firstName": name, "login": login, "password": password}
    requests.post(Url.CREATE_COURIER, json=create_courier_body)
    login_courier_body = {"login": login, "password": password}
    courier_login = requests.post(f'{Url.LOGIN_COURIER}', json=login_courier_body)
    yield [create_courier_body, login_courier_body, login, password]
    requests.delete(f'{Url.DELETE_COURIER}{courier_login.json().get("id")}')



