# -*- coding: utf-8 -*-
"""Файл-контроллер для взаимодействия основных окон приложения
с модулем"""

from module.work_with_db import DB
import logging
from module.class_about_user import User, User_Char
from module.train import train_main
from module.train import current_ex_name

# Тут должен быть логин, который передаётся с экрана!!!!!
with open('desktop_login_name.txt', 'r', encoding='UTF-8') as file:
    desktop_login = file.readline()

db = DB()
# Создаём объект юзера по логину, который ввёл пользователь.
user = User(*db.select_user(desktop_login))
print('final login is ', user.login)
# Создаём класс характеристик юзера;
# запрашиваем информацию из БД по id юзера
user_char = User_Char(*db.select_user_char(user.iduser))

# Вызываем функцию, чтобы началось первое упражнение
train_main(db, user_char)


class Exercise_Screen():

    @staticmethod
    def find_ex(ex_name: str) -> bool:
        """
        Ищет в БД упражнение, введенное пользователем
        :return: True, если такое упражнение есть в БД
        """
        if db.select_current_ex(ex_name):
            return True
        return False

    @staticmethod
    def take_short_descr(name: str) -> str | None:
        """
        :param name: название упражнения как в БД
        :return: короткое описание упражнения из БД
        """
        return db.select_current_ex(name)[3]

    @staticmethod
    def take_full_descr(name: str) -> str | None:
        """
        :param name: название упражнения как в БД
        :return: развернутое описание упражнения из БД
        """
        return db.select_current_ex(name)[4]


class Tr_St_Screen():

    # @staticmethod
    # def take_all_inf() -> dict:
    #     """
    #     Возвращает словарь со всеми характеристиками тренировки
    #     :return: name - название упражнения,
    #     number_of_ex - число упражнений в тренировке,
    #     weight - вес в подходе
    #     number - кол-во повторений в подходе
    #     """
    #
    #     return {'name': train_main.ex_name, 'number_of_ex': train_main.number_of_ex,
    #             'weight': train_main.weight, 'number': train_main.number}

    @staticmethod
    def call_train():
        """Вызывает функцию тренировки"""
        return train_main(db, user_char)

    @staticmethod
    def ex_counter():
        return current_ex_name.count

    @staticmethod
    def take_ex_name() -> str:
        """Возвращает название упражнения.
        train_main - основная функция, запускаемая при начале тренировки"""
        return train_main.ex_name

    @staticmethod
    def take_number_of_ex() -> int:
        """
        :return: Число упражнений в текущей тренировке
        """
        return train_main.number_of_ex

    @staticmethod
    def take_ex_info() -> list:
        """

        :return: возвращает список с весом и числом повторений
        """
        return [train_main.weight, train_main.number]

    @staticmethod
    def train_finish():
        # передаёт в модуль, что тренировка завершена.
        # Возможно, понадобиться ещё 1 файлик контроллера.
        pass

