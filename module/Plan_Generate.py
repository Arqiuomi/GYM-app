from Class_About_User import User_Char
from Work_With_DB import DB
import random
import logging

logging.basicConfig(level=logging.INFO, filename='myapp.log', filemode='a',
                    format="%(module)s def %(funcName)s, %(levelname)s: %(message)s")
open('myapp.log', 'w')


def muscules(user_char: object) -> list:
    """Создаёт список из тех групп мышц, которые выбрал пользователь"""

    return user_char.muscule.split(",")


def train_from_bd(muscule: str) -> list:
    """Возвращает индексы всех тренировок на данную группу мышц из БД"""

    db = DB()
    tr_l = db.train_muscule(muscule=muscule)
    l = []
    for i in tr_l:
        l.append(i[0])
    return l


def choose_train_to_input(plan: list, muscule_list: list) -> list:
    """Выбирает случайную тренировку из тренирок из БД (train_from_bd)
    для каждой группы мышц (muscule_list) и добавляет её в план"""

    for muscule in muscule_list:
        plan = list(plan)
        train_list = train_from_bd(muscule)
        # индекс случайной тренировки из списка на данную группу мышц:
        i = random.randint(0, len(train_list) - 1)
        plan.append(train_list[i])
        # чтобы тренировки не повторялись, удаляем дубликаты
        plan = set(plan)
    return plan


def check_len_of_plan(plan) -> bool:
    """Возвращает True, если в тренировочном плане больше 4ёх тренировок"""
    if len(plan) < 4:
        return True
    return False


def plan_generate(user_char: object) -> list:
    """генерирует набор тренировок для юзера"""

    muscule_list = muscules(user_char)

    # Словарь для индексов тренировок
    plan = []

    plan = choose_train_to_input(plan, muscule_list)

    # Важно, чтобы в тренировочном цикле было не менее 4х различных тренировок
    while check_len_of_plan(plan):
        plan = choose_train_to_input(plan, muscule_list)

    return list(plan)





def check_plan(db: object, plan: list) -> bool:
    """Проверяет, есть ли тренировочный план c теми же тренировками в БД"""

    for i in db.select_all_plan():
        # Делаем срез без idplan
        if i[1::] == plan:
            return True
    return False




def init_plan(cp: bool, db: object, plan: list) -> int | None:
    """Если такой план есть, выводит idplan этого плана"""
    if cp:
        for i in db.select_all_plan():
            logging.info(f'сгенерированный план найден в БД!')
            # Делаем срез без idplan
            if i[1::] == plan:
                return i[0]
    logging.info(f'возможно, такого плана нет в БД. Попробуйте добавить его в БД')
    return None


def add_plan(cp: bool, db: object, plan)->int | None:
    """Если такого плана нет в БД, добавляет его в БД таблицу plan, выводит индекс этого плана"""
    if not cp:
        logging.info(f'добавляю сгенерированный план {plan} в БД')
        plan=db.prepare_plan(plan)
        return db.add_new_plan(plan)
    logging.info(f'возможно, этот план уже есть в БД')
    return None

def update_user_char_plan(idplan: int, user_char: object, cp: bool, db: object, plan):
    """Обновляет поле current_plan объекта класса user_char (характеристики пользователя).
    Т.к. на момент обновления, план обязан быть в БД, передаём только id нашего плана, используя ЗНАЧЕНИЕ функции init_plan"""
    try:
        if type(idplan)==int:
            user_char.current_plan=idplan
        elif type(idplan)==None:
            raise ValueError
    except ValueError:
        logging.warning(f'индекс такого плана не найден в БД. Попытка создать такой план и добавить в БД')
        add_plan(cp, db, plan)
    except Exception as exc:
        logging.error(f'не удалось обновить поле current_plan объекта user_char. {exc}')


def main():
    db = DB()
    # Вместо db_init_user должен быть объект класса user_char, созданный при входе в приложение
    tom = db.init_user(desktop_login='Tom', desktop_password='1II1')
    # # Глобальная переменная сгенерированного нами плана тренировок
    # plan=plan_generate(user_char=db.init_user_char(user=tom))
    # пробная попытка - ошибки в двойном подключении
    # tom_char=db.init_user_char(user=tom)
    # print(tom_char.current_plan)
    plan = [5, 6, 7, 8]
    char=User_Char()
    cp = check_plan(db, plan)
    ip = init_plan(cp, db, plan)
    ap = add_plan(cp, db, plan)
    print(ip)
    print(ap)
    update_user_char_plan(ip, char, cp, db, plan)
    print(char.current_plan)
    # print(db.prepare_plan(plan))
    # print(db.add_new_plan(plan))

main()

"""Файл для генерации плана тренировок в зависимости от запросов юзера"""

