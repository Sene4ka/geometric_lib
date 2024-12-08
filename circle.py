import math
import unittest


def area(r):
    '''
    Вычисляет площадь круга с радиусом r
    
        Параметры:
            r (float): радиус r круга в виде положительного вещественного числа

        Возвращаемое значение:

            area (float): площадь круга с радиусом r в виде положительного вещественного числа
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Вычисляет периметр(длину окружности) круга с радиусом r
    
        Параметры:
            r (float): радиус r круга в виде положительного вещественного числа

        Возвращаемое значение:

            perimeter (float): периметр(длина окружности) круга с радиусом r в виде положительного вещественного числа
    '''
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    def test_area_zero_r(self):
        self.assertEqual(area(0), 0)

    def test_area_int(self):
        self.assertAlmostEqual(area(3), 28.27433, places=5)


    def test_area_float(self):
        self.assertAlmostEqual(area(6.756), 143.3934, places=4)

    def test_perimeter_zero_r(self):
        self.assertEqual(perimeter(0), 0)


    def test_perimeter_int(self):
        self.assertAlmostEqual(perimeter(4), 25.13274, places=5)


    def test_perimeter_float(self):
        self.assertAlmostEqual(perimeter(7.8769), 49.49202, places=5)
