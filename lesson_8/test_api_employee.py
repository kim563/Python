from api_employee import Employee

api = Employee("https://x-clients-be.onrender.com")
company_id = 14734

def test_employee_list():
    resp = api.get_employee_list({'company': company_id})
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json; charset=utf-8"

def test_add_employee():
    resp = api.get_employee_list({'company': company_id})
    len_before = len(resp.json())

    body = {
        "id": 10,
        "firstName": "Anastasia",
        "lastName": "Titova",
        "middleName": "Sergeevna",
        "companyId": 14734,
        "email": "bo@mail.ru",
        "url": "db-54.ooo.ru",
        "phone": "8-800-555-35-35",
        "birthdate": "2000-07-11T09:38:55.274Z",
        "isActive": True
    }
    resp = api.create_employee(body)

    assert resp.status_code == 201

    resp = api.get_employee_list({'company': company_id})
    len_after = len(resp.json())

    assert len_after - len_before == 1
    assert resp.json()[-1]["firstName"] == body["firstName"]
    assert resp.json()[-1]["lastName"] == body["lastName"]
    assert resp.json()[-1]["middleName"] == body["middleName"]

def test_get_employee_id():

    body = {
        "id": 10,
        "firstName": "Anastasia",
        "lastName": "Titova",
        "middleName": "Sergeevna",
        "companyId": 14734,
        "email": "bo@mail.ru",
        "url": "db-54.ooo.ru",
        "phone": "8-800-555-35-35",
        "birthdate": "2000-07-11T09:38:55.274Z",
        "isActive": True
    }
    resp = api.create_employee(body)
    user_id = resp.json()['id']

    resp = api.get_employee(user_id)
    assert resp.status_code == 200
    assert resp.json()["firstName"] == body["firstName"]
    assert resp.json()["lastName"] == body["lastName"]
    assert resp.json()["middleName"] == body["middleName"]

def test_update_info():

    body = {
        "id": 10,
        "firstName": "Anastasia",
        "lastName": "Titova",
        "middleName": "Sergeevna",
        "companyId": 14734,
        "email": "bo@mail.ru",
        "url": "db-54.ooo.ru",
        "phone": "8-800-555-35-35",
        "birthdate": "2000-07-11T09:38:55.274Z",
        "isActive": True
    }
    resp = api.create_employee(body)
    user_id = resp.json()['id']

    new_body = {
        "lastName": "Titiva",
        "email": "booo@mail.ru",
        "url": "db-54.oooo.ru",
        "phone": "8-800-555-35-39",
        "isActive": True
    }

    resp = api.update_employee(user_id, new_body)
    assert resp.status_code == 200
    print(resp.json())
    assert resp.json()["email"] == new_body["email"]
