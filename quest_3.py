class Worker():

    def __init__(self, name, surname, position, income={'wage': 0, 'bonus': 0}):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def __init__(self, name, surname, _income, b):
        super().__init__(name, surname, 'pos', _income)

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


name = input("Введите имя: ")
surname = input("Введите фамилию: ")
try:
    wage = float(input("Введите оклад: "))
    bonus = float(input("Введите размер премии: "))
    w_1 = Position(name, surname, {'wage': wage, 'bonus': bonus})
    print(w_1.name)
    print(w_1.surname)
    print(w_1._income)
    print(w_1.get_full_name())
    print(f'Работник поучит: {w_1.get_total_income()}')
except ValueError:
    print("Оклад или премия заданы не числом")
