class Road():

    def __init__(self,lenght, width):
        self._lenght = lenght
        self._width = width

    def mass(self):
        density = 25
        hight = 5
        return self._lenght*self._width*density*hight


road_01 = Road(float(input("Введите длину: ")), float(input("Введите ширину: ")))
print(f'Масса дорожного полотна: {road_01.mass()/1000} т')
