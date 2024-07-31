from kivy.app import App
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from controller.login import Login
from controller.login import Registration
# from menu_screen import MenuApp
# import os
# import subprocess


class EnterScreen(Screen):
    pass


class LoginScreen(Screen):

    def user_login(self) -> dict:
        """
        Передаёт логин и пароль пользователя в контроллер на проверку
        :return: словарь с логином и паролем, введённым через интерфейс
        """
        return {'username': self.ids.username.text, 'password': self.ids.password.text}

    def confirm(self):
        """Проверяет введённые данные, в случае успешной проверки входит в аккаунт"""

        if Login.check_user(self.user_login()):
            # Была идея создать метод для обновления логина
            # Login.update_login(self.user_login()['username'])
            print(f'self login is {self.user_login()["username"]}')
            print('sucsess!')
            self.ids.confirm.text = 'sucsess!'
            with open('desktop_login_name.txt', 'w', encoding='UTF-8') as file:
                file.write(self.user_login()['username'])

            # # my_app.stop()
            App.get_running_app().stop()
            # MenuApp().run()
            # os.startfile('C:/Users/aelis/Documents/GitHub/GYM-app/controller/start_menu.py')
            # subprocess.run('C:/Users/aelis/Documents/GitHub/GYM-app/controller/start_menu.py')
            from menu_screen import MenuApp
            MenuApp().run()

        else:
            print('try again')
            self.ids.confirm.text = 'try again'

    def default_fill_username(self):
        """Возвращает имя юзера по умолчанию"""

        if self.ids.username.text == 'Bob Paris':
            self.ids.username.text = ''
        elif self.ids.username.text == '':
            self.ids.username.text = 'Bob Paris'

    def default_fill_password(self):
        """Возвращает пароль по умолчанию"""

        if self.ids.password.text == 'K@r1':
            self.ids.password.password = True
            self.ids.password.text = ''
        elif self.ids.password.text == '':
            self.ids.password.password = False
            self.ids.password.text = 'K@r1'

    def go_back(self):
        if self.ids.username.text == '':
            pass
        elif self.ids.password.text == '':
            pass
        else:
            self.default_view()
            self.manager.current = "Enter Screen"

    def default_view(self):
        """Возвращает вид по умолчанию"""

        self.ids.confirm.text = 'Confirm'
        self.ids.username.text = 'Bob Paris'
        self.ids.password.text = 'K@r1'
        self.ids.password.password = False


class AimScreen(Screen):

    def confirm_thin(self):
        """Сохраняет информацию в БД, переводит на следующий экран"""
        print('подсушиться')
        Registration.user_char['aim'] = 1
        self.manager.current = 'Level Screen'

    def confirm_mass(self):
        """Сохраняет информацию в БД, переводит на следующий экран"""
        print('набрать массу')
        Registration.user_char['aim'] = 2
        self.manager.current = 'Level Screen'

    def confirm_fit(self):
        """Сохраняет информацию в БД, переводит на следующий экран"""
        print('поддерживать тело в тонусе')
        Registration.user_char['aim'] = 3
        self.manager.current = 'Level Screen'

    def go_back(self):
        """Очищает выбор пользователя в БД"""
        Registration.user_char['aim'] = 1

    def default_view(self, groupname: list):
        """Возвращает вид по умолчанию"""
        widgets = ToggleButtonBehavior.get_widgets(groupname)
        for value in widgets:
            value.state = 'normal'


class LevelScreen(Screen):
    def confirm_beginner(self):
        """Сохраняет информацию в БД, переводит на следующий экран"""
        print('новичок')
        Registration.user_char['level'] = 1
        self.manager.current = 'Weekday Screen'

    def confirm_intermediate(self):
        """Сохраняет информацию в БД, переводит на следующий экран"""
        print('продолжающий')
        Registration.user_char['level'] = 2
        self.manager.current = 'Weekday Screen'

    def confirm_profi(self):
        """Сохраняет информацию в БД, переводит на следующий экран"""
        print('профи')
        Registration.user_char['level'] = 3
        self.manager.current = 'Weekday Screen'

    def go_back(self):
        """Очищает выбор пользователя в БД"""
        Registration.user_char['level'] = 1

    def default_view(self, groupname: list):
        """Возвращает вид по умолчанию"""
        widgets = ToggleButtonBehavior.get_widgets(groupname)
        for value in widgets:
            value.state = 'normal'


