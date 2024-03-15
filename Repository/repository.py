import psycopg2
from modules.User.user_schema import User
class Repository:

    __conn = None

    def __init__(self):
        self.__conn = psycopg2.connect(dbname = "postgres", user = "postgres", password = "postgres", host = "db", port = "5432")
        cursor = self.__conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name TEXT, projects TEXT[], user_id TEXT)")
        self.__conn.commit()
        pass


    def add_user(self, user: User):
        cursor = self.__conn.cursor()
        cursor.execute(f"SELECT * FROM users where name = '{user.name}'")
        
        _user = cursor.fetchall()
        print(_user)
        if _user == []:
            cursor.execute(f"INSERT INTO users (name, user_id) VALUES ('{user.name}', '{user.user_id}')")
            self.__conn.commit()
            return

        raise ValueError

    def get_user_info_by_id(self, id: str):
        cursor = self.__conn.cursor()
        cursor.execute(f"SELECT name, projects, user_id FROM users where user_id = '{id}'")
        user = cursor.fetchall()
        return user
    
    def get_user_info_by_name(self, name: str):
        cursor = self.__conn.cursor()
        cursor.execute(f"SELECT name, projects, user_id FROM users where name = '{name}'")
        user = cursor.fetchall()
        return user