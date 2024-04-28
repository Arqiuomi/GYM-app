from work_with_db import DB

db = DB()


class Exercise():
    """Класс упражнение. """

    def __init__(self, id_column=1, name='name', muscule='muscule', description='descr', full_description='fdescr',
                 number=12, weight=80.5):
        self.id_column = id_column
        self.name = name
        self.muscule = muscule
        self.description = description
        self.ful_desc = full_description
        self.number = number
        self.weight = weight

    def init_ex(db, name: str) -> object:
        """Создает экземпляр класса Exercise"""
        selected_ex = db.select_current_ex(name)
        return Exercise(*selected_ex)

    def create_personal_ex(self, user_char: object):
        """Создаёт персональное упражнение нашего юзера - учитываются множители веса и кол-ва повторений"""
        self.weight = self.weight * user_char.weight_mult
        self.number = self.number * user_char.number_mult


# # ПРИМЕР. Создали экземпляр по данным из БД и имени упражнения
# ex = Exercise.init_ex(db, 'Брусья')


