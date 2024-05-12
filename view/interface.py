from kivy.app import App
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from controller.login import Login
from controller.login import Registration

Builder.load_string("""
<EnterScreen>:
    AnchorLayout:
        BoxLayout:
            spacing: 15
            orientation: 'vertical'
            size_hint: [.5, .25]
            Button:
                text: 'Log in'
                on_press: root.manager.current ="Log in"
            Button:
                text: 'Sign up'
                on_press: root.manager.current ="Aim Screen"
<LoginScreen>:
    AnchorLayout:
        id: LoginWidgets
        BoxLayout:
            orientation: 'vertical'
            size_hint: [.5, .25]
            GridLayout:
                cols:2
                padding: 0, 0, 0, 15
                Label:
                    text: 'username'
                TextInput:
                    id:username
                    text: 'Bob Paris'                                                
                    on_focus: root.default_fill_username()
                    multiline: False
                Label:
                    text: 'password'
                TextInput:
                    id:password
                    text: 'K@r1'
                    on_focus: root.default_fill_password()
                    password: False
                    multiline: False
            Button:
                size_hint: [1, .25]
                id: confirm
                text: 'Confirm'
                on_press: root.confirm()
            Button:
                size_hint: [1, .25]
                text: 'Go back'
                on_press: root.go_back()
             
<AimScreen>:
    AnchorLayout:
        BoxLayout:
            orientation: 'vertical'
            size_hint: [.5, .5]
            Button:
                text: 'Подсушиться'
                on_press: root.confirm_thin() 
            Button:
                text: 'Набрать массу'
                on_press: root.confirm_mass()
            Button:
                text: 'Поддерживать тело в тонусе'
                on_press: root.confirm_fit()
            BoxLayout:
                orientation: 'vertical'
                spacing: 2
                AnchorLayout:
                    Button:
                        size_hint: [.5, .7]
                        text: 'Go back'
                        on_press: root.default_view(groupname='smth'); root.manager.current ="Enter Screen"; root.go_back()                      
<LevelScreen>:
    AnchorLayout:   
        BoxLayout:
            orientation: 'vertical'
            size_hint: [.5, .5]
            spacing: 20
            BoxLayout:
                orientation: 'vertical'
                Button:
                    id: beginner
                    text: 'Новичок'
                    on_press: root.confirm_beginner() 
                Label:
                    size_hint: [1, .5]
                    text: 'Первый раз в зале'
                    canvas.before:
                        Color:
                            rgba: 0, 0.5, 0.5, 1
                        Rectangle:
                            size: self.size
                            pos: self.pos
            BoxLayout:
                orientation: 'vertical'
                Button:
                    id: intermediate
                    text: 'Продолжающий'
                    on_press:  root.confirm_intermediate()
                Label:
                    size_hint: [1, .5]
                    text: 'Занимаюсь для себя несколько месяцев'
                    canvas.before:
                        Color:
                            rgba: 0, 0.5, 0.5, 1
                        Rectangle:
                            size: self.size
                            pos: self.pos
            BoxLayout:
                orientation: 'vertical'
                Button:
                    id: profi
                    text: 'Профи'
                    on_press: root.confirm_profi()
                Label:
                    size_hint: [1, .5]
                    text: 'Регулярно тренируюсь на протяжении нескольких лет'
                    canvas.before:
                        Color:
                            rgba: 0, 0.5, 0.5, 1
                        Rectangle:
                            size: self.size
                            pos: self.pos
            BoxLayout:
                orientation: 'vertical'
                AnchorLayout:
                    Button:
                        size_hint: [.5, .7]
                        text: 'Go back'
                        on_press: root.default_view(groupname='smth'); root.manager.current ="Aim Screen"; root.go_back()
<WeekdayScreen>:    
    AnchorLayout:
        BoxLayout:
            spacing: 15        
            GridLayout:
                cols:2
                padding: 0, 0, 0, 15
                ToggleButton:
                    id: mon  
                    text: 'Пн'
                    on_press: root.active_mon()
                ToggleButton:
                    id: tue
                    text: 'Вт'
                    on_press: root.active_tue()
                ToggleButton:
                    id: wen
                    text: 'Ср'
                    on_press: root.active_wen()
                ToggleButton:
                    id: thr
                    text: 'Чт'
                    on_press: root.active_thr()
                ToggleButton:
                    id: fr
                    text: 'Пт'
                    on_press: root.active_fr()
                ToggleButton:
                    id: sat
                    text: 'Сб'
                    on_press: root.active_sat()
                ToggleButton:
                    id: sun
                    text: 'Вс'
                    on_press: root.active_sun()
                BoxLayout    
                    orientation: 'vertical'
                    AnchorLayout:
                        Button:
                            size_hint: [.5, .7]
                            id: confirm
                            text: 'Confirm'
                            on_press: root.confirm(); root.default_view()
                    AnchorLayout:
                        Button:
                            size_hint: [.5, .7]
                            text: 'Go back'
                            on_press: root.go_back()
<MusculetypeScreen>:
    AnchorLayout:
        BoxLayout:
            height: '200dp'
            width: '200dp' 
            spacing: 15
            GridLayout:
                cols:2
                CheckBox:
                    id: chest
                    background_checkbox_normal: 'i_chest.png'
                    background_checkbox_down:'i_chest_frame.png'
                    on_press: root.active_chest()   
                CheckBox
                    id: back
                    size:          
                    background_checkbox_normal: 'i_back.png'
                    background_checkbox_down:'i_back_frame.png'
                    on_press: root.active_back() 
                CheckBox
                    id: hand
                    size:          
                    background_checkbox_normal: 'i_hand.png'
                    background_checkbox_down:'i_hand_frame.png'
                    on_press: root.active_hand()
                CheckBox
                    id: leg
                    size:          
                    background_checkbox_normal: 'i_leg2.png'
                    background_checkbox_down:'i_leg2_frame.png'
                    on_press: root.active_leg()
                CheckBox
                    id: shoulder
                    size:          
                    background_checkbox_normal: 'i_shoulder.png'
                    background_checkbox_down:'i_shoulder_frame.png'
                    on_press: root.active_shoulder()
                CheckBox
                    id: body
                    size:          
                    background_checkbox_normal: 'i_body.png'
                    background_checkbox_down:'i_body_frame.png'

                    on_press: root.active_body()
                AnchorLayout:
                    Button:
                        size_hint: [.5, .7]
                        text: 'Go back'
                        on_press: root.go_back()
                AnchorLayout:
                    Button:
                        size_hint: [.5, .7]
                        id: confirm
                        text: 'Confirm'
                        on_press: root.confirm(); root.default_view()
<FatScreen>
    AnchorLayout:
        BoxLayout:
            orientation: 'vertical' 
            GridLayout:
                cols: 3
                AnchorLayout:
                    id: fat_thin
                    size_hint: [.3, .3]
                    Image:
                        source: 'fat_thin.png'
                AnchorLayout:
                    id: fat_thin
                    size_hint: [1, 1]
                    Image:
                        source: 'fat_fit.png'
                AnchorLayout:
                    id: fat_thin
                    size_hint: [.3, .3]
                    Image:
                        source: 'fat_fat.png'
            AnchorLayout:
                anchor_x: 'center'           
                anchor_y: 'bottom'          
            Label:
                id: fat_label 
                text: '30.0%'
                bold: True
                font_size: '30sp'
            Slider:
                id: fat_slider 
                max: 85
                min: 5
                value: 30
                on_touch_up: root.label_value()
            Label:
                text: 'Оцените уровень подкожного жира'
                sixe_hint: [1, 1]
                font_size: '20sp'
            
            GridLayout:
                cols: 2
                AnchorLayout:
                    Button:
                        size_hint: [.5, .7]
                        text: 'Go back'
                        on_press: root.go_back()
                AnchorLayout:    
                    Button:
                        size_hint: [.5, .7]
                        id: confirm
                        text: 'Confirm'
                        on_press: root.confirm()
<UserInfoScreen>
    AnchorLayout:
        BoxLayout:
            orientation: 'vertical'
            size_hint: [.5, .5]
            TextInput: 
                id: login
                text: 'Логин'                                                
                on_focus: root.default_fill_login()
                multiline: False
            TextInput:
                id: new_password
                text: 'Пароль'
                on_focus: root.default_fill_password()
                password: False
                multiline: False
            TextInput:
                id: check_password
                text: 'Подтверждение пароля'
                on_focus: root.default_fill_check_password()
                password: False
                multiline: False
            TextInput:
                id: email
                text: 'email'                                                
                on_focus: root.default_fill_email()
                multiline: False
            Spinner:
                id: male
                text: 'Пол'
                values: ('М', 'Ж')
            TextInput:
                id: height
                text: 'Рост'                                                
                on_focus: root.default_fill_height()
                multiline: False
            TextInput:
                id: weight
                text: 'Вес'                                                
                on_focus: root.default_fill_weight()
                multiline: False
            GridLayout:
                cols: 2
                AnchorLayout:    
                    Button:
                        size_hint: [.5, .7]
                        text: 'Go back'
                        on_press: root.go_back()
                AnchorLayout:
                    Button:
                        size_hint: [.5, .7]
                        id: confirm
                        text: 'Confirm'
                        on_press: root.confirm()
<StartScreen>
    AnchorLayout:
        BoxLayout:
            orientation: 'vertical'
            size_hint: [.5, .5]
            AnchorLayout:
                Button:
                    text: 'На старт!'
                    on_press: root.confirm()
            AnchorLayout:
                Button:
                    size_hint: [.3, .5]
                    text: 'Зачем Go back?!'
                    on_press: root.go_back()
""")


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
        # print(self.user_login())
        if Login.check_user(self.user_login()):
            print('sucsess!')
            self.ids.confirm.text = 'sucsess!'
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
            self.list.remove(i+1)
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
        Registration.user_char['fat']=self.ids.fat_label.text[:-1]
        print(Registration.user_char['fat'])
        self.manager.current = 'UserInfo Screen'
        self.default_view()

    def go_back(self):
        """Очищает выбор пользователя в БД"""

        self.manager.current = 'Musculetype Screen'
        Registration.user_char['fat'] =15.5
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

    def __password_control(self)->bool:
        """
        Проверяет, совпали ли пароли
        :return: True, если пароли совпали
        """
        if self.ids.new_password.text==self.ids.check_password.text:
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
        print('У-ра!')

    def go_back(self):
        """Очищает выбор пользователя в БД"""
        self.manager.current = 'UserInfo Screen'


class TestApp(App):

    def build(self):
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
