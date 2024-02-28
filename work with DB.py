import mysql.connector
from config import data_base
from Class_exercise import Chest_ex
from Class_about_user import User
from Class_about_user import User_char
import openpyxl as op


class DB:
    """Класс для инициализации базы данных и работы с ней
        в методе init присваиваются значения из файла config.py"""

    def __init__(self, host=data_base['host'], port=data_base['port'], user=data_base['user'],
                 password=data_base['password'], db_name=data_base['db_name']):
        self._host = host
        self._port = port
        self._user = user
        self._password = password
        self._db_name = db_name
        self._connection = self.connect()
        # self._cursor = self._connection.cursor()

    # def connect(self) -> mysql.connector | None:
    def connect(self) -> mysql.connector:
        """Подключение к БД"""

        try:
            self.name = self._db_name
            connect = mysql.connector.connect(
                host=self._host,
                port=self._port,
                user=self._user,
                password=self._password,
                database=self.name,
            )
            return connect

        except Exception as exc:
            print(f'connection failed in function connect, exception: {exc}')
            print(exc)

    def add_new_user(self, user: object) -> int:
        """Добавляет нового пользователя в таблицу user.
        Возвращает iduser последнего добавленного юзера"""

        insert_query = f"INSERT INTO exercise.user (login, email, password)" \
                       f" VALUES (\"{user.login}\", \"{user.email}\", \"{user.password}\");"

        try:
            with self._connection.cursor() as cursor:
                cursor.execute(insert_query)
                # чтобы сохранить в бд
                self._connection.commit()
                print('string is added')
                return self._connection_lastid(cursor)
                # print(self._connection_lastid(cursor))
                # self._connection_close()
        except Exception as exc:
            print(f'connection failed in function add_new_user, exception: {exc}')
            print(exc)

    def add_user_char(self, id_user: int, user_char: object) -> None:
        """Создаёт характеристики юзера"""

        insert_query = f"INSERT INTO exercise.user_characteristic (iduser, aim, level, days," \
                       f" muscule, male, height, weight, fat, day_counter, mark, weight_mult, number_mult, current_plan) " \
                       f"VALUES ({id_user}, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        try:
            with self._connection.cursor() as cursor:
                cursor.execute(insert_query, user_char.all_stat())
                # чтобы сохранить в бд
                self._connection.commit()
                # self._connection_close() #- for what???
                print('string is added')
        except Exception as exc:
            print(f'connection failed in function add_user_char, exception: {exc}')
            print(exc)

    def select_user(self, desktop_login: str) -> list:
        """Выводит данные юзера по логину из БД
        desktop_login - логин, который вводит пользователь с экрана"""

        select_query = f"SELECT * FROM exercise.user WHERE login = \"{desktop_login}\";"
        # select_query = f"SELECT * FROM exercise.user WHERE login = 'Monica';"
        try:
            with self._connection.cursor() as cursor:
                cursor.execute(select_query)
                # self._connection_close()
                selected_user = cursor.fetchone()
                if selected_user is None:
                    raise TypeError
                return selected_user
                # self._connection_close()
        except TypeError as exc:
            print(f'пользователь с таким логином не зарегистрирован')
            print('connection failed in function select_user')

        except Exception as exc:
            print(f'connection failed in function select_user, exception: {exc}')
            print(exc)

    def init_user(self, desktop_login: str, desktop_password: str) -> object:
        """Создаём объект класса юзер, если логин и пароль совпал.
        desktop_login - логин, который вводит пользователь с экрана,
        desktop_password - пароль, который вводит пользователь с экрана"""

        selected_user = self.select_user(desktop_login)
        if desktop_password == selected_user[3]:
            iduser = selected_user[0]
            login = selected_user[1]
            email = selected_user[2]
            password = selected_user[3]
            return User(iduser, login, email, password)

    def select_user_char(self, user: object) -> object:
        """Возвращает характеристики пользователя"""
        select_query = f"SELECT * FROM exercise.user_characteristic WHERE iduser = {user.iduser};"

        try:
            with self._connection.cursor() as cursor:
                cursor.execute(select_query)
                # self._connection_close()
                selected_user_char = cursor.fetchone()
                if selected_user_char is None:
                    raise TypeError
                return selected_user_char
                # self._connection_close()
        except TypeError as exc:
            print(f'пользователь с таким логином не зарегистрирован')
            print('connection failed in function select_user_char')
        except Exception as exc:
            print(f'connection failed in function select_user_char, exception: {exc}')
            print(exc)

    def init_user_char(self, user: object) -> object:
        """Создаём объект характеристик класса юзер"""

        selected_user_char = self.select_user_char(user)
        # dict={
        # 'iduser_characteristic': selected_user_char[0],
        # 'iduser': selected_user_char[1],
        # 'aim': selected_user_char[2],
        # 'level': selected_user_char[3],
        # 'days': selected_user_char[4],
        # 'muscule': selected_user_char[5],
        # 'male': selected_user_char[6],
        # 'height': selected_user_char[7],
        # 'weight': selected_user_char[8],
        # 'fat': selected_user_char[9],
        # 'day_counter': selected_user_char[10],
        # 'mark': selected_user_char[11],
        # 'weight_mult': selected_user_char[12],
        # 'number_mult': selected_user_char[13],
        # 'current_plan': selected_user_char[14]
        # }
        # return User_char(dict.values())

        iduser_characteristic = selected_user_char[0]
        iduser = selected_user_char[1]
        aim = selected_user_char[2]
        level = selected_user_char[3]
        days = selected_user_char[4]
        muscule = selected_user_char[5]
        male = selected_user_char[6]
        height = selected_user_char[7]
        weight = selected_user_char[8]
        fat = selected_user_char[9]
        day_counter = selected_user_char[10]
        mark = selected_user_char[11]
        weight_mult = selected_user_char[12]
        number_mult = selected_user_char[13]
        current_plan = selected_user_char[14]
        return User_char(iduser_characteristic, iduser, aim, level, days, muscule, male, height, weight, fat,
                         day_counter, mark, weight_mult, number_mult, current_plan)

    def del_user(self, id_user=2) -> None:
        """Добавляет нового пользователя в таблицу user"""

        delete_query = f"DELETE FROM exercise.user WHERE iduser={id_user};"

        try:
            with self._connection.cursor() as cursor:
                cursor.execute(delete_query)
                # чтобы сохранить в бд
                self._connection.commit()
                # self.connection_close()
                print('string is deleted')

        except Exception as exc:
            print(f'connection failed in function del_user, exception: {exc}')
            print(exc)

    def show_bd(self, table_name='user') -> None:
        """Принтует всю БД"""
        try:
            with self._connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM exercise.{table_name}")
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
                self._connection_lastid()

        except Exception as exc:
            print(f'connection failed in function show_bd, exception: {exc}')
            print(exc)

    def get_iduser(self, user: object) -> int:
        """Возвращает id юзера по логину"""
        try:
            select_query = f"SELECT iduser FROM exercise.user WHERE login=\"{user.login}\""
            with self._connection.cursor() as cursor:
                cursor.execute(select_query)
                return cursor.fetchone()[0]
        except Exception as exc:
            print(f'connection failed in function get_iduser, exception: {exc}')
            print(exc)

    def _connection_lastid(self, cursor):
        """Возвращает индекс последней добавленной строки"""

        try:
            last_id = cursor.lastrowid
            # if string wasn't added, we see an except
            if last_id == None:
                raise TypeError
            return last_id

        except TypeError as tr:
            print(f'{tr}. Function _connection_lastid. No string is added! ')

        except Exception as exc:
            print(f'connection failed in function _connection_lastid, exception: {exc}')
        finally:
            cursor.close()

    def _connection_commit(self):
        return self._connection.commit()

    def _connection_close(self):
        return self._connection.close()


if __name__ == "__main__":
    Tom = User(login='Tom', email='Tom.com', password='1II1')
    Jerry = User(login='Jerry', email='Jeronimo.ru', password='1VV1')
    # ex = Chest_ex()
    db = DB()
    # db.add_new_ex(ex)
    # db.add_new_user(Tom)
    # db.add_new_user(Jerry)
    # db.del_user(id_user=5)
    # print(db.get_iduser(Tom))
    # db.show_bd()
    # db.show_bd()
    # db.add_user_char(id_user=1, user_char=User_char())
    # print(db.select_user_char(Tom))
    print(db.init_user_char(Tom).all_stat())
    # Tom=db.init_user('Tom', '1II1')
    # print(Tom.email)

# db.add_new_ex(ex)
