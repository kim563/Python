import requests

class Employee:

    # Инициализация
    def __init__(self, url) -> None:
        self.url = url
    
    # Получить токен авторизации
    def get_token(self, user='donatello', password='does-machines'):
        creds = {
            "username": user,
            "password": password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]
    
    # Получить список сотрудников для компании
    def get_employee_list(self, id_company):
        resp = requests.get(self.url + '/employee', params=id_company)
        return resp
    
    # Добавить нового сотрудника:
    def create_employee(self, description):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/employee',
                             json=description, headers=my_headers)
        return resp
    
    # Получение сотрудника по id
    def get_employee(self, user_id):
        resp = requests.get(self.url + '/employee/' + str(user_id))
        return resp
    
    # Изменить информацию о сотруднике
    def update_employee(self, user_id, description):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.patch(self.url + '/employee/' + str(user_id),
                              json=description, headers=my_headers)
        return resp
