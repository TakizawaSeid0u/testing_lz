import math

def funcia(a, b, c):
    
    if not a or not b or not c:
        return "Ошибка ввода: пустой ввод"

    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except (ValueError, TypeError):
        return "Ошибка! ожидается число" if isinstance(a, str) else "Ошибка: неправильный тип данных"

    if c < 0:
        return "ошибка! значение c должно быть неотрицательным"

    a_rad = math.radians(a)
    b_rad = math.radians(b)

    if abs(math.cos(b_rad)) < 00000000000000.1:
        return "ошибка! деление на ноль"

    return (math.sin(a_rad) / math.cos(b_rad)) + math.sqrt(c)