from Class_About_User import User_Char
from Work_With_DB import DB
import openpyxl as op
#
# class Plan_Generator():
#     def __init__(self, muscule: str, days: str):
#         """muscule - перечень мышц, на которые пользователь хочет сделать акцент"""
#
#         self.muscule=muscule.split(",")
#         self.days=days.split(",")
#
#
#     def day_number(self)->int:
#         """Подсчитывает, сколько тренировочных дней за 35-дневный цикл
#         Например, пользователь хочет тренироваться три раза в неделю.
#         Значит, за тренировочный цикл он потренируется 35/7*3 = 15 тренировок"""
#         return int(5*len(self.days))
#
#
#     def counter(func):
#         def wrapper(*args, **kwargs):
#             wrapper.count += 1
#             return func(*args, **kwargs)
#
#         wrapper.count = 0
#         return wrapper
#
#     @counter
#     def current_ex_name(db: object, train: object) -> str:
#         """Возвращает НАЗВАНИЕ текущего упражнения
#         ex_number - номер упражнения по ходу тренировки
#         db - экземпляр класса БД
#         current_train - текущая тренировка (из метода current_train класса Train)
#         """
#
#         train_l = db.select_current_train(train.current_train)
#         try:
#             # for discussion
#             if current_ex_name.count == 0:
#                 logging.info('It should be the first exercise in your train')
#                 return train_l[0]
#             logging.info(f'current exercise is {train_l[current_ex_name.count - 1]}')
#             return train_l[current_ex_name.count - 1]
#         except IndexError:
#             logging.error(f'error in current_ex_name. Perhaps, train contains no exercise')
#             print('проверь содержание тренировки')
#             return 'Жим штанги лёжа'
#         except Exception as exc:
#             logging.error(f'error in current_ex_name. Check the connection to the BD')
#             print(f'connection failed in function current_ex, exception: {exc}')
#             return 'Жим штанги лёжа'
#
#     def plan_general(self):
#         """Создаёт план из тренировок на всё тело"""
#         pass
#
# class Train_Generator():
#
#     def __init__(self, muscule:list):
#         """muscule - перечень мышц, на которые пользователь хочет сделать акцент"""
#         self.muscule=muscule


#
#
#
# plan = Plan_Generator('всё тело', 'Вт,Чт,Сб')
#


#
# # Важная штука для заполнения sql через xlsx
# class Excl(DB):
#     def demo(self, start_row: int, last_row: int):
#         wb = op.load_workbook('C:/Users/aelis/Documents/GitHub/GYM-app/tr.xlsx')
#         ws = wb.active
#         row = ws.iter_rows(min_row=start_row, max_row=last_row, values_only=True)
#         rv = [cell for cell in row]
#         print(rv)
#
#         for row in range(0, len(rv)):
#             name = rv[row][1]
#             muscule = rv[row][2]
#             number = rv[row][5]
#             weight = rv[row][6]
#             self._fill_DB(name, muscule, number, weight)
#
#         #     cell = ws.cell(row=row, column=2).value
#         #
#         #     self.fill_DB(cell, id)
#         #     id += 1
#         # cell=str(cell)
#
#     def _fill_DB(self, name, muscule, number, weight):
#         insert_query = f"INSERT INTO exercise.exercise_collection (name, muscule_type, number, weight)" \
#                        f" VALUES ('{name}', '{muscule}','{number}', '{weight}');"
#         # update_query = f"UPDATE exercise.exercise_collection SET weight=('{cell}') WHERE id_column = {id}"
#         try:
#             with self._connection.cursor() as cursor:
#                 cursor.execute(insert_query)
#                 # cursor.execute(update_query)
#                 # чтобы сохранить в бд
#                 self._connection.commit()
#         except Exception as exc:
#             print(f'connection failed in function fill_DB, exception: {exc}')
#             print(exc)
# excel = Excl()
# excel.demo(2, 5)


# class Excl(DB):
#     def demo(self):
#         wb = op.load_workbook('tr.xlsx')
#         ws = wb.active
#         id = 17
#         for row in range(26, 36):
#             cell = ws.cell(row=row, column=7).value
#             self.fill_DB(cell, id)
#             id += 1
#             # cell=str(cell)
#
#     def fill_DB(self, cell, id):
#         # insert_query = f"INSERT INTO exercise.exercise_collection (name)"  \
#         #                f" VALUES ('{cell}');"
#         update_query = f"UPDATE exercise.exercise_collection SET weight=('{cell}') WHERE id_column = {id}"
#         try:
#             with self._connection.cursor() as cursor:
#                 # cursor.execute(insert_query)
#                 cursor.execute(update_query)
#                 # чтобы сохранить в бд
#                 self._connection.commit()
#         except Exception as exc:
#             print(f'connection failed in function fill_DB, exception: {exc}')
#             print(exc)
# excel = Excl()
# excel.demo()

#

# Запросы для добавления из одной таблицы в другую:
# class Excl(DB):
#     def demo(self):
#
#         for i in range(1, 7):
#             id = i + 27
#             idtrain = 5
#             self.fill_DB(i, id, idtrain)
#
#         #     cell = ws.cell(row=row, column=2).value
#         #
#         #     self.fill_DB(cell, id)
#         #     id += 1
#         # cell=str(cell)
#
#     def fill_DB(self, i, id, idtrain):
#         # insert_query = f"INSERT INTO exercise.exercise_collection (name, muscule_type, number, weight)" \
#         #                f" VALUES ('{name}', '{muscule}','{number}', '{weight}');"
#         update_query = f"UPDATE exercise.train SET Ex{i}=(SELECT name FROM exercise.exercise_collection" \
#                        f" WHERE id_column = {id}) WHERE idtrain={idtrain}"
#         # insert_query = f"INSERT INTO exercise.train (Ex{i}) " \
#         #                f"VALUES (SELECT name FROM exercise.exercise_collection," \
#         #                f" WHERE id_column = {id})"
#         try:
#             with self._connection.cursor() as cursor:
#                 # cursor.execute(insert_query)
#                 cursor.execute(update_query)
#                 # чтобы сохранить в бд
#                 self._connection.commit()
#         except Exception as exc:
#             print(f'connection failed in function fill_DB, exception: {exc}')
#             print(exc)
