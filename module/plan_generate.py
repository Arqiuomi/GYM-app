import random
import logging
"""Генерирует тренировочный план для юзера. Если такой план есть в БД, 
присваивает юзеру (user_char.idplan) номер этого плана"""




logging.basicConfig(level=logging.INFO, filename='myapp.log', filemode='a',
                    format="%(module)s def %(funcName)s, %(levelname)s: %(message)s")
open('myapp.log', 'w')


def muscules(user_char: object) -> list:
    """Создаёт список из тех групп мышц, которые выбрал пользователь"""

    return user_char.muscule.split(",")


def train_from_bd(db: object, muscule: str) -> list:
    """Возвращает индексы всех тренировок на данную группу мышц из БД"""

    tr_l = db.train_muscule(muscule=muscule)
    l = []
    for i in tr_l:
        l.append(i[0])
    return l


def choose_train_to_input(db: object, plan: set, muscule_list: list) -> set:
    """Выбирает случайную тренировку из тренирок из БД (train_from_bd)
    для каждой группы мышц (muscule_list) и добавляет её в план"""

    for muscule in muscule_list:
        train_list = train_from_bd(db, muscule)
        # индекс случайной тренировки из списка на данную группу мышц:
        i = random.randint(0, len(train_list) - 1)
        plan.add(train_list[i])
    return plan


def check_len_of_plan(plan: set) -> bool:
    """Возвращает True, если в тренировочном плане больше 4ёх тренировок"""
    if len(plan) < 4:
        return True
    return False


def plan_generate(db: object, user_char: object) -> list:
    """
    Генерирует тренировочный план (набор тренировок) для юзера
    Parameters:
        объект свойства юзера
    Returns:
        тренировочный план
        """
    # Список приоритетных груп мышц пользователя
    muscule_list = muscules(user_char)

    # Множество (уникальных) индексов тренировок
    plan = set()

    plan = choose_train_to_input(db, plan, muscule_list)

    # Важно, чтобы в тренировочном цикле было не менее 4х различных тренировок
    while check_len_of_plan(plan):
        plan = choose_train_to_input(db, plan, muscule_list)
    # И вот тут множество становится списком
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
        logging.info(f'план добавлен в БД')
    except Exception as exc:
        logging.error(f'не удалось обновить поле current_plan объекта user_char. {exc}')



#тестовая функция для проверки, что функционал работает. Дополнительно нужно импортнуть класс DB и User_Char

# def test ():
#     from work_with_db import DB
#     from class_about_user import User_Char
#     from class_about_user import User
#     db = DB()
#     # Вместо db_init_user должен быть объект класса user_char, созданный при входе в приложение
#     tom = User.init_user(db, desktop_login='Tom', desktop_password='1II1')
#     # # Глобальная переменная сгенерированного нами плана тренировок
#     plan=plan_generate(db, user_char=User_Char.init_user_char(db, iduser=tom.iduser))
#     print(plan)
#     # пробная попытка - ошибки в двойном подключении
#     # tom_char=db.init_user_char(user=tom)
#     # print(tom_char.current_plan)
#     # plan = [5, 6, 7, 8]
#     # char=User_Char()
#     # print(plan)
#     # cp = check_plan(db, plan)
#     # ip = init_plan(cp, db, plan)
#     # ap = add_plan(cp, db, plan)
#     # print(ip)
#     # print(ap)
#     # update_user_char_plan(ip, char, cp, db, plan)
#     # print(char.current_plan)
#     # print(db.prepare_plan(plan))
#     # print(db.add_new_plan(plan))
#
# test()

