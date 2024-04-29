import logging

import mysql.connector
from config import data_base

logging.basicConfig(level=logging.INFO, filename='myapp.log', filemode='a',
                    format="%(module)s def %(funcName)s, %(levelname)s: %(message)s")

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

    @property
    def connection(self):
        return self._connection

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
            logging.info(f"connected to the DB")
            return connect

        except Exception as exc:
            print(f'connection failed in function connect, exception: {exc}')
            print(exc)
            logging.error(f'connection failed in function connect, exception: {exc}')

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
        """Добавляет в БД характеристики юзера"""

        insert_query = f"INSERT INTO exercise.user_characteristic (iduser, aim, level, days," \
                       f" muscule, male, height, weight, fat, day_counter, mark, weight_mult, number_mult, current_plan) " \
                       f"VALUES ({id_user}, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        try:
            with self._connection.cursor() as cursor:
                cursor.execute(insert_query, user_char.all_stat)
                # чтобы сохранить в бд
                # self._connection.commit()
                # self._connection_close() #- for what???
                print('string is added')
        except Exception as exc:
            print(f'connection failed in function add_user_char, exception: {exc}')
            print(exc)

    def select_user(self, desktop_login: str) -> list:
        """Выводит данные юзера ИЗ БД по логину
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

    def select_user_char(self, iduser: int) -> list:
        """Возвращает характеристики пользователя ИЗ БД"""
        select_query = f"SELECT * FROM exercise.user_characteristic WHERE iduser = {iduser};"
        logging.info(f"table user.char is connected")

        try:
            with self._connection.cursor() as cursor:
                cursor.execute(select_query)
                selected_user_char = cursor.fetchone()
                if selected_user_char is None:
                    raise TypeError
                return selected_user_char

        except TypeError as exc:
            print(f'пользователь с таким логином не зарегистрирован')
            print('connection failed in function select_user_char')
        except Exception as exc:
            print(f'connection failed in function select_user_char, exception: {exc}')
            print(exc)

    def select_сurrent_plan(self, idplan: int) -> list:
        """
        Возвращает ИЗ БД текущий план тренировок в виде списка.
            На вход принимает индекс нужного плана
        """

        select_query = f"SELECT * FROM exercise.plan WHERE idplan = {idplan};"
        try:
            with self._connection.cursor() as cursor:
                cursor.execute(select_query)
                selected_plan = cursor.fetchone()
                if selected_plan is None:
                    raise TypeError
                # Теперь мы возвращаем строку с индексом и всеми None
                # selected_plan = self.clear_selected_plan(list(selected_plan))
                return selected_plan
        except TypeError:
            print(f'такого плана тренировок не существует')
            print('connection failed in function select_current_plan')
        except Exception as exc:
            print(f'connection failed in function select_current_plan, exception: {exc}')

    # Уехал в класс Plan
    # def clear_selected_plan(self, l: list) -> list:
    #     """Внутренний метод класса.
    #     Очищает строчку из таблицы "plan" от индеска строки и всех None.
    #     Остаются только номера тренировок"""
    #
    #     l.pop(0)
    #     c = l.count(None)
    #     for i in range(0, c):
    #         l.remove(None)
    #     return l

    def select_current_train(self, idtrain: int) -> list:
        """Выводит из БД информацию о текущей тренировке"""
        select_query = f"SELECT * FROM exercise.train WHERE idtrain = {idtrain};"
        try:
            with self._connection.cursor() as cursor:
                cursor.execute(select_query)
                # self._connection_close()
                selected_train = cursor.fetchone()
                if selected_train is None:
                    raise TypeError
                selected_plan = self.clear_selected_train(list(selected_train))
                return selected_plan
                # self._connection_close()
        except TypeError as exc:
            print(f'такой тренировки не существует')
            print('connection failed in function select_current_train')
        except Exception as exc:
            print(f'connection failed in function select_current_plan, exception: {exc}')

    def select_current_ex(self, name: str) -> list:
        """Выводит из БД информацию о текущем упражнении """
        select_query = f"SELECT * FROM exercise.exercise_collection WHERE name = '{name}';"
        try:
            with self._connection.cursor() as cursor:
                cursor.execute(select_query)
                # self._connection_close()
                selected_ex = cursor.fetchone()
                if selected_ex is None:
                    raise TypeError
                selected_plan = list(selected_ex)
                self._connection_close()
                return selected_plan
        except TypeError as exc:
            print(f'такой тренировки не существует')
            print('connection failed in function select_current_ex')
        except Exception as exc:
            print(f'connection failed in function select_current_plan, exception: {exc}')

    def train_muscule(self, muscule: str) -> list:
        """Выводит список id-тренировок по данной группе мышц"""

        try:
            with self._connection.cursor() as cursor:
                cursor.execute(f"SELECT idtrain FROM exercise.train where muscule_type='{muscule}';")
                train_muscule = cursor.fetchall()
                if train_muscule is None:
                    raise TypeError
                return train_muscule
                # self._connection_close()
        except TypeError as exc:
            logging.warning('тренировки на такую группу мышц не существует')
            return [1, 2, 3, 4, 5]
        except Exception as exc:
            logging.warning('тренировки на такую группу мышц не существует')
            return [1, 2, 3, 4, 5]
        # finally:
        #     self._connection_close()

    def select_all_plan(self) -> list:
        """Выводит из БД все тренировочные планы"""
        select_query = f"SELECT * FROM exercise.plan;"
        try:
            with self._connection.cursor() as cursor:
                cursor.execute(select_query)
                # self._connection_close()
                all_plan = cursor.fetchall()
                if all_plan is None:
                    raise TypeError
                # Очищаем полученные вложенные кортежи от None. Преобразуем кортежи в списки. Первым идёт idplan!!!
                for i in range(len(all_plan)):
                    all_plan[i] = self.clear_all_plan(list(all_plan[i]))
                return all_plan
        except TypeError as exc:
            print(f'такого плана тренировок не существует')
            print('connection failed in function select_all_plan')
        except Exception as exc:
            print(f'connection failed in function select_all_plan, exception: {exc}')

    def clear_all_plan(self, l: list) -> list:
        """Внутренний метод класса.
        Очищает строчку из таблицы "plan" от всех None.
        Остаются только номера тренировок и idplan"""

        c = l.count(None)
        for i in range(0, c):
            l.remove(None)
        return l

    def prepare_plan(self, plan) -> list:
        """Проверяет, сколько тренировок в плане, если меньше 7, заполняет None"""
        while len(plan) < 7:
            plan.append('NULL')
        return plan

    def add_new_plan(self, plan) -> int:
        """Добавляет новый тренировочный план в таблицу plan.
        Возвращает idplan последнего добавленного плана"""
        plan = self.prepare_plan(plan)
        insert_query = f"INSERT INTO exercise.plan (T1, T2, T3, T4, T5, T6, T7)" \
                       f" VALUES ({plan[0]}, {plan[1]}, {plan[2]}, {plan[3]}, {plan[4]}, " \
                       f"{plan[5]}, {plan[6]});"

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
            print(f'connection failed in function add_new_plan, exception: {exc}')
            print(exc)

    def clear_selected_train(self, l: list) -> list:
        """Внутренний метод класса.
        Очищает строчку из таблицы "train" от индеска строки, типа мыщц и всех None.
        Остаются только номера тренировок"""
        l.pop(0)
        l.pop(0)
        c = l.count(None)
        for i in range(0, c):
            l.remove(None)
        return l

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

    def show_bd(self, table_name='user') -> list:
        """Принтует всю БД"""
        try:
            with self._connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM exercise.{table_name}")
                rows = cursor.fetchall()
                self._connection_lastid(cursor)
                return rows

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
    # ex = Chest_Ex()
    db = DB()
    # db.add_new_ex(ex)
    # db.add_new_user(Tom)
    # db.add_new_user(Jerry)
    # db.del_user(id_user=5)
    # print(db.get_iduser(Tom))
    print(db.show_bd())
    # db.show_bd()
    # print(db.select_user_char(Tom))

