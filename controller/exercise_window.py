# -*- coding: utf-8 -*-
from module.work_with_db import DB
import logging

db = DB()


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
    def take_short_descr(name: str) -> str:
        """

        :param name: название упражнения как в БД
        :return: короткое описание упражнения из БД
        """
        return db.select_current_ex(name)[3]

    @staticmethod
    def take_full_descr(name: str) -> str:
        """
        :param name: название упражнения как в БД
        :return: развернутое описание упражнения из БД
        """
        return db.select_current_ex(name)[4]


# print(Exercise_Screen.take_full_descr('Жим штанги лёжа'))
# print(Exercise_Screen.find_ex('Жим штанги лёжа'))
