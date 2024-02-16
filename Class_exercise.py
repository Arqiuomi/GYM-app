from abc import ABC, abstractmethod

class Exercise(ABC):
    """Класс упражнение. """

    def __init__(self, name='name', description='descr', full_description='fdescr', number=12, weight=80):
        self.name = name
        self.description = description
        self.ful_desc = full_description
        self.number = number
        self.weight = weight

class Chest_ex(Exercise):
    def __init__(self):
        super().__init__()

