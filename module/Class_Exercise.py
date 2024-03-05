from abc import ABC, abstractmethod

class Exercise(ABC):
    """Класс упражнение. """

    def __init__(self, name='name', muscule ='muscule',  description='descr', full_description='fdescr', number=12, weight=80.5):
        self.name = name
        self.muscule = muscule
        self.description = description
        self.ful_desc = full_description
        self.number = number
        self.weight = weight

class Chest_Ex(Exercise):
    def __init__(self):
        super().__init__()

