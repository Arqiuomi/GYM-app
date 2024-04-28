# from common_func import train_start
# from init_func import train_start
from user_char_const import d_mark, d_aim_mult, d_male_mult, d_level_mult
import logging

"""Файл содержит класс User и класс User_Char - пользователь и характеристики пользователя"""

logging.basicConfig(level=logging.INFO, filename='myapp.log', filemode='a',
                    format="%(module)s def %(funcName)s, %(levelname)s: %(message)s")


class User():

    def __init__(self, iduser: object = '1', login: object = 'log', email: object = 'email',
                 password: object = 'pswrd') -> object:
        self.iduser = iduser
        self.login = login
        self.email = email
        self.password = password

    def init_user(db: object, desktop_login: str, desktop_password: str) -> object:
        """Создаём ОБЪЕКТ класса юзер, если логин и пароль совпал.
        desktop_login - логин, который вводит пользователь с экрана,
        desktop_password - пароль, который вводит пользователь с экрана"""
        try:
            selected_user = db.select_user(desktop_login)
            if desktop_password == selected_user[3]:
                iduser = selected_user[0]
                login = selected_user[1]
                email = selected_user[2]
                password = selected_user[3]
                logging.debug(f"user's login is {selected_user[1]}")
                return User(iduser, login, email, password)
        except TypeError:
            logging.warning(f"пользователь не прошёл аутентификацию")
            return User()
        except Exception:
            logging.error(f"неизвестная ошибка при аутентификации пользователя")
            return User()

    def iduser(self):
        # DB.get_iduser(self)
        pass

    # @set


class User_Char():
    # Константы среднестатистического Гэндальфа
    H, W, FAT = 180, 80, 10

    def __init__(self, iduser_characteristic='1', iduser='1', aim=1, level=1, days='Вт,Чт,Сб', muscule='всё тело',
                 male='М', height=178.3, weight=100.1, fat=15.5, day_counter=0, mark=0, weight_mult=1.1,
                 number_mult=1.1,
                 current_plan=1):
        self.iduser_characteristic = iduser_characteristic
        self.iduser = iduser
        self.aim = aim
        self.level = level
        self.days = days
        self.muscule = muscule
        self.male = male
        self.height = height
        self.weight = weight
        self.fat = fat
        self.day_counter = day_counter
        self.mark = mark
        self.weight_mult = weight_mult
        self.number_mult = number_mult
        self.current_plan = current_plan
        self.all_stat = self.all_stat()

    def init_user_char(db, iduser: int) -> object:
        """Создаём ОБЪЕКТ характеристик класса юзер"""
        selected_user_char = db.select_user_char(iduser)
        return User_Char(*selected_user_char)

    def all_stat(self) -> list:
        """Все характеристики класса"""
        return [
            self.aim,
            self.level,
            self.days,
            self.muscule,
            self.male,
            self.height,
            self.weight,
            self.fat,
            self.day_counter,
            self.mark,
            self.weight_mult,
            self.number_mult,
            self.current_plan
        ]

    def day_counter(self, train_start: bool) -> int:
        """Подсчитывает число выполненных тренировок за месяц"""
        if train_start():
            self.day_counter += 1
            return self.day_counter

            pass

    def set_mark(self, key: str) -> int:
        """Добавляет в суммарную оценку юзера текущую оценку тренировки"""
        self.mark += d_mark[key]
        return self.mark

    def set_weight_mult(self) -> float:
        """Устанавливает значение множителя веса"""
        p1 = 0.8
        p2 = 0.9
        self.weight_mult = d_male_mult[self.male] * d_level_mult[self.level] * d_aim_mult[self.aim]

        return round(self.weight_mult, 2)

    def set_number_mult(self) -> float:
        """Устанавливает значение множителя повторений"""
        p1 = 0.7
        p2 = 0.8

        self.number_mult = d_male_mult[self.male] * d_level_mult[self.level] * d_aim_mult[self.aim] * (
                p1 * self.height / User_Char.H +
                +p2 * self.weight * (100 - self.fat) / (User_Char.W * (100 - User_Char.FAT)))
        return round(self.number_mult, 2)

    def crete_train(self):
        """Создаёт тренировку из списка упражнений в БД, """
        pass

    def current_plan(self):
        """Подбирает оптимальный план по запросам юзера: целевые мышцы, количество дней в неделю"""

        pass

    def update_day_counter(self):
        """Обновление числа завершённых тренировок в объекте класса характеристики пользователя"""
        self.day_counter = self.day_counter + train_start.count


def mark(key: str) -> int:
    """Возвращает оценку тренировки"""

    return d_mark[key]
