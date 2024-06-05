# -*- coding: utf-8 -*-
from module.work_with_db import DB
import logging
db=DB()
class Exercise_Screen():

    @staticmethod
    def find_ex(ex_name: str)-> bool:
        """
        Ищет в БД упражнение, введенное пользователем
        :return: True, если такое упражнение есть в БД
        """
        if db.select_current_ex(ex_name):
            return True
        return False

# print(Exercise_Screen.find_ex('Жим штанги лёжа'))



