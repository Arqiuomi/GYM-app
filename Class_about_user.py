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


class User_char():
    def __init__(self, iduser_characteristic='1', iduser='1', aim=1, level=2, days='Вт,Чт,Сб', muscule='всё тело',
                 male='М', height=178.3, weight=80.1, fat=15.5, day_counter=0, mark=0,
                 weight_mult=1, number_mult=1, current_plan=1):
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

    def day_counter(self) -> int:
        pass

    def mark(self) -> int:
        pass

    def weight_mult(self) -> float:
        pass

    def number_mult(self) -> float:
        pass
# from work_with_DB import DB
