from User_Char_Const import d_mark, d_aim_mult, d_male_mult, d_level_mult
class User():

    def __init__(self, iduser='1', login='log', email='email', password='pswrd'):
        self.iduser = iduser
        self.login = login
        self.email = email
        self.password = password

    def iduser(self):
        # DB.get_iduser(self)
        pass

    # @set


class User_Char():
    H, W, FAT = 180, 80, 10

    def __init__(self, iduser_characteristic='1', iduser='1', aim=1, level=1, days='Вт,Чт,Сб', muscule='всё тело',
                 male='М', height=178.3, weight=100.1, fat=15.5, day_counter=0, mark=0, weight_mult=1.1, number_mult=1.1,
                 current_plan=1):
        self.iduser_characteristic = iduser_characteristic
        self.iduser = iduser
        self.aim = aim
        self.level = level
        self.days = days
        self.muscule = muscule
        self.male = male
        self.height = height
        self.weight = weight
        self.fat = fat
        self.day_counter = day_counter
        self.mark = mark
        self.weight_mult = weight_mult
        self.number_mult = number_mult
        self.current_plan = current_plan
        self.all_stat = self.all_stat()

    def all_stat(self) -> list:
        return [
            self.aim,
            self.level,
            self.days,
            self.muscule,
            self.male,
            self.height,
            self.weight,
            self.fat,
            self.day_counter,
            self.mark,
            self.weight_mult,
            self.number_mult,
            self.current_plan
        ]

    def day_counter(self, train_start: bool) -> int:
        """Подсчитывает число выполненных тренировок за месяц"""
        if train_start():
            self.day_counter += 1
            return self.day_counter

            pass

    def set_mark(self, key: str) -> int:
        self.mark += d_mark[key]
        return self.mark


    def set_weight_mult(self) -> float:
        p1 = 0.8
        p2 = 0.9
        self.weight_mult = d_male_mult[self.male] * d_level_mult[self.level] * d_aim_mult[self.aim]

        return round(self.weight_mult, 2)


    def set_number_mult(self) -> float:
        p1 = 0.7
        p2 = 0.8

        self.number_mult = d_male_mult[self.male] * d_level_mult[self.level] * d_aim_mult[self.aim] * (
                p1 * self.height / User_Char.H +
                +p2 * self.weight * (100 - self.fat) / (User_Char.W * (100 - User_Char.FAT)))
        return round(self.number_mult, 2)


# from work_with_DB import DB


def train_start(event=True) -> bool:
    """Пользователь начал тренировку"""
    if event:
        return True
    return False


def mark(key) -> int:
    """Возвращает оценку тренировки"""
    d = {'трудно': 0,
         'круто': 1,
         'легко': 2}

    return d[key]

