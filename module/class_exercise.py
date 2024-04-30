from work_with_db import DB
import logging



db = DB()

logging.basicConfig(level=logging.INFO, filename='myapp.log', filemode='a',
                    format="%(module)s def %(funcName)s, %(levelname)s: %(message)s")

class Exercise():
    """Класс упражнение"""

    def __init__(self, id_column=1, name='name', muscule='muscule',
                 description='descr', full_description='fdescr',
                 number=12, weight=80.5):
        self.id_column = id_column
        self.name = name
        self.muscule = muscule
        self.description = description
        self.ful_desc = full_description
        self.number = number
        self.weight = weight

    def init_ex(db, name: str) -> object:
        """Создает экземпляр класса Exercise
        Parameters:
            name - название упражнения, которое будем искать в БД
        Returns:
            объект класса Exercise
        """
        try:
            selected_ex = db.select_current_ex(name)
            return Exercise(*selected_ex)

        except AttributeError:
            logging.error(f'Def init_ex, error {AttributeError}. '
                          f'Check the select_current_ex() in class DB.')
            return Exercise(1, 'Жим штанги лёжа', 'грудь',
                            'description', 'full_description', 5, 80)

        except Exception as exc:
            logging.error(f'Def init_ex, error {exc}. '
                          f'Check the connection to the BD.\\ '
                          f'Compare the name in the table exercise_collection'
                          f' and the name of the train')
            return Exercise(1, 'Жим штанги лёжа', 'грудь',
                            'description', 'full_description', 5, 80)

    def create_personal_ex(self, user_char: object):
        """
        Создаёт персональное упражнение нашего юзера -
        учитываются множители веса и кол-ва повторений
        """
        self.weight = self.weight * user_char.weight_mult
        self.number = self.number * user_char.number_mult


# # ПРИМЕР. Создали экземпляр по данным из БД и имени упражнения
ex = Exercise.init_ex(db, 'Брусья')


