from .api_employee9 import Employee
from .db_employee import DataBase
from faker import Faker
import allure
import re

fake = Faker('ru_RU')

api = Employee("https://x-clients-be.onrender.com")
db = DataBase("postgresql+psycopg2://x_clients_user:\
              95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.\
              frankfurt-postgres.render.com/x_clients_db_fxd0")


@allure.title("Получение списка сотрудников")
@allure.description("Тест проверяет получение списка \
                    сотрудников с использованием API и \
                    сравнение с данными из базы данных.")
@allure.feature("Сотрудники")
@allure.severity(allure.severity_level.CRITICAL)
@allure.step("Тестирование получения сотрудников")
def test_get_employee():
    with allure.step("Создание компании"):
        db.create_company(fake.company())
    with allure.step("Получение id созданной компании"):
        company_id = db.get_max_id_company()

    with allure.step("Получение списка сотрудников через API"):
        api_result = api.get_employee_list({'company': company_id})
    with allure.step("Получение списка сотрудников из базы данных"):
        db_result = db.get_employee_list(company_id)

    with allure.step("Удаление компании"):
        db.delete_company(company_id)
    with allure.step("Сравнение количества сотрудников"):
        assert len(api_result.json()) == len(db_result)


@allure.title("Добавление нового сотрудника")
@allure.description("Тест проверяет добавление нового \
                    сотрудника через API и проверку его \
                    наличия в списке сотрудников.")
@allure.feature("Сотрудники")
@allure.severity(allure.severity_level.BLOCKER)
@allure.step("Тестирование добавления сотрудника")
def test_add_employee():
    with allure.step("Создание компании"):
        db.create_company(fake.company())
    with allure.step("Получение id созданной компании"):
        company_id = db.get_max_id_company()

    with allure.step("Получение списка сотрудников перед добавлением"):
        resp = api.get_employee_list({'company': company_id})
        len_before = len(resp.json())

        body = {
            "id": 0,
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "middleName": fake.middle_name(),
            "companyId": company_id,
            "email": fake.ascii_free_email(),
            "url": fake.uri(),
            "phone": re.sub('\\D', '', fake.phone_number()),
            "birthdate": fake.iso8601(),
            "isActive": True
        }
    with allure.step("Добавление нового сотрудника"):
        resp = api.create_employee(body)
        print(resp)
        user_id = resp.json()['id']

    with allure.step("Проверка кода состояния после создания"):
        assert resp.status_code == 201

    with allure.step("Получение списка сотрудников после добавления"):
        resp = api.get_employee_list({'company': company_id})
        len_after = len(resp.json())

    with allure.step("Удаление созданного сотрудника"):
        db.delete_employee(user_id)
    with allure.step("Удаление созданной компании"):
        db.delete_company(company_id)

    with allure.step("Сравнение длины списков и проверка \
                     данных нового сотрудника"):
        assert len_after - len_before == 1
        for employee in resp.json():
            if employee["id"] == user_id:
                assert employee["firstName"] == body["firstName"]
                assert employee["lastName"] == body["lastName"]
                assert employee["middleName"] == body["middleName"]


@allure.title("Получение сотрудника по id")
@allure.description("Тест проверяет получение сотрудника по ID \
                    через API и сравнение с данными в базе данных.")
@allure.feature("Сотрудники")
@allure.severity(allure.severity_level.MINOR)
@allure.step("Тестирование получения сотрудника по его ID")
def test_get_employee_id():
    with allure.step("Создание компании"):
        db.create_company(fake.company())
    with allure.step("Получение id созданной компании"):
        company_id = db.get_max_id_company()

        body = {
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "phone": re.sub('\\D', '', fake.phone_number())
        }

    with allure.step("Создание сотрудника в базе данных"):
        db.create_employee(
            body["firstName"],
            body["lastName"],
            body["phone"],
            company_id
            )
    with allure.step("Получение id созданного сотрудника"):
        user_id = db.get_max_id_employee()
    with allure.step("Получение сотрудника через API"):
        resp = api.get_employee(user_id)

    with allure.step("Удаление сотрудника"):
        db.delete_employee(user_id)
    with allure.step("Удаление компании"):
        db.delete_company(company_id)

    with allure.step("Проверка кода состояния и данных сотрудника"):
        assert resp.status_code == 200
        assert resp.json()["firstName"] == body["firstName"]
        assert resp.json()["lastName"] == body["lastName"]


@allure.title("Изменение данных о сотруднике")
@allure.description("Тест проверяет изменение данных сотрудника \
                    через API и проверку обновленных данных.")
@allure.feature("Сотрудники")
@allure.severity(allure.severity_level.CRITICAL)
@allure.step("Тестирование обновления данных сотрудника")
def test_update_employee():
    with allure.step("Создание компании"):
        db.create_company(fake.company())
    with allure.step("Получение id созданной компании"):
        company_id = db.get_max_id_company()

        body = {
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "phone": re.sub('\\D', '', fake.phone_number())
        }

    with allure.step("Создание сотрудника в базе данных"):
        db.create_employee(
            body["firstName"],
            body["lastName"],
            body["phone"],
            company_id
            )

    with allure.step("Получение id созданного сотрудника"):
        user_id = db.get_max_id_employee()

        new_body = {
            "lastName": fake.last_name(),
            "email": fake.ascii_free_email(),
            "url": fake.uri(),
            "phone": re.sub('\\D', '', fake.phone_number()),
            "isActive": True
        }

    with allure.step("Обновление данных сотрудника через API"):
        resp = api.update_employee(user_id, new_body)

    with allure.step("Удаление сотрудника"):
        db.delete_employee(user_id)
    with allure.step("Удаление компании"):
        db.delete_company(company_id)

    with allure.step("Проверка кода состояния и данных сотрудника"):
        assert resp.status_code == 200
        assert resp.json()["email"] == new_body["email"]
