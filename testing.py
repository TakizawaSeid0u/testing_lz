import math
from function import func
import unittest
from math import pi



result = func("",3,4)
   
class AH(unittest.TestCase):

    def test(self):
        self.assertEqual(func(0, pi/2, 1),'деление на ноль')

    def test_num_under_the_root(self):
        self.assertEqual(func(pi, pi/2, 49), 'извлечение корня из отрицательного числа')
    
    def test_strings(self):
        self.assertEqual(func("",pi/2,49),'ошибка типов данных')

    
if __name__ == "__main__":
    unittest.main() 


'''1.деление на 0
2.отрицательное под корнем
3.не тот тип данных'''