from work_with_db import DB
from class_about_user import User, User_Char
from class_exercise import Exercise
from plan_generate import *
import logging


class Plan():
    def __init__(self, idplan, T1, T2, T3, T4, T5, T6, T7):
        """
        Parameters:
            idplan - индекс тренировочного плана
            T_i - индекс тренировки в таблице тренировок (может быть None)
        """
        self.idplan = idplan
        self.T1 = T1
        self.T2 = T2
        self.T3 = T3
        self.T4 = T4
        self.T5 = T5
        self.T6 = T6
        self.T7 = T7

    def init_plan(db, idpan) -> object:
        """
        Создаёт объект класса Plan по данным из БД

        :param db:
            База данных
        :param idpan:
            индекс плана
        :return :
            объект класса Plan
        """
        selected_plan = db.select_сurrent_plan(idpan)
        return Plan(*selected_plan)

    def all_stat(self) -> list:
        """
        Выводит статистику об объекте Plan
        :return:
            свойства объекта ввиде списка
        """
        return [
            self.idplan,
            self.T1,
            self.T2,
            self.T3,
            self.T4,
            self.T5,
            self.T6,
            self.T7
        ]

    def clear_plan(self) -> list:
        """
            Очищает "plan" от индеска строки и всех None. Остаются только номера тренировок
         :return:
            Список индексов тренировок из текущего плана.
        """
        l = self.all_stat()
        l.pop(0)
        c = l.count(None)
        for i in range(0, c):
            l.remove(None)
        return l

    def train_days(self, user_char: object) -> int:
        """Подсчитывает, сколько всего тренировочных дней за 35-дневный цикл.
        Например, пользователь хочет тренироваться три раза в неделю.
        Значит, за тренировочный цикл он потренируется 35/7*3 = 15 тренировок"""
        days = user_char.days.split(",")
        return int(5 * len(days))

    def cycle_check(self, user_char: object):
        """Проверяет, закончился ли тренировочный цикл по данному плану"""
        t_d = self.train_days(user_char)
        if user_char.day_counter > t_d:
            return True
        return False

    def update_plan(self, db: object, user_char: object):
        """Обновляет тренировочный план"""
        plan = plan_generate(user_char)
        cp = check_plan(db, plan)
        if cp:
            ip = init_plan(cp, db, plan)
        else:
            ip = add_plan(cp, db, plan)
        update_user_char_plan(ip, user_char, cp, db, plan)


class Train():
    def __init__(self, current_plan: list, day_counter: int):
        """
        Parameters:
            current_plan - список тренировок из тренировочного плана (результат clear_plan() )
            day_counter - атрибут класса характиеристики юзера (информация из БД)"""

        self.current_plan = current_plan
        self.day_counter = day_counter
        self.current_train = self.current_train()
        logging.info(
            f"New Train was created. Train info current_plan={self.current_plan}, day_counter={self.day_counter},"
            f"current_train= {self.current_train}")

    # Определение тренировки
    def current_train(self) -> int:
        """Определяет текущую тренировку из тренировачного плана по кол-ву проведённых тренировок"""
        try:
            if self.day_counter >= len(self.current_plan):
                return self.current_plan[
                    self.day_counter - (self.day_counter // len(self.current_plan)) * len(self.current_plan)]
            return self.current_plan[self.day_counter]
        except IndexError:
            logging.warning(f"IndexError in class Train() method current_train(). New value of train is 0")
            print('проверь содержание плана тренировок')
            return 0
        except Exception as exc:
            logging.error(f"{exc} in class Train() method current_train(). New value of train is 0")
            print(f'connection failed in function current_train class Train, exception: {exc}')
            return 0


def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper


@counter
def current_ex_name(db: object, train: object) -> str:
    """
    Возвращает НАЗВАНИЕ текущего упражнения
    Parameters:
        db - экземпляр класса БД
        train - текущая тренировка (из метода current_train класса Train)
    """

    train_l = db.select_current_train(train.current_train)
    try:
        # for discussion
        if current_ex_name.count == 0:
            logging.info('It should be the first exercise in your train')
            return train_l[0]
        logging.info(f'current exercise is {train_l[current_ex_name.count - 1]}')
        return train_l[current_ex_name.count - 1]
    except IndexError:
        logging.error(f'error in current_ex_name. Perhaps, train contains no exercise')
        print('проверь содержание тренировки')
        return 'Жим штанги лёжа'
    except Exception as exc:
        logging.error(f'error in current_ex_name. Check the connection to the BD')
        print(f'connection failed in function current_ex, exception: {exc}')
        return 'Жим штанги лёжа'


# def current_ex(ex_name: str, db: object) -> object:
#     """
#     Создаёт объект класса Exercise - упражнение из БД
#     Returns:
#         объект класса Exercise
#     """
#     try:
#         return db.init_ex(ex_name)
#     except AttributeError:
#
#         logging.error(f'Def current_ex, error {AttributeError}. Check the init_ex in the class DB.')
#         return Exercise(1, 'Жим штанги лёжа', 'грудь', 'description', 'full_description', 5, 80)
#
#     except Exception as exc:
#         logging.error(f'Def current_ex, error {exc}. Check the connection to the BD.\\ '
#                       f'Check the name in tables exercise_collection and train')
#


@counter
def train_start(event=True) -> bool:
    """Начинается тренировка тренировку"""
    if event:
        return True
    return False


# Обновление характеристик юзера
def update_day_counter(user_char: object):
    """Обновление числа завершённых тренировок в объекте класса характеристики пользователя"""
    user_char.day_counter = user_char.day_counter + train_start.count


def plan_main(db, user_char):
    current_plan = Plan.init_plan(db, user_char.current_plan)

    list_of_trains = current_plan.clear_plan()

    if current_plan.cycle_check():
        current_plan.update_plan(db, user_char)


def train_main(db, user_char):

    current_plan = Plan.init_plan(db=db, idpan=user_char.current_plan)
    list_of_trains = current_plan.clear_plan()

    tr = Train(list_of_trains, user_char.day_counter)

    # строка для теста декоратора
    ex_name = current_ex_name(db, tr)
    # каждый раз новое упражнение
    ex_name = current_ex_name(db, tr)
    # каждый раз новое упражнение
    ex_name = current_ex_name(db, tr)

    # Для тестов
    print(current_ex_name.count)
    ex = Exercise.init_ex(db, ex_name)
    print(ex.name)
    print(ex.weight)
    ex.create_personal_ex(tom_char)
    print(ex.weight)


if __name__ == '__main__':
    # Эта строка должна быть в файле main, откуда будет запускаться вся программа!!!
    #Создание log-файла
    open('myapp.log', 'w')
    # Настройки log-файла
    logging.basicConfig(level=logging.INFO, filename='myapp.log', filemode='a',
                        format="%(module)s def %(funcName)s %(levelname)s: %(message)s")
    # Для теста
    db = DB()
    tom = User.init_user(db, desktop_login='Tom', desktop_password='1II1')
    tom_char = User_Char.init_user_char(db, tom.iduser)
    train_main(db, tom_char)



