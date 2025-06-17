from math import sin, cos, sqrt, isclose, pi

class func:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.y = 0.0

    def funn(self):
        try:
            if not all(isinstance(x, (int, float)) for x in [self.a, self.b, self.c]):
                raise TypeError("все параметры должны быть числами")
            
            z = cos(self.b)
            if isclose(z, 0, abs_tol=1e-10):
                raise ValueError("cos(b) слишком близок к нулю значит деление невозможно")
            if self.c < 0:
                raise ValueError("отрицательное под корнем")
            result = sin(self.a) / z + sqrt(self.c)
            self.y += result
            return result
        except Exception as e:
            print(f"ошибка вычисления: {str(e)}")
            return None

if __name__ == "__main__":
    print("Тест 1: все нормально")
    ff1 = func(1.0, 0.5, 4.0)
    print(ff1.funn()) 
    
    print("Тест 2: попытка деления на 0")
    ff2 = func(0, pi/2, 1)
    ff2.funn()
    
    print("Тест 3: отрицательное под корнем")
    ff3 = func(0, 0, -1)
    ff3.funn()
    
    print("Тест 4: данные не того типа")
    ff4 = func("1", 0, 1)
    ff4.funn()
