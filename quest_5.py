class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        super().draw()
        print("Риуем ручкой")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        super().draw()
        print("Риуем карандашом")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        super().draw()
        print("Риуем маркером")


thing_1 = Pen("Erick")
thing_1.draw()
thing_2 = Handle("Wars")
thing_2.draw()
thing_3 = Pencil("Cohh")
thing_3.draw()
