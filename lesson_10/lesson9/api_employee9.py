import requests
import allure


class Employee:
    """ Класс для работы с API сотрудников """

    def __init__(self, url: str) -> None:
        """
        Инициализация обьекта.

        args:
        url - базовый URL для API.
        """
        self.url = url

    @allure.step("Получение токена авторизации для пользователя {user}")
    def get_token(
        self,
        user: str = 'donatello',
        password: str = 'does-machines'
    ):
        """
        Авторизация на сайте.

        args:
        user - имя пользователя,
        password - пароль пользователя.

        return: Токен авторизации.
        """
        creds = {
            "username": user,
            "password": password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]

    @allure.step("Получение списка сотрудников для компании с {id_company}")
    def get_employee_list(self, id_company: int):
        """
        Получить список сотрудников для компании.

        args:
        id_company - ID компании.

        return: Список сотрудников.
        """
        resp = requests.get(self.url + '/employee', params=id_company)
        return resp

    @allure.step("Добавление нового сотрудника с описанием {description}")
    def create_employee(self, description: dict):
        """
        Добавить нового сотрудника.

        args:
        description - описание сотрудника в формате JSON.

        return: Ответ после создания сотрудника.
        """
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/employee',
                             json=description, headers=my_headers)
        return resp

    @allure.step("Получение сотрудника по {user_id}")
    def get_employee(self, user_id: int):
        """
        Получение информации о сотруднике по id.

        args:
        user_id: id сотрудника.

        return: Ответ с информацией о сотруднике.
        """
        resp = requests.get(self.url + '/employee/' + str(user_id))
        return resp

    @allure.step("Изменение информации о сотруднике с {user_id}")
    def update_employee(self, user_id: int, description: dict):
        """
        Изменить информацию о сотруднике.

        args:
        user_id - id сотрудника.
        description - новое описание сотрудника в формате JSON.

        return: Ответ после изменения информации о сотруднике.
        """
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.patch(self.url + '/employee/' + str(user_id),
                              json=description, headers=my_headers)
        return resp
