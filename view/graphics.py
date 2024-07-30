# python -m pip install https://github.com/kivy-garden/graph/archive/master.zip

from math import sin
from kivy_garden.graph import Graph, MeshLinePlot
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

# Какой-то график, который будет создаваться по статистике пользователя
graph = Graph(xlabel='X', ylabel='Y', x_ticks_minor=5,
              x_ticks_major=25, y_ticks_major=1,
              y_grid_label=True, x_grid_label=True, padding=5,
              x_grid=True, y_grid=True, xmin=-0, xmax=100, ymin=-1, ymax=1)
plot = MeshLinePlot(color=[1, 0, 0, 1])
plot.points = [(x, sin(x / 10.)) for x in range(0, 101)]
graph.add_plot(plot)


# Класс виджета
class GraphWidget(FloatLayout):
    """Создаём виджет"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.add_widget(graph)
        self.graph = Graph()
        self.ids.graph.add_widget(self/graph)

# Класс приложения
class MainApp(App):
    def build(self):
        # возвращаем "вмещающий" виджет
        return GraphWidget()


MainApp().run()
