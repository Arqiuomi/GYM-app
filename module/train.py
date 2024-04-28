from work_with_db import DB
from class_exercise import Exercise
import logging
# from class_about_user import User_Char
# from common_func import counter
# from common_func import train_start


class Plan():
    def __init__(self, muscule: str, days: str, day_counter: int):
        """muscule - перечень мышц, на которые пользователь хочет сделать акцент
            days - Дни, которые пользователь выбрал для тренировки
            day_counter - число дней, которые пользователь тренировался в цикле (информация из БД)
        """

        self.muscule = muscule.split(",")
        self.days = days.split(",")
        self.day_counter = day_counter

    def day_number(self) -> int:
        """Подсчитывает, сколько всего тренировочных дней за 35-дневный цикл
        Например, пользователь хочет тренироваться три раза в неделю.
        Значит, за тренировочный цикл он потренируется 35/7*3 = 15 тренировок"""
        return int(5 * len(self.days))

    def plan_update(self):
        """Проверяет, закончился ли тренировочный цикл по данному плану"""
        if self.day_counter > self.day_number():
            return True
        return False

    def plan_general(self):
        """Создаёт план из тренировок на всё тело"""
        pass


class Train():
    def __init__(self, current_plan: list, day_counter: int):
        """current_plan, day_counter - атрибуты класса характиеристики юзера (информация из БД)"""

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
    """Возвращает НАЗВАНИЕ текущего упражнения
    ex_number - номер упражнения по ходу тренировки
    db - экземпляр класса БД
    current_train - текущая тренировка (из метода current_train класса Train)
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


def current_ex(ex_name: str, db: object) -> object:
    """Создаёт объект класса Exercise - упражнение из БД"""
    try:
        return db.init_ex(ex_name)
    except AttributeError:

        logging.error(f'Def current_ex, error {AttributeError}. Check the init_ex in the class DB.')
        return Exercise(1, 'Жим штанги лёжа', 'грудь', 'description', 'full_description', 5, 80)

    except Exception as exc:
        logging.error(f'Def current_ex, error {exc}. Check the connection to the BD.\\ '
                      f'Check the name in tables exercise_collection and train')
        return


@counter
def train_start(event=True) -> bool:
        """Начинается тренировка тренировку"""
        if event:
            return True
        return False

# Обновление характеристик юзера
# def update_day_counter(user_char: object):
#     """Обновление числа завершённых тренировок в объекте класса характеристики пользователя"""
#     user_char.day_counter = user_char.day_counter+train_start.count


def plan_main():
    # plan = Plan('всё тело', 'Вт,Чт,Сб')
    pass


def train_main():
    # Перед запуском очищаем log
    open('myapp.log', 'w')
    # Задаём настройки Log-файла
    logging.basicConfig(level=logging.INFO, filename='myapp.log', filemode='a',
                        format="%(module)s def %(funcName)s %(levelname)s: %(message)s")
    db = DB()
    Tom = db.init_user(desktop_login='Tom', desktop_password='1II1')
    print(Tom.email)
    Tom_char = db.init_user_char(Tom)

    tr = Train(db.select_сurrent_plan(idplan=1), Tom_char.day_counter)
    # print(db.select_сurrent_plan(idplan=1))
    # print(Tom_char.day_counter)
    # print(tr.current_train)
    # print(db.select_current_train(tr.current_train))
    # ex_name=current_ex_name(1, db,tr)

    # строка для теста декоратора
    ex_name = current_ex_name(db, tr)

    print(current_ex_name.count)

    ex = current_ex(ex_name, db)

    print(ex.name)
    print(ex.weight)
    ex.create_personal_ex(Tom_char)
    print(ex.weight)


if __name__ == '__main__':
    # train_main()
    # plan_main()
    # Эта строка должна быть в файле main, откуда будет запускаться вся программа!!!
    open('myapp.log', 'w')
    db = DB()
    print(db.show_bd())
    print(db.select_user('Tom'))

    tom = db.init_user(desktop_login='Tom', desktop_password='1II1')
    print(tom.login)

    Tom_char = db.init_user_char(tom)
    print(f' число дней {Tom_char.day_counter}')
    ## тест counter для дней тренировок
    train_start(True)
    print(train_start.count)
    Tom_char.update_day_counter()
    print(f' число дней {Tom_char.day_counter}')
    # # train_start(True)
    # print(train_start.count)
