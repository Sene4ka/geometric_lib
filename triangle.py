import unittest

def area(a, h):
    '''
    Вычисляет площадь треугольника со стороной a и высотой h, проведенной к стороне a
    
        Параметры:
            a (float): длина стороны a треугольника в виде положительного вещественного числа
            h (float): длина высоты h треугольника, проведенной к стороне a, в виде положительного вещественного числа

        Возвращаемое значение:

            area (float): площадь треугольника со стороной a и высотой h, проведенной к стороне a, в виде положительного вещественного числа
    '''
    return a * h / 2


def perimeter(a, b, c):
    '''
    Вычисляет периметр треугольника со сторонами a, b, c
    
        Параметры:
            a (float): длина стороны a треугольника в виде положительного вещественного числа
            b (float): длина стороны b треугольника в виде положительного вещественного числа
            c (float): длина стороны c треугольника в виде положительного вещественного числа

        Возвращаемое значение:

            perimeter (float): периметр треугольника со сторонами a, b, c в виде положительного вещественного числа
    '''
    return a + b + c


class TriangleTestCase(unittest.TestCase):
    def test_area_zero_a(self):
        self.assertEqual(area(0, 4.42), 0)


    def test_area_zero_h(self):
        self.assertEqual(area(5.673, 0), 0)


    def test_area_int(self):
        self.assertEqual(area(3, 4), 6)


    def test_area_float(self):
        self.assertAlmostEqual(area(6.034, 7.3452), 22.1604684, places=7)


    def test_perimeter_int(self):
        self.assertEqual(perimeter(4, 5, 6), 15)


    def test_perimeter_float(self):
        self.assertAlmostEqual(perimeter(1.23, 4.56, 7.89), 13.68, places=2)