class WeekdayScreen(Screen):
    def __init__(self, name):
        super(Screen, self).__init__()
        self.list = [0, 0, 0, 0, 0, 0, 0]

        self.name = name

    def active_mon(self):
        i = 0
        if self.ids.mon.state == 'down':
            print('Пн')
            self.list.insert(i, i + 1)
            self.list.pop(i + 1)
        else:
            self.list.insert(i, 0)
            self.list.remove(i + 1)
        return self.list

    def active_tue(self):
        i = 1
        if self.ids.tue.state == 'down':
            print('Вт')
            self.list.insert(i, i + 1)
            self.list.pop(i + 1)
        else:
            self.list.insert(i, 0)
            self.list.remove(i + 1)
        return self.list

    def active_wen(self):
        i = 2
        if self.ids.wen.state == 'down':
            print('Ср')
            self.list.insert(i, i + 1)
            self.list.pop(i + 1)
        else:
            self.list.insert(i, 0)
            self.list.remove(i + 1)
        return self.list

    def active_thr(self):
        i = 3
        if self.ids.thr.state == 'down':
            print('Чт')
            self.list.insert(i, i + 1)
            self.list.pop(i + 1)
        else:
            self.list.insert(i, 0)
            self.list.remove(i + 1)
        return self.list

    def active_fr(self):
        i = 4
        if self.ids.fr.state == 'down':
            print('Пт')
            self.list.insert(i, i + 1)
            self.list.pop(i + 1)
        else:
            self.list.insert(i, 0)
            self.list.remove(i + 1)
        return self.list

    def active_sat(self):
        i = 5
        if self.ids.sat.state == 'down':
            print('Сб')
            self.list.insert(i, i + 1)
            self.list.pop(i + 1)
        else:
            self.list.insert(i, 0)
            self.list.remove(i + 1)
        return self.list

    def active_sun(self):
        i = 6
        if self.ids.sun.state == 'down':
            print('Вс')
            self.list.insert(i, i + 1)
            self.list.pop(i + 1)
        else:
            self.list.insert(i, 0)
            self.list.remove(i + 1)
        return self.list

    def check_flag(self, flag):
        if flag:
            self.manager.current = "Musculetype Screen"

    def __clear_list(self):
        for i in range(0, self.list.count(0)):
            self.list.remove(0)

    def __create_day_str(self, l: list) -> str:
        """
        Создаёт из списка номеров дней строку с краткими наименованиями
        :param l: список номеров дней
        :return: строка кратких названий
        """
        d = {1: 'Пн', 2: 'Вт', 3: 'Ср', 4: 'Чт', 5: 'Пт', 6: 'Сб', 7: 'Вс'}
        d_list = []
        for i in l:
            d_list.append(d[i])
        d_str = ','.join(d_list)
        return d_str

    def confirm(self):
        """Передаёт cтроку выбранных дней в контроллер.
        Переводит пользователя на следующую страницу, если что-то выбрано, если не выбрано, остаемся на этой странице"""
        self.__clear_list()
        if len(self.list) == 0:
            Registration.user_char['days'] = 'Вт,Чт,Сб'
        else:
            self.check_flag(1)
            # print(self.list)
            d_str = self.__create_day_str(self.list)
            Registration.user_char['days'] = d_str
            # print(Registration.user_char['days'])

    def go_back(self):
        """Очищает выбор пользователя в БД"""
        self.default_view()
        Registration.user_char['days'] = 'Вт,Чт,Сб'
        self.manager.current = "Level Screen"

    def default_view(self):
        """Возвращает вид по умолчанию"""
        """Возвращает вид по умолчанию"""
        self.ids.mon.state = 'normal'
        self.ids.tue.state = 'normal'
        self.ids.wen.state = 'normal'
        self.ids.thr.state = 'normal'
        self.ids.fr.state = 'normal'
        self.ids.sat.state = 'normal'
        self.ids.sun.state = 'normal'
        self.list = [0, 0, 0, 0, 0, 0, 0]


