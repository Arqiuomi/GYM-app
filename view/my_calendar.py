# -*- coding: utf-8 -*-
# from kivy.lang import Builder
# from kivymd.app import MDApp
# from kivymd.uix.pickers import MDDatePicker
#
# # Загружаем стилизацию для календаря
# Builder.load_string('''
# <CustomLabel@MDLabel>:
#     theme_text_color: "Custom"
#     text_color: 0, 0, 0, 1
#
# <RedLabel@MDLabel>:
#     theme_text_color: "Custom"
#     text_color: 1, 0, 0, 1
#
# <BlueLabel@MDLabel>:
#     theme_text_color: "Custom"
#     text_color: 0, 0, 1, 1
# ''')
#
# class CalendarApp(MDApp):
#     def build(self):
#         self.theme_cls.primary_palette = "Blue"
#         self.show_date_picker()  # Вызываем метод show_date_picker() сразу при запуске приложения
#         return
#
#     def show_date_picker(self):
#         date_dialog = MDDatePicker()
#         date_dialog.bind(on_save=self.on_date_picker_callback)
#         # date_dialog = MDDatePicker(callback=self.on_date_picker_callback)
#         date_dialog.open()
#
#     def on_date_picker_callback(self, instance, date):
#         print(date)
#
# if __name__ == '__main__':
#     CalendarApp().run()
#
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from datetime import datetime, timedelta

KV = '''
<CustomCalendar>:
    cols: 7
    rows: 6
    padding: dp(10)
    spacing: dp(10)

    Label:
        text: "Пн"
        halign: "center"
    Label:
        text: "Вт"
        halign: "center"
    Label:
        text: "Ср"
        halign: "center"
    Label:
        text: "Чт"
        halign: "center"
    Label:
        text: "Пт"
        halign: "center"
    Label:
        text: "Сб"
        halign: "center"
    Label:
        text: "Вс"
        halign: "center"

    # Дни будут добавляться динамически

BoxLayout:
    orientation: 'vertical'
    MDTopAppBar:
        title: "Календарь с особыми датами"
        elevation: 10

    CustomCalendar:
        id: custom_calendar

'''


class CustomCalendar(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.populate_calendar()

    def populate_calendar(self):
        today = datetime.today()
        first_day_of_month = today.replace(day=1)
        last_day_of_month = (first_day_of_month + timedelta(days=31)).replace(day=1) - timedelta(days=1)

        # Заполнение пустыми метками для дней перед первым днем месяца
        for _ in range(first_day_of_month.weekday()):
            self.add_widget(Label(text=''))

        # Заполнение дней месяца
        for day in range(1, last_day_of_month.day + 1):
            date = first_day_of_month.replace(day=day)
            if date.day in [1, 10, 12, 21]:  # Особые даты
                btn = Button(text=str(day), background_color=(1, 0, 0, 1))  # Красный цвет
            else:
                btn = Button(text=str(day), background_color=(1, 1, 1, 1))  # Белый цвет

            btn.bind(on_release=lambda instance, d=date: self.show_date_info(d))
            self.add_widget(btn)

    # Сюда будут записываться названия тренировок
    def show_date_info(self, date):
        popup = Popup(title='Информация', content=Label(text=f"Вы выбрали дату: {date.strftime('%Y-%m-%d')}"),
                      size_hint=(0.5, 0.5))
        popup.open()


class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


if __name__ == "__main__":
    MainApp().run()
