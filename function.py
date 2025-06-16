from math import sqrt
from math import sin
from math import cos
import math

class funct:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.y = 0

    def ff(self):
        self.y += sin(math.degrees(self.a))/cos(math.degrees(self.b)) + sqrt(self.c)
        print (self.y)
        print (sin(math.degrees(self.a)))
        print (cos(math.degrees(self.b)))
    


fu = funct(90, 0, 49)
funct.ff(fu)
'первый тест на работу без ошибок'
'ожидается ответ 8, полученный ответ 7.89'
'в чем ошибка: не учел что питон считает в радианах'