class MusculetypeScreen(Screen):
    def __init__(self, name):
        super(Screen, self).__init__()
        self.list = [0, 0, 0, 0, 0, 0]
        self.name = name

    # def cb_create(self):
    #     self.ids.chest.size=

    def active_chest(self):
        i = 0
        if self.ids.chest.state == 'down':
            print('chest')
            self.list.insert(i, 1)
            self.list.pop(i + 1)
        else:
            self.list.insert(i, 0)
            self.list.remove(i + 1)
        return self.list

    def active_back(self):
        i = 1
        if self.ids.back.state == 'down':
            print('back')
            self.list.insert(i, 2)
            self.list.pop(i + 1)
        else:
            self.list.insert(i, 0)
            self.list.remove(i + 1)
        return self.list

    def active_hand(self):
        i = 2
        if self.ids.hand.state == 'down':
            print('hand')
            self.list.insert(i, 3)
            self.list.pop(i + 1)
        else:
            self.list.insert(i, 0)
            self.list.remove(i + 1)
        return self.list

    def active_leg(self):
        i = 3
        if self.ids.leg.state == 'down':
            print('leg')
            self.list.insert(i, 4)
            self.list.pop(i + 1)
        else:
            self.list.insert(i, 0)
            self.list.remove(i + 1)
        return self.list

    def active_shoulder(self):
        i = 4
        if self.ids.shoulder.state == 'down':
            print('schoulder')
            self.list.insert(i, 5)
            self.list.pop(i + 1)
        else:
            self.list.insert(i, 0)
            self.list.remove(i + 1)
        return self.list

    def active_body(self):
        i = 5
        if self.ids.body.state == 'down':
            print('body')
            self.list.insert(i, 6)
            self.list.pop(i + 1)
        else:
            self.list.insert(i, 0)
            self.list.remove(i + 1)
        return self.list

    def __muscule_str(self, l):
        """Преобразует список номеров выбранных групп мышц в строковый тип"""

        d = {1: 'грудь', 2: 'спина', 3: 'руки', 4: 'ноги', 5: 'плечи', 6: 'всё тело'}
        d_list = []
        for i in l:
            d_list.append(d[i])
        d_str = ','.join(d_list)
        return d_str

    def confirm(self):
        """Сохраняет cписок из выбранных положений в БД"""
        for i in range(0, self.list.count(0)):
            self.list.remove(0)
        if len(self.list) == 0:
            Registration.user_char['muscule'] = 'всё тело'
        else:
            self.check_flag(1)
            m_str = self.__muscule_str(self.list)
            Registration.user_char['muscule'] = m_str

    def check_flag(self, flag):
        if flag:
            self.manager.current = "Fat Screen"

    def go_back(self):
        """Очищает выбор пользователя в БД"""
        self.default_view()
        Registration.user_char['muscule'] = 'всё тело'
        self.manager.current = 'Weekday Screen'

    def default_view(self):
        """Возвращает вид по умолчанию"""
        self.ids.chest.state = 'normal'
        self.ids.back.state = 'normal'
        self.ids.hand.state = 'normal'
        self.ids.leg.state = 'normal'
        self.ids.shoulder.state = 'normal'
        self.ids.body.state = 'normal'
        self.list = [0, 0, 0, 0, 0, 0]


class FatScreen(Screen):

    def label_value(self):
        self.ids.fat_label.text = str(round(self.ids.fat_slider.value, 1)) + '%'

    def confirm(self):
        Registration.user_char['fat'] = self.ids.fat_label.text[:-1]
        print(Registration.user_char['fat'])
        self.manager.current = 'UserInfo Screen'
        self.default_view()

    def go_back(self):
        """Очищает выбор пользователя в БД"""

        self.manager.current = 'Musculetype Screen'
        Registration.user_char['fat'] = 15.5
        self.default_view()

    def default_view(self):
        """Возвращает вид по умолчанию"""
        self.ids.fat_slider.value = 30
        self.ids.fat_label.text = '30%'


