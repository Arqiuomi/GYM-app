# -*- coding: utf-8 -*-

from module.work_with_db import DB
import logging
from module.class_about_user import User, User_Char
from module.train import train_main

db = DB()
user_char = User_Char()


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
    #     train_main(db, user_char)
    #     return {'name': train_main.ex_name, 'number_of_ex': train_main.number_of_ex,
    #             'weight': train_main.weight, 'number': train_main.number}
    #
    # # Словарь с информацией о тренировке
    #
    # all_inf = take_all_inf()
    @staticmethod
    def take_ex_name() -> str:
        """Возвращает название упражнения.
        train_main - основная функция, запускаемая при начале тренировки"""
        train_main(db, user_char)
        return train_main.ex_name

    @staticmethod
    def take_number_of_ex() -> int:
        """
        :return: Число упражнений в текущей тренировке
        """
        train_main(db, user_char)
        return train_main.number_of_ex

    @staticmethod
    def take_ex_info() -> list:
        """

        :return: возвращает список с весом и числом повторений
        """
        train_main(db, user_char)

        return [train_main.weight, train_main.number]

    @staticmethod
    def train_finish():
        # передаёт в модуль, что тренировка завершена.
        # Возможно, понадобиться ещё 1 файлик контроллера.
        pass

# print(Exercise_Screen.take_full_descr('Жим штанги лёжа'))
# print(Exercise_Screen.find_ex('Жим штанги лёжа'))

# tr = Tr_St_Screen()
#
# print(tr.take_number_of_ex())
# print(tr.take_ex_info())
# print(tr.take_ex_info())
