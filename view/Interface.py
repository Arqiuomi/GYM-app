import kivy
from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.anchorlayout import AnchorLayout
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
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
                on_press: root.manager.current ="EnterScreen"; root.default_view()

""")
#
# Button
# text: 'Print'
# on_press: root.go()

class EnterScreen(Screen):
    pass

class LoginScreen(Screen):
    def confirm(self):
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


class TestApp(App):

    def build(self):
        sm=ScreenManager()
        sm.add_widget(EnterScreen(name='EnterScreen'))
        sm.add_widget(LoginScreen(name='Log in'))
        return sm
TestApp().run()
