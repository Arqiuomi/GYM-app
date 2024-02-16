import mysql.connector
from config import data_base
from Class_exercise import Chest_ex
from Class_user import User


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

    def add_new_ex(self, ex: object) -> None:
        """Добавляет новое упражнение в таблицу chest_exercise"""

        insert_query = f"INSERT INTO exercise.chest_exercise (name, description, full_description, number, weight)" \
                       f" VALUES (\"{ex.name}\", \"{ex.description}\", \"{ex.ful_desc}\", {ex.number}, {ex.weight});"

        try:
            with self._connection.cursor() as cursor:
                cursor.execute(insert_query)
                # чтобы сохранить в бд
                self._connection.commit()
                # self._connection_close() - for what???
                print('string is added')

        except Exception as exc:
            print(f'connection failed in function add_new_ex, exception: {exc}')
            print(exc)

    def add_new_user(self, user: object) -> None:
        """Добавляет нового пользователя в таблицу user"""

        insert_query = f"INSERT INTO exercise.user (login, email, password)" \
                       f" VALUES (\"{user.login}\", \"{user.email}\", \"{user.password}\");"

        try:
            with self._connection.cursor() as cursor:
                cursor.execute(insert_query)
                # чтобы сохранить в бд
                self._connection.commit()
                # self._connection_close()
                print('string is added')

        except Exception as exc:
            print(f'connection failed in function add_new_user, exception: {exc}')
            print(exc)
    def get_iduser(self, user: object)->int:
        """Возвращает id юзера в таблице user"""
        try:
            select_query=f"SELECT iduser FROM exercise.user WHERE login=\"{user.login}\""
            with self._connection.cursor() as cursor:
                cursor.execute(select_query)
                return cursor.fetchone()[0]
        except Exception as exc:
            print(f'connection failed in function get_iduser, exception: {exc}')
            print(exc)

    def add_new_train(self, train: object) -> None:
        """Добавляет в таблицу train новую строчку"""

        insert_query = f"INSERT INTO exercise.train (day_counter, mark, weight_mult, number_mult)" \
                       f" VALUES (\"{train.day_counter}\", \"{train.mark}\", \"{train.weight_mult}\", " \
                       f"\"{train.number_mult}\");"

        try:
            with self._connection.cursor() as cursor:
                cursor.execute(insert_query)
                # чтобы сохранить в бд
                self._connection.commit()
                # self._connection_close()
                print('string is added')

        except Exception as exc:
            print(f'connection failed in function add_new_user, exception: {exc}')
            print(exc)

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

        except Exception as exc:
            print(f'connection failed in function show_bd, exception: {exc}')
            print(exc)

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
    print(db.get_iduser(Tom))

    db.show_bd()
    # db.show_bd()
    # db.add_new_ex(ex)
