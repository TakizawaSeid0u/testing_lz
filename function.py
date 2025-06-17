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
        if self.c >= 0:
            self.y += sin((self.a))/cos((self.b)) + sqrt(self.c)
            print (self.y)
        else:
            print('ОШИБКА - отрицательное число под корнем')
    


fu = funct(90, 0, 49)
funct.ff(fu)
'первый тест на работу без ошибок'
'ожидается ответ 8, полученный ответ 7.89'
'в чем ошибка: не учел что питон считает в радианах'

'второй тест с учетом углов в радианах'
'ожидаемый ответ 7.893996, полученный ответ 7.893996'

'третий тест с попыткой возведения отрицательного числа под корень'
'ожидаемый ответ: ОШИБКА, полученный ответ 7.893996'
'исправление: добавлен if'



