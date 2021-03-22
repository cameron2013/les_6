import time
import turtle as tr


class TrafficLight():

    def __init__(self):
        self.__color = ""

    def running(self):
        tr.hideturtle()
        tr.speed('fastest')
        self.__color = "red"
        print(self.__color)
        tr.down
        tr.begin_fill()
        tr.fillcolor(self.__color)
        tr.circle(50)
        tr.end_fill()
        tr.up
        time.sleep(7)
        self.__color = "yellow"
        print(self.__color)
        tr.down
        tr.begin_fill()
        tr.fillcolor(self.__color)
        tr.circle(50)
        tr.end_fill()
        tr.up
        time.sleep(2)
        self.__color = "green"
        print(self.__color)
        tr.down
        tr.begin_fill()
        tr.fillcolor(self.__color)
        tr.circle(50)
        tr.end_fill()
        tr.up
        time.sleep(4)
        self.running()


TrafficLight_01 = TrafficLight()
TrafficLight_01.running()
