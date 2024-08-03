# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle
from kivy.utils import get_color_from_hex
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from controller.exercise_window import Exercise_Screen
from controller.exercise_window import Tr_St_Screen
from controller.exercise_window import CalendarDateScreen
from kivy.clock import Clock
import locale
from datetime import datetime, timedelta
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout

locale.setlocale(
    category=locale.LC_ALL,
    locale="Russian"
)


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

    def go_to_calendar(self):
        self.default_view()
        self.manager.current = 'Calendar_Screen'

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
        # print(Exercise_Screen.test())
        self.default_view()
        self.manager.current = 'Ex_Screen'

    def go_to_calendar(self):
        self.default_view()
        self.manager.current = 'Calendar_Screen'

    def go_to_train_start(self):
        self.default_view()
        self.flag = True
        self.manager.current = 'Train_Start_Screen'
        # Обнуляем секунды при переходе в активный режим тренировки
        self.manager.get_screen('Train_Start_Screen').zero_seconds()

    def default_view(self):
        pass


class Train_Start_Screen(Screen):
    def __init__(self, **kwargs):
        super(Train_Start_Screen, self).__init__(**kwargs)
        self.seconds = 0
        self.new_train = True
        self.time()
        self.number_of_ex = self.take_number_of_ex()
        self.current_train()
        self.create_labels()

    # Время
    def time(self):
        Clock.schedule_interval(self.update_time, 1)

    def zero_seconds(self):
        """Обнуляет секунды при переходе на экран активного режима тренировки"""
        self.seconds = 0
        pass

    def update_time(self, *args):
        self.seconds += 1
        minutes = str(self.seconds // 60).zfill(2)
        seconds = str(self.seconds % 60).zfill(2)
        self.ids.time_label.text = f"{minutes}:{seconds}"

    #  Чистка виджетов
    def resert(self):
        # future default_view
        self.seconds = 0
        self.ids.time_label.text = "00:00"
        Clock.unschedule(self.update_time)
        # important!
        # self.clear_ex_number_label()
        # self.clear_ex_info_label()

    def clear_ex_number_label(self):
        layout = self.ids.grid_ex_number
        layout.clear_widgets()

    def clear_ex_info_label(self):
        layout = self.ids.active_train_mode
        layout.remove_widget(layout.children[0])

    # Параметры тренировки
    @staticmethod
    def take_number_of_ex():
        """Принимает и возвращает количество упражнений в текущей тренировке из контроллера"""
        return Tr_St_Screen.take_number_of_ex()

    def create_ex_number_label(self):
        """Создаёт lables с номерами упражнений"""
        if self.new_train:
            layout = self.ids.grid_ex_number
            for i in range(1, self.number_of_ex + 1):
                # disabled делает кнопки неактивными
                button = Button(text=f'{i}', color=(1, 1, 1, 1),
                                background_color=(182 / 255, 66 / 255, 245 / 255, 1), disabled=True)
                layout.add_widget(button)
                # Делает активным 1ую кнопку
                button = layout.children[len(layout.children) - Tr_St_Screen.ex_counter()]
                button.state = 'down'
                # Устанавливаем белый цвет текста
                button.disabled_color = get_color_from_hex('#FFFFFF')
                # # Отключаем фон для кнопки в состоянии disabled
                button.background_disabled_normal = ''

    def current_number(self):
        """Подсвечивает номер текущего упражнения"""
        layout = self.ids.grid_ex_number
        button = layout.children[len(layout.children) - Tr_St_Screen.ex_counter()]
        button.state = 'down'
        button.disabled_color = get_color_from_hex('#FFFFFF')  # Устанавливаем белый цвет текста
        button.background_disabled_normal = ''  # Отключаем фон для кнопки в состоянии disabled

    def check_ex_counter(self) -> bool:
        if Tr_St_Screen.ex_counter() < self.take_number_of_ex():
            return True
        return False

    def call_next_ex(self):
        """Вызывает следующее упражнение"""
        if self.check_ex_counter():
            Tr_St_Screen.call_train()
        else:
            self.resert()
            self.manager.get_screen('Train_Screen').flag = False
            self.manager.current = 'Train_Finish_Screen'

    def current_train(self):
        """Выводит в label название упражнения"""
        self.ids.train_label.text = Tr_St_Screen.take_ex_name()

    @staticmethod
    def take_ex_inform():
        return Tr_St_Screen.take_ex_info()

    def create_ex_info(self):
        ex_inform = self.take_ex_inform()
        self.ids.ex_info_label.text = f' Вес: {ex_inform[0]} \n \n Повторы: {ex_inform[1]}'

    def create_labels(self):
        layout = self.ids.grid_ex_number
        layout.cols = self.number_of_ex
        self.create_ex_number_label()
        self.create_ex_info()
        self.new_train = False

    def go_to_ex(self):
        self.manager.current = 'Ex_Screen'

    def go_to_calendar(self):
        self.default_view()
        self.manager.current = 'Calendar_Screen'

    # Опустить флажок, когда тренировка закончится
    # screen_train = self.manager.get_screen('Train_Screen')
    # screen_train.flag = False


class Train_Finish_Screen(Screen):

    def go_to_train(self):
        self.default_view()
        self.manager.current = 'Train_Screen'

    def go_to_ex(self):
        self.manager.current = 'Ex_Screen'

    def default_view(self):
        pass


class Calendar_Screen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_calendar()

    def create_calendar(self):
        # Устанавливаем текущую дату
        today = datetime.now()
        first_day_of_month = today.replace(day=1)

        # Получаем номер первого дня недели для первого дня месяца
        start_day = first_day_of_month.weekday()
        days_in_month = (first_day_of_month.replace(month=today.month % 12 + 1) - timedelta(days=1)).day
        # Создаём основной лэйбл
        main_layout = AnchorLayout(anchor_x='center', anchor_y='top')
        top_layout = BoxLayout(orientation='vertical', size_hint=[1, .7])
        # Создаём бокс для названия месяца
        label = Label(text=str(today.strftime('%B')), size_hint=[1, .1])
        top_layout.add_widget(label)

        # Создаём сетку для календаря
        grid = GridLayout(cols=7, spacing=20, size_hint_y=None, padding=[0, 40, 0, 0])
        grid.bind(minimum_height=grid.setter('height'))

        # Добавляем заголовок дней недели
        weekdays = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
        for day in weekdays:
            grid.add_widget(Label(text=day))

        # Добавляем пустые ячейки до первого дня месяца
        for _ in range(start_day):
            grid.add_widget(Label())

        # Добавляем дни месяца
        for day in range(1, days_in_month + 1):
            # btn = Button(text=str(day), size_hint_y=None, height=80)
            btn = Button(text=str(day), size_hint_y=None, height=70)
            btn.bind(on_release=self.on_date_select)

            # Выделяем определённые даты
            # if day in CalendarDateScreen.find_train_day():
            if day in CalendarDateScreen.find_train_day():
                btn.background_color = (1, 0, 0, 1)  # Красный цвет
                btn.color = (1, 1, 1, 1)  # Белый текст

            grid.add_widget(btn)
        # Добавляем календарь в основной лэйбл
        top_layout.add_widget(grid)
        # main_layout.add_widget(Builder.load_file('calendar_bar.kv'))
        main_layout.add_widget(top_layout)
        self.add_widget(main_layout)

    def on_date_select(self, instance):
        date_selected = instance.text
        date = self._find_date(date_selected)

        if int(date_selected) in CalendarDateScreen.find_train_day():

            popup = Popup(title='Выбранная дата', content=Label(text=f'Cегодня {date}. У тебя тренировка'),
                          size_hint=(0.5, 0.5))
            popup.open()
        else:
            popup = Popup(title='Выбранная дата', content=Label(text=f'Сегодня {date}. Отдыхай.'),
                          size_hint=(0.5, 0.5))
            popup.open()

    def _find_date(self, day: str):
        date = datetime(year=datetime.today().year, month=datetime.today().month, day=int(day))
        return datetime.strftime(date, '%B, %#d число')

    def go_to_train(self):
        self.default_view()
        screen_train = self.manager.get_screen('Train_Screen')
        if screen_train.flag:
            self.manager.current = 'Train_Start_Screen'
        else:
            self.manager.current = 'Train_Screen'

    def go_to_ex(self):
        self.default_view()
        self.manager.current = 'Ex_Screen'

    def default_view(self):
        pass

class MenuApp(App):
    def build(self):
        Builder.load_file('menu_screen.kv', encoding='CP1251')
        sm = ScreenManager()
        sm.add_widget(Train_Screen(name='Train_Screen'))
        sm.add_widget(Train_Start_Screen(name='Train_Start_Screen'))
        sm.add_widget(Ex_Screen(name='Ex_Screen'))
        sm.add_widget(Train_Finish_Screen(name='Train_Finish_Screen'))
        sm.add_widget(Calendar_Screen(name="Calendar_Screen"))
        return sm


if __name__ == "__main__":
    MenuApp().run()
