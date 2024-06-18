# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from controller.exercise_window import Exercise_Screen, Tr_St_Screen
from kivy.clock import Clock

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
                on_press: root.default_view(), root.go_to_train(), 
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
                    on_press: root.find(), root.remove_label_text(), root.add_descr()
    AnchorLayout:
        anchor_x: 'center'           
        anchor_y: 'center'
        GridLayout:
            id: central_grid
            rows: 2  
            size_hint: [.9, .6]
            ScrollView:
                do_scroll_x: False
                Label:
                    id: l1
                    text_size: self.size
                    size_hint_y: None
                    height: self.texture_size[1] + dp(10)
                    text_size: self.width, None
                    text: ''
            ScrollView:
                do_scroll_x: False
                Label:
                    id: l2
                    text_size: self.size
                    size_hint_y: None
                    height: self.texture_size[1] + dp(10)

                    text_size: self.width, None
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
                name: start
                id: start
                text: 'Начать тренировку'
                on_press: root.go_to_train_start()
            Button:
                id: skip
                text: 'Пропустить тренировку'

            
<Train_Start_Screen>:
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
            Label:
                id: time_label
                text: '00:00'
            Label:
                id: train_label
            GridLayout:
                id: grid_ex_number
                cols: root.number_of_ex()
            Button:
                text: 'start'
                on_press: root.start_stop(), root.current_train(), root.create_ex_number_label()
            Button:
                text: 'Resert'
                on_press: root.resert()  

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

    def add_label_text(self, text_1: str, text_2: str):
        self.ids.l1.text = text_1
        self.ids.l2.text = text_2

    def add_descr(self):
        """
        Выводит короткое и полное описание упражнения в label_1 и label_2
        :return:
        """
        if Exercise_Screen.find_ex(self.ids.search.text):
            try:
                self.add_label_text(Exercise_Screen.take_short_descr(self.ids.search.text),
                                    Exercise_Screen.take_full_descr(self.ids.search.text))
            except Exception as exc:
                self.ids.l1.text = 'Упс... '
                # Заменить на лог
                print(f'{exc} в методе take_descr. Проверь методы take_short_decscr() и take_full_decscr()')

        else:
            self.ids.l1.text = 'К счастью для Вас, мы пока не добавили это упражнение. Оно точно оно?'

    def go_to_train(self):
        self.default_view()
        screen_train = self.manager.get_screen('Train_Screen')
        if screen_train.flag:
            self.manager.current = 'Train_Start_Screen'
        else:
            self.manager.current = 'Train_Screen'

    def default_view(self):
        self.ids.search.text = 'Введите название упражнения'
        self.remove_label_text()


class TrainApp(App):
    def build(self):
        return Train_Start_Screen()


class Train_Screen(Screen):
    def __init__(self, **kwargs):
        super(Train_Screen, self).__init__(**kwargs)
        self.flag = False

    def go_to_ex(self):
        self.default_view()
        self.manager.current = 'Ex_Screen'

    def go_to_train_start(self):
        self.default_view()
        self.flag = True
        self.manager.current = 'Train_Start_Screen'

    def default_view(self):
        pass


class Train_Start_Screen(Screen):
    def __init__(self, **kwargs):
        super(Train_Start_Screen, self).__init__(**kwargs)
        self.seconds = 0
        self.is_counting = False
        self.new_train = True
        # self.number_of_ex = self.number_of_current_ex()

    # @property
    # def number_of_current_ex(self):
    #     return self.number_of_ex
    #
    #
    # @number_of_current_ex.getter
    # def number_of_current_ex(self):
    #     return Tr_St_Screen.take_number_of_ex()

    def start_stop(self):
        if self.is_counting:
            Clock.unschedule(self.update_time)
            self.is_counting = False
        else:
            self.is_counting = True
            Clock.schedule_interval(self.update_time, 1)

    def resert(self):
        self.seconds = 0
        self.ids.time_label.text = "00:00"
        if self.is_counting:
            Clock.unschedule(self.update_time)
            self.is_counting = False
        self.new_train = True
        self.clear_ex_number_label()

    def clear_ex_number_label(self):
        number = self.number_of_ex()
        layout = self.ids.grid_ex_number
        layout.clear_widgets()
    def update_time(self, *args):
        self.seconds += 1
        minutes = str(self.seconds // 60).zfill(2)
        seconds = str(self.seconds % 60).zfill(2)
        self.ids.time_label.text = f"{minutes}:{seconds}"

    def current_train(self):
        self.ids.train_label.text = Tr_St_Screen.take_ex_name()

    def number_of_ex(self):
        """Принимает и возвращает количество упражнений в текущей тренировке из контроллера"""
        return Tr_St_Screen.take_number_of_ex()

    def create_ex_number_label(self):
        if self.new_train:
            number = self.number_of_ex()
            layout = self.ids.grid_ex_number
            for i in range(1, number + 1):
                layout.add_widget(Label(text=f'{i}'))
            self.new_train = False

    def go_to_ex(self):
        self.manager.current = 'Ex_Screen'

    # Опустить флажок, когда тренировка закончится
    # screen_train = self.manager.get_screen('Train_Screen')
    # screen_train.flag = False


if __name__ == "__main__":
    class TestApp(App):
        def build(self):
            sm = ScreenManager()
            sm.add_widget(Train_Screen(name='Train_Screen'))
            sm.add_widget(Train_Start_Screen(name='Train_Start_Screen'))
            sm.add_widget(Ex_Screen(name='Ex_Screen'))
            return sm


    TestApp().run()
