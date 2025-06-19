from function import funcia
import unittest

class Testfuncia(unittest.TestCase):

    def test_zero_division(self):
        self.assertEqual(funcia("30", "90", "9"), "Ошибка! деление на ноль")

    def test_negative_under_root(self):
        self.assertEqual(funcia("45", "45", "-9"), "Ошибка ввода! значение c должно быть неотрицательным")

    def test_non_numeric(self):
        self.assertEqual(funcia("abc", "60", "5"),"Ошибка ввода! введено не число")

    def test_empty_input(self):
        self.assertEqual(funcia("", "45", "5"), "Ошибка ввода! пустой ввод")

    def test_type_error(self):
        self.assertEqual(funcia(["30"], "45", "4"), "Ошибка! неверный тип данных")

if __name__ == "__main__":
    unittest.main()