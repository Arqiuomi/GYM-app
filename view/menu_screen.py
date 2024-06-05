# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from controller.exercise_window import Exercise_Screen

Builder.load_string("""
<Ex_Screen>:
    AnchorLayout:
        anchor_x: 'center'           
        anchor_y: 'bottom'
        BoxLayout:
            spacing: 15
            orientation: 'horizontal'
            size_hint: [1, .25]
            Button:
                id: calendar
                background_normal: 'i_calendar.png'
                background_down:'i_calendar2.jpg'
            Button:
                id: exercise
                background_normal: 'i_ex.png'
                background_down:'i_ex2.jpg'                
            Button:
                id: train
                background_normal: 'i_train.png'
                background_down:'i_train2.jpg'
                on_press: root.go_to_train()
            Button:
                id: statistic
                background_normal: 'i_stat.png'
    AnchorLayout:
        anchor_x: 'center'           
        anchor_y: 'top'
        GridLayout:
            cols:2
            size_hint: [.5, .1]
            padding: 0, 0, 0, 0
            TextInput:
                id: search
                text: 'Введите название упражнения'
                on_focus: root.default_fill_search()
            AnchorLayout:
                anchor_x: 'left'           
                anchor_y: 'top'
                size_hint: [.2, 1]
                Button:
                    id: find
                    text: 'Найти'
                    on_press: root.find(), root.remove_label_text(), root.add_label_text()
        GridLayout:
            id: central_grid
            rows: 2  
            size_hint: [.2, .8]
            Label:
                id: l1
                text: ''
            Label:
                id: l2
                text: ''
            
<Train_Screen>:
    AnchorLayout:
        anchor_x: 'center'           
        anchor_y: 'bottom'
        BoxLayout:
            spacing: 15
            orientation: 'horizontal'
            size_hint: [1, .15]
            Button:
                id: calendar
                text: 'Cal'
            Button:
                id: exercise
                text: 'Ex'
                on_press: root.go_to_ex()
            Button:
                id: train
                text: 'Tr'
            Button:
                id: statistic
                text: 'Stat'
    AnchorLayout:
        anchor_x: 'center'           
        anchor_y: 'center'
        BoxLayout:
            spacing: 20
            orientation: 'vertical'
            size_hint: [.4, .5]
            Button:
                id: start
                text: 'Начать тренировку'
            Button:
                id: skip
                text: 'Пропустить тренировку'

""")


class Ex_Screen(Screen):

    def default_fill_search(self):
        """Работает с курсором и надписью в поисковике"""

        if self.ids.search.text == 'Введите название упражнения':
            self.ids.search.text = ''
        elif self.ids.search.text == '':
            self.ids.search.text = 'Введите название упражнения'

    def find(self) -> bool:
        print(self.ids.search.text)
        return Exercise_Screen().find_ex(self.ids.search.text)

    def create_label(self, id) -> Label:
        label = Label()
        label.id = id
        label.text = 'print'
        return label

    def remove_label_text(self):
        self.ids.l1.text = ''
        self.ids.l2.text = ''

    def add_label_text(self):
        # заменить на описание упражнений из БД
        self.ids.l1.text = 'print'
        self.ids.l2.text = 'print'

    def go_to_train(self):
        self.default_view()
        self.manager.current = 'Train_Screen'

    def default_view(self):
        self.ids.search.text == 'Введите название упражнения'


class Train_Screen(Screen):
    def go_to_ex(self):
        self.default_view()
        self.manager.current = 'Ex_Screen'

    def default_view(self):
        pass


if __name__ == "__main__":
    class TestApp(App):
        def build(self):
            sm = ScreenManager()
            sm.add_widget(Ex_Screen(name='Ex_Screen'))
            sm.add_widget(Train_Screen(name='Train_Screen'))

            return sm


    TestApp().run()