class UserInfoScreen(Screen):

    def default_fill_login(self):
        """Возвращает имя юзера по умолчанию"""

        if self.ids.login.text == 'Логин':
            self.ids.login.text = ''
        elif self.ids.login.text == '':
            self.ids.login.text = 'Логин'

    def default_fill_password(self):
        """Возвращает пароль по умолчанию"""

        if self.ids.new_password.text == 'Пароль':
            self.ids.new_password.password = True
            self.ids.new_password.text = ''
        elif self.ids.new_password.text == '':
            self.ids.new_password.password = False
            self.ids.new_password.text = 'Пароль'

    def default_fill_check_password(self):
        """Возвращает в поле  по умолчанию"""

        if self.ids.check_password.text == 'Подтверждение пароля':
            self.ids.check_password.password = True
            self.ids.check_password.text = ''
        elif self.ids.check_password.text == '':
            self.ids.check_password.password = False
            self.ids.check_password.text = 'Подтверждение пароля'

    def default_fill_email(self):
        """Возвращает имя юзера по умолчанию"""

        if self.ids.email.text == 'email':
            self.ids.email.text = ''
        elif self.ids.email.text == '':
            self.ids.email.text = 'email'

    def default_fill_height(self):
        """Возвращает имя юзера по умолчанию"""

        if self.ids.height.text == 'Рост':
            self.ids.height.text = ''
        elif self.ids.height.text == '':
            self.ids.height.text = 'Рост'

    def default_fill_weight(self):
        """Возвращает имя юзера по умолчанию"""

        if self.ids.weight.text == 'Вес':
            self.ids.weight.text = ''
        elif self.ids.weight.text == '':
            self.ids.weight.text = 'Вес'

    def __password_control(self) -> bool:
        """
        Проверяет, совпали ли пароли
        :return: True, если пароли совпали
        """
        if self.ids.new_password.text == self.ids.check_password.text:
            return True
        return False

    def __check_filling(self) -> bool:
        """
        Проверяет, не остался ли курсор в пустом TextBox
        :return: True - если  все заполнено корректно
        """
        if self.ids.login.text == '':
            return False
        elif self.ids.new_password.text == '':
            return False
        elif self.ids.check_password.text == '':
            return False
        elif self.ids.new_password.text == '':
            return False
        elif self.ids.email.text == '':
            return False
        elif self.ids.weight.text == '':
            return False
        elif self.ids.height.text == '':
            return False
        else:
            return True

    def confirm(self):
        Registration.user['login'] = self.ids.login.text
        Registration.user['email'] = self.ids.email.text
        Registration.user_char['male'] = self.ids.male.text
        # Возможна ошибка, что пользователь передал в словарь "Пол" - значение по умолчанию
        print(Registration.user_char['male'])
        Registration.user_char['height'] = self.ids.height.text
        Registration.user_char['weight'] = self.ids.weight.text
        if self.__check_filling():
            if self.__password_control():
                Registration.user['password'] = self.ids.new_password.text
                self.default_view()
                self.manager.current = "Start Screen"
            else:
                print('Пароли должны сопадать')

    def go_back(self):
        """Очищает выбор пользователя в БД"""
        if self.__check_filling():
            self.default_view()
            self.manager.current = 'Fat Screen'

    def default_view(self):
        """Возвращает вид по умолчанию"""
        self.ids.login.text = 'Логин'
        self.ids.email.text = 'email'
        self.ids.new_password.text = 'Пароль'
        self.ids.new_password.password = False
        self.ids.check_password.text = 'Подтверждение пароля'
        self.ids.check_password.password = False
        self.ids.male.text = 'Пол'
        self.ids.height.text = 'Рост'
        self.ids.weight.text = 'Вес'


class StartScreen(Screen):
    def confirm(self):
        Registration.fill_user_bd()
        self.manager.current = "Log in"
        print('У-ра!')

    def go_back(self):
        """Очищает выбор пользователя в БД"""
        self.manager.current = 'UserInfo Screen'


class TestApp(App):

    def build(self):
        Builder.load_file('interface.kv', encoding='CP1251')
        sm = ScreenManager()
        sm.add_widget(EnterScreen(name='Enter Screen'))
        sm.add_widget(LoginScreen(name='Log in'))
        sm.add_widget(AimScreen(name='Aim Screen'))
        sm.add_widget(LevelScreen(name='Level Screen'))
        sm.add_widget(WeekdayScreen(name='Weekday Screen'))
        sm.add_widget(MusculetypeScreen(name='Musculetype Screen'))
        sm.add_widget(FatScreen(name='Fat Screen'))
        sm.add_widget(UserInfoScreen(name='UserInfo Screen'))
        sm.add_widget(StartScreen(name='Start Screen'))

        return sm


TestApp().run()
# my_app=TestApp()
# my_app.run()
