from sqlalchemy import create_engine
from sqlalchemy.sql import text


class Data_Base:

    __scripts = {
        "select_for_id": text("select * from employee where company_id = :id"),
        "delete_by_id": text("delete from employee where id = :id_to_delete"),
        "insert_employee": text("INSERT into employee (first_name, \
            last_name, phone, company_id) values (:first_name, \
            :last_name, :phone, :company_id)"),
        "get_max_id": text("select MAX(\"id\") from employee"),
    }

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_employee_list(self, id_company):
        sql = self.__scripts["select_for_id"]
        return self.db.connect().execute(sql, {"id": id_company}).fetchall()

    def delete_employee(self, id):
        sql = self.__scripts["delete_by_id"]
        self.db.connect().execute(sql, {"id_to_delete": id})

    def create_employee(self, firstname, lastname, phone, company_id):
        sql = self.__scripts["insert_employee"]
        self.db.connect().execute(
            sql,
            {
                "first_name": firstname,
                "last_name": lastname,
                "phone": phone,
                "company_id": company_id
            }
        )

    def get_max_id_employee(self):
        sql = self.__scripts["get_max_id"]
        resp = self.db.connect().execute(sql).fetchall()[0][0]
        return resp
