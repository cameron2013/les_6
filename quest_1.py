import time


class TrafficLight():

    def __init__(self):
        self.__color = ""

    def running(self):
        self.__color = "red"
        print(self.__color)
        time.sleep(7)
        self.__color = "yellow"
        print(self.__color)
        time.sleep(2)
        self.__color = "green"
        print(self.__color)
        time.sleep(4)
        self.running()


TrafficLight_01 = TrafficLight()
TrafficLight_01.running()
