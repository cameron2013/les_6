class Car():

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Автомобиль поехал")

    def stop(self):
        print("Автомобиль остановился")
        self.speed = 0

    def turn(self, direction):
        print(f"Автмобиль поехал {direction}")

    def show_speed(self):
        print(f"Скорость автомобиля {self.speed} км/ч")


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Превышение скорости")


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Превышение скорости")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


auto_1 = TownCar(50, 'red', 'Mazda')
auto_1.show_speed()
auto_1.turn("назад")
auto_1.turn("направо")
print(auto_1.is_police)
auto_2 = WorkCar(50, 'blue', 'Toyota')
auto_2.show_speed()
auto_2.go()
auto_2.stop()
auto_2.show_speed()
auto_3 = PoliceCar(100, 'green', 'Lada')
auto_3.show_speed()
print(auto_3.is_police)
