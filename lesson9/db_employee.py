from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.orm import Session
import allure

class DataBase:
    """ Класс для работы с базой данных сотрудников и компаний """

    __scripts = {
        "select_for_id": text("select * from employee where company_id = :id"),
        "delete_by_id": text("delete from employee where id = :id_to_delete"),
        "insert_company": text("INSERT INTO company (\"name\") values (:new_name);"),
        "insert_employee": text("INSERT into employee (first_name, \
            last_name, phone, company_id) values (:first_name, \
            :last_name, :phone, :company_id)"),
        "get_max_id": text("select MAX(\"id\") from employee"),
        "get_max_id_company": text("select MAX(\"id\") from company"),
        "delete_by_id_company": text("delete from company where id =:id_to_delete"),
    }

    def __init__(self, connection_string: str):
        """
        Инициализация обьекта.

        args:
        connection_string - строка подключения к базе данных.
        """
        self.db = Session(create_engine(connection_string))

    @allure.step("Создание компании с именем {name}")
    def create_company(self, name: str):
        """
        Создать новую компанию.

        args:
        name - имя новой компании.
        """
        with self.db.begin():
            sql = self.__scripts["insert_company"]
            self.db.execute(sql, {"new_name": name})
            self.db.commit()

    @allure.step("Получение максимального ID компании")
    def get_max_id_company(self):
        """
        Получить максимальный ID компании.

        return: Максимальный ID компании.
        """
        with self.db.begin():
            sql = self.__scripts["get_max_id_company"]
            result = self.db.execute(sql).fetchall()[0][0]
            self.db.commit()
            return result

    @allure.step("Получение списка сотрудников компании с {id_company}")
    def get_employee_list(self, id_company: int):
        """
        Получить список сотрудников для компании.

        args:
        id_company - id компании.

        return: Список сотрудников.
        """
        with self.db.begin():
            sql = self.__scripts["select_for_id"]
            result = self.db.execute(sql, {"id": id_company}).fetchall()
            self.db.commit()
            return result
    
    @allure.step("Удаление компании с {id}")
    def delete_company(self, id: int):
        """
        Удалить компанию по id.

        args:
        id - id компании.
        """
        with self.db.begin():
            sql = self.__scripts["delete_by_id_company"]
            self.db.execute(sql, {"id_to_delete": id})
            self.db.commit()

    @allure.step("Удаление сотрудника с {id}")
    def delete_employee(self, id: int):
        """
        Удалить сотрудника по id.

        args:
        id - id сотрудника.
        """
        with self.db.begin():
            sql = self.__scripts["delete_by_id"]
            self.db.execute(sql, {"id_to_delete": id})
            self.db.commit()

    @allure.step(
            "Создание сотрудника с параметрами: Имя {firstname}, \
            Фамилия {lastname}, Телефон {phone}, ID компании {company_id}"
        )
    def create_employee(
        self, firstname: str, lastname: str, phone: str, company_id: int
        ):
        """
        Создать нового сотрудника.

        args:
        firstname - имя сотрудника.
        lastname - фамилия сотрудника.
        phone - телефон сотрудника.
        company_id id компании.
        """
        with self.db.begin():
            sql = self.__scripts["insert_employee"]
            self.db.execute(
                sql,
                {
                    "first_name": firstname,
                    "last_name": lastname,
                    "phone": phone,
                    "company_id": company_id
                })
            self.db.commit()

    @allure.step("Получение максимального id сотрудника")
    def get_max_id_employee(self):
        """
        Получить максимальный id сотрудника.

        return: Максимальный id сотрудника.
        """
        with self.db.begin():
            sql = self.__scripts["get_max_id"]
            resp = self.db.execute(sql).fetchall()[0][0]
            self.db.commit()
            return resp
