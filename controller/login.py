# -*- coding: utf-8 -*-
from module.work_with_db import DB
import logging

logging.basicConfig(level=logging.INFO, filename='myapp.log', filemode='a',
                    format="%(module)s def %(funcName)s, %(levelname)s: %(message)s")

db = DB()


class Login():
    @staticmethod
    def user_from_bd(username: str) -> list:
        """
        Проверяет, зарегестрирован ли пользователь, в БД он или нет
        :param username: имя искомого пользователя
        :return: True, если такой пользователь есть в БД
        """
        try:
            bd_user_data = db.select_user(username)
            if type(bd_user_data) is None:
                raise TypeError
            return bd_user_data
        except TypeError:
            print('Логин пользователя в БД не найден')
            return [1, 1, 1, 1]
        except Exception:
            print('Логин пользователя в БД не найден')
            return [1, 1, 1, 1]

    @staticmethod
    def check_user(d: dict) -> bool:
        """
        Проверяет, совпал ли введённый пароль с паролем пользователя в БД
        :param d: словарь с логином и паролем юзера, переданные через интерфейс
        :return: да, если пароль совпал со значениями в БД
        """
        bd_user_data = Login.user_from_bd(d['username'])
        try:
            if bd_user_data[3] == d['password']:
                return True
            return False
        except Exception:
            logging.warning('в интерфейс введён некорректный логин')


class Registration():
    user_char = {'aim': 1, 'level': 1, 'days': 'Вт,Чт,Сб', 'muscule': 'всё тело', 'male': 'М',
                 'height': 178.3, 'weight': 100.1, 'fat': 15.5}

    user = {'login': 'log', 'email': 'email', 'password': 'pswrd'}
