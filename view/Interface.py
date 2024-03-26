import kivy
from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.anchorlayout import AnchorLayout
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

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
                on_press: root.default_view(); root.manager.current ="EnterScreen"
             
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
                        on_press: root.default_view(groupname='smth'); root.manager.current ="EnterScreen"; root.go_back()
                         
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
                    text: 'Пн'

                ToggleButton:
                    text: 'Вт'
                ToggleButton:
                    text: 'Ср'
                ToggleButton:
                    text: 'Чт'
                ToggleButton:
                    text: 'Пт'
                ToggleButton:
                    text: 'Сб'
                ToggleButton:
                    text: 'Вс'
                BoxLayout    
                    orientation: 'vertical'
                    AnchorLayout:
                        Button:
                            size_hint: [.5, .7]
                            id: confirm
                            text: 'Confirm'
                            on_press: root.confirm(groupname='smth'); root.manager.current ="Musculetype Screen"; root.default_view(groupname='smth')
                    AnchorLayout:
                        Button:
                            size_hint: [.5, .7]
                            text: 'Go back'
                            on_press: root.default_view(groupname='smth'); root.manager.current ="Level Screen"; root.go_back()
<MusculetypeScreen>:
    AnchorLayout:
        BoxLayout:
            spacing: 15
            GridLayout:
                cols:2
                CheckBox:
                    id: chest
                    size: (150, 150)
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
                        on_press: root.confirm(); root.manager.current ="Fat Screen"
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
                        on_press: root.confirm(); root.manager.current ="Start Screen"
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
#
# Button
# text: 'Print'
# on_press: root.go()

class EnterScreen(Screen):
    pass

class LoginScreen(Screen):
    def confirm(self):
        """Проверяет введённые данные, в случае успешной проверки входит в аккаунт"""
        print('sucsess!')
        # label=Label(text='sucsess')
        # self.ids.LoginWidgets.add_widget(label)
        self.ids.confirm.text='sucsess!'

    def default_fill_username(self):
        """Возвращает имя юзера по умолчанию"""

        if self.ids.username.text=='Bob Paris':
            self.ids.username.text =''
        elif self.ids.username.text=='':
            self.ids.username.text = 'Bob Paris'

    def default_fill_password(self):
        """Возвращает пароль по умолчанию"""

        if self.ids.password.text=='K@r1':
            self.ids.password.password = True
            self.ids.password.text =''
        elif self.ids.password.text=='':
            self.ids.password.password = False
            self.ids.password.text = 'K@r1'


    def default_view(self):
        """Возвращает вид по умолчанию"""

        self.ids.confirm.text = 'Confirm'
        self.ids.username.text = 'Bob Paris'
        self.ids.password.text = 'K@r1'
        self.ids.password.password = False

# class AimToggleButton(ToggleButtonBehavior):
#     def __init__(self, **kwargs):
#         super(AimToggleButton, self).__init__(**kwargs)
#     def on_state(self, widget, value):
#         if value == 'Подсушиться':
#             print('подсушиться')
#         elif value == 'Набрать массу':
#             print('Набрать массу')
#         elif value == 'Поддерживать тело в тонусе':
#             print('Поддерживать тело в тонусе')
class AimScreen(Screen):

    def confirm_thin(self):
        """Сохраняет информацию в БД, переводит на следующий экран"""
        print('Сбросить массу')
        self.manager.current='Level Screen'
    def confirm_mass(self):
        """Сохраняет информацию в БД, переводит на следующий экран"""
        print('Набрать массу')
        self.manager.current='Level Screen'
    def confirm_fit(self):
        """Сохраняет информацию в БД, переводит на следующий экран"""
        print('Поддерживать тело в тонусе')
        self.manager.current='Level Screen'

    def confirm(self, groupname: list):
        """В зависимости от того, что выбрал пользователь, сохраняет для БД один из вариантов,
            переводит пользователя на следующую страницу, если что-то выбрано, если не выбрано, ничего не происходит"""
        # toggle_button = AimToggleButton()
        # return toggle_button
        widgets=ToggleButtonBehavior.get_widgets(groupname)
        for value in widgets:
            if value.state=='down' and value.text=='Подсушиться':
                print('подсушиться')
                # sm.currrent='Level Screen'
            #     тут он должен перейти на следующую страницу
            elif value.state=='down' and value.text=='Набрать массу':
                print('Набрать массу')
            elif value.state=='down' and value.text == 'Поддерживать тело в тонусе':
                print('Поддерживать тело в тонусе')
    def go_back(self):
        """Очищает выбор пользователя в БД"""
        pass
    def default_view(self, groupname: list):
        """Возвращает вид по умолчанию"""
        widgets = ToggleButtonBehavior.get_widgets(groupname)
        for value in widgets:
            value.state = 'normal'

class LevelScreen(Screen):
    def confirm_beginner(self):
        """Сохраняет информацию в БД, переводит на следующий экран"""
        print('Новичок')
        self.manager.current='Weekday Screen'
    def confirm_intermediate(self):
        """Сохраняет информацию в БД, переводит на следующий экран"""
        print('Продолжающий')
        self.manager.current='Weekday Screen'

    def confirm_profi(self):
        """Сохраняет информацию в БД, переводит на следующий экран"""
        print('Профи')
        self.manager.current='Weekday Screen'

    def go_back(self):
        """Очищает выбор пользователя в БД"""
        pass

    def default_view(self, groupname: list):
        """Возвращает вид по умолчанию"""
        widgets = ToggleButtonBehavior.get_widgets(groupname)
        for value in widgets:
            value.state = 'normal'

