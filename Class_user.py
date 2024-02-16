# from work_with_DB import DB
class User():
    def __init__(self, login='log', email='email', password='pswrd'):
        self.login = login
        self.email = email
        self.password = password
        self.day_counter = self.day_counter()
        self.weight_mult=self.weight_mult()
        self.number_mult=self.number_mult()

    def iduser(self):
        # DB.get_iduser(self)
        pass
    # @set
    def day_counter(self)->int:
        pass

    def mark(self)->int:
        pass

    def weight_mult(self)->float:
        pass

    def number_mult(self)->float:
        pass
