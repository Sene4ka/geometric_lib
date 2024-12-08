import unittest

def area(a):
    '''
    Возвращает площадь квадрата со стороной a
    
        Параметры:
            a (float): длина стороны a квадрата в виде положительного вещественного числа

        Возвращаемое значение:

            area (float): площадь квадрата со стороной a в виде положительного вещественного числа
    '''
    return a * a


def perimeter(a):
    '''
    Возвращает периметр квадрата со стороной a
    
        Параметры:
            a (float): длина стороны a квадрата в виде положительного вещественного числа

        Возвращаемое значение:

            perimeter (float): периметр квадрата со стороной a в виде положительного вещественного числа
    '''
    return 4 * a


class SquareTestCase(unittest.TestCase):
    def test_area_zero_a(self):
        self.assertEqual(area(0), 0)


    def test_area_int(self):
        self.assertEqual(area(3), 9)


    def test_area_float(self):
        self.assertAlmostEqual(area(8.32354), 69.28132, places=5)

    def test_perimeter_zero_a(self):
        self.assertEqual(perimeter(0), 0)


    def test_perimeter_int(self):
        self.assertEqual(perimeter(4), 16)


    def test_perimeter_float(self):
        self.assertAlmostEqual(perimeter(7.8769), 31.5076, places=4)