class WeekdayScreen(Screen):
    def confirm(self, groupname: list):
        """В зависимости от того, что выбрал пользователь, сохраняет для БД один из вариантов,
            переводит пользователя на следующую страницу, если что-то выбрано, если не выбрано, ничего не происходит"""
        widgets = ToggleButtonBehavior.get_widgets(groupname)

        for value in widgets:
            if value.state == 'down' and value.text == 'Пн':
                print('Пн')
            #     тут он должен перейти на следующую страницу
            elif value.state == 'down' and value.text == 'Вт':
                print('Вт')
            elif value.state == 'down' and value.text == 'Ср':
                print('Ср')
            elif value.state == 'down' and value.text == 'Чт':
                print('Чт')
            elif value.state == 'down' and value.text == 'Пт':
                print('Пт')
            elif value.state == 'down' and value.text == 'Сб':
                print('Сб')
            elif value.state == 'down' and value.text == 'Вс':
                print('Вс')
    def go_back(self):
        """Очищает выбор пользователя в БД"""
        pass

    def default_view(self, groupname: list):
        """Возвращает вид по умолчанию"""
        widgets = ToggleButtonBehavior.get_widgets(groupname)
        for value in widgets:
            value.state = 'normal'

class MusculetypeScreen(Screen):
    def __init__(self, name):
        super(Screen, self).__init__()
        self.list=[0,0,0,0,0,0]
        self.name=name
    def active_chest(self):
        if self.ids.chest.state == 'down':
            print('chest')
            i=0
            self.list.insert(i,1)
            self.list.pop(i+1)
            return self.list
    def active_back(self):
        if self.ids.back.state == 'down':
            print('back')
            i = 1
            self.list.insert(i, 2)
            self.list.pop(i + 1)
            return self.list
    def active_hand(self):
        if self.ids.hand.state == 'down':
            print('hand')
            i = 2
            self.list.insert(i, 3)
            self.list.pop(i + 1)
            return self.list
    def active_leg(self):
        if self.ids.leg.state == 'down':
            print('leg')
            i = 3
            self.list.insert(i, 4)
            self.list.pop(i + 1)
            return self.list
    def active_shoulder(self):
        if self.ids.shoulder.state == 'down':
            print('schoulder')
            i = 4
            self.list.insert(i, 5)
            self.list.pop(i + 1)
            return self.list
    def active_body(self):
        if self.ids.body.state == 'down':
            print('body')
            i = 5
            self.list.insert(i, 6)
            self.list.pop(i + 1)
            return self.list
    def confirm(self):
        """Сохраняет словарь из выбранных положений в БД"""
        c=self.list.count(0)
        for i in range(0, c):
            self.list.remove(0)

        print(self.list)
        self.default_view()

        return self.list

    def go_back(self):
        """Очищает выбор пользователя в БД"""
        self.default_view()
        self.manager.current = 'Weekday Screen'

    def default_view(self):
        """Возвращает вид по умолчанию"""
        self.ids.chest.state = 'normal'
        self.ids.back.state = 'normal'
        self.ids.hand.state = 'normal'
        self.ids.leg.state = 'normal'
        self.ids.shoulder.state = 'normal'
        self.ids.body.state = 'normal'
        self.list=[0,0,0,0,0,0]

class FatScreen(Screen):


    def label_value(self):
        self.ids.fat_label.text=str(round(self.ids.fat_slider.value, 1))+'%'
    def confirm(self):
        self.manager.current = 'UserInfo Screen'
        self.default_view()

    def go_back(self):
        """Очищает выбор пользователя в БД"""

        self.manager.current = 'Musculetype Screen'
        self.default_view()

    def default_view(self):
        """Возвращает вид по умолчанию"""
        self.ids.fat_slider.value=30
        self.ids.fat_label.text='30%'

class UserInfoScreen(Screen):

    def default_fill_login(self):
        """Возвращает имя юзера по умолчанию"""

        if self.ids.login.text=='Логин':
            self.ids.login.text =''
        elif self.ids.login.text=='':
            self.ids.login.text = 'Логин'

    def default_fill_email(self):
        """Возвращает имя юзера по умолчанию"""

        if self.ids.email.text == 'email':
            self.ids.email.text = ''
        elif self.ids.email.text == '':
            self.ids.email.text = 'email'
    def default_fill_height(self):
        """Возвращает имя юзера по умолчанию"""

        if self.ids.height.text=='Рост':
            self.ids.height.text =''
        elif self.ids.height.text=='':
            self.ids.height.text = 'Рост'
    def default_fill_weight(self):
        """Возвращает имя юзера по умолчанию"""

        if self.ids.weight.text=='Вес':
            self.ids.weight.text =''
        elif self.ids.weight.text=='':
            self.ids.weight.text = 'Вес'

    def confirm(self):
        pass
    def go_back(self):
        """Очищает выбор пользователя в БД"""

        self.default_view()
        self.manager.current = 'Fat Screen'
    def default_view(self):
        """Возвращает вид по умолчанию"""
        self.ids.login.text = 'Логин'
        self.ids.email.text = 'email'
        self.ids.male.text = 'Пол'
        self.ids.height.text = 'Рост'
        self.ids.weight.text = 'Вес'
class StartScreen(Screen):
    def confirm(self):
        print('У-ра!')

    def go_back(self):
        """Очищает выбор пользователя в БД"""
        self.manager.current = 'UserInfo Screen'
class TestApp(App):

    def build(self):
        sm=ScreenManager()
        sm.add_widget(EnterScreen(name='EnterScreen'))
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

