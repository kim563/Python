from .api_employee9 import Employee
from .db_employee import Data_Base

api = Employee("https://x-clients-be.onrender.com")
db = Data_Base("postgresql+psycopg2://x_clients_db_3fmx_user:\
               mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21f\
               ec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")

company_id = 14734


def test_get_employee():
    api_result = api.get_employee_list({'company': company_id})
    db_result = db.get_employee_list(company_id)
    assert len(api_result.json()) == len(db_result)


def test_add_employee():
    resp = api.get_employee_list({'company': company_id})
    len_before = len(resp.json())

    body = {
        "id": 10,
        "firstName": "Anastasia",
        "lastName": "Titova",
        "middleName": "Sergeevna",
        "companyId": company_id,
        "email": "bo@mail.ru",
        "url": "db-54.ooo.ru",
        "phone": "8-800-555-35-35",
        "birthdate": "2000-07-11T09:38:55.274Z",
        "isActive": True
    }
    resp = api.create_employee(body)
    user_id = resp.json()['id']
    print(user_id)

    assert resp.status_code == 201

    resp = api.get_employee_list({'company': company_id})
    len_after = len(resp.json())

    db.delete_employee(user_id)

    assert len_after - len_before == 1
    for employee in resp.json():
        if employee["id"] == user_id:
            assert employee["firstName"] == body["firstName"]
            assert employee["lastName"] == body["lastName"]
            assert employee["middleName"] == body["middleName"]


def test_get_employee_id():

    body = {
        "id": 10,
        "firstName": "Anastasia",
        "lastName": "Titova",
        "middleName": "Sergeevna",
        "companyId": company_id,
        "email": "bo@mail.ru",
        "url": "db-54.ooo.ru",
        "phone": "8-800-555-35-35",
        "birthdate": "2000-07-11T09:38:55.274Z",
        "isActive": True
    }

    db.create_employee(
        body["firstName"],
        body["lastName"],
        body["phone"],
        company_id
        )
    max_id = db.get_max_id_employee()

    resp = api.get_employee(max_id)

    db.delete_employee(max_id)

    assert resp.status_code == 200
    assert resp.json()["firstName"] == body["firstName"]
    assert resp.json()["lastName"] == body["lastName"]


def test_update_employee():

    body = {
        "id": 10,
        "firstName": "Anastasia",
        "lastName": "Titova",
        "middleName": "Sergeevna",
        "companyId": company_id,
        "email": "bo@mail.ru",
        "url": "db-54.ooo.ru",
        "phone": "8-800-555-35-35",
        "birthdate": "2000-07-11T09:38:55.274Z",
        "isActive": True
    }
    db.create_employee(
        body["firstName"],
        body["lastName"],
        body["phone"],
        company_id
        )
    max_id = db.get_max_id_employee()

    new_body = {
        "lastName": "Titiva",
        "email": "booo@mail.ru",
        "url": "db-54.oooo.ru",
        "phone": "8-800-555-35-39",
        "isActive": True
    }

    resp = api.update_employee(max_id, new_body)

    db.delete_employee(max_id)

    assert resp.status_code == 200
    assert resp.json()["email"] == new_body["email"]
