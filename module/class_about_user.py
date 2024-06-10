# from common_func import train_start
# from init_func import train_start
from module.user_char_const import d_mark, d_aim_mult, d_male_mult, d_level_mult
import logging
from module.work_with_db import DB


"""Файл содержит класс User и класс User_Char - пользователь и характеристики пользователя"""

logging.basicConfig(level=logging.INFO, filename='myapp.log', filemode='a',
                    format="%(module)s def %(funcName)s, %(levelname)s: %(message)s")


class User():

    def __init__(self, iduser='1', login='log', email='email',
                 password='pswrd') -> object:
        self.iduser = iduser
        self.login = login
        self.email = email
        self.password = password


class User_Char():
    # Константы среднестатистического Гэндальфа
    H, W, FAT = 180, 80, 10
    n1 = 0.7
    n2 = 0.8

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
        self._mark = mark
        self.weight_mult = weight_mult
        self.number_mult = number_mult
        self.current_plan = current_plan
        self.all_stat = self.all_stat()

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

    @property
    def mark(self):
        return self._mark

    @mark.setter
    def mark(self, key: str) -> int:
        """Добавляет в суммарную оценку юзера текущую оценку тренировки"""
        self._mark += d_mark[key]

    def set_weight_mult(self) -> float:
        """Устанавливает значение множителя веса"""

        self.weight_mult = d_male_mult[self.male] * d_level_mult[self.level] * d_aim_mult[self.aim]

        return round(self.weight_mult, 2)

    def set_number_mult(self) -> float:
        """Устанавливает значение множителя повторений"""

        self.number_mult = d_male_mult[self.male] * d_level_mult[self.level] * d_aim_mult[self.aim] * (
                User_Char.n1 * self.height / User_Char.H +
                +User_Char.n2 * self.weight * (100 - self.fat) / (User_Char.W * (100 - User_Char.FAT)))
        return round(self.number_mult, 2)

    def crete_train(self):
        """Создаёт тренировку из списка упражнений в БД, """
        pass

    def current_plan(self):
        """Подбирает оптимальный план по запросам юзера: целевые мышцы, количество дней в неделю"""

        pass

# Тест декоратора
# tom= User_Char()
# print(tom.mark)
# tom.mark = 'легко'
# print(tom.mark)
