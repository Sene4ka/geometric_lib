import unittest

def area(a, b):
    '''
    Вычисляет площадь прямоугольника со смежными сторонами a, b
    
        Параметры:
            a (float): длина стороны a прямоугольника в виде положительного вещественного числа
            a (float): длина стороны b прямоугольника в виде положительного вещественного числа

        Возвращаемое значение:

            area (float): площадь прямоугольника cо сторонами a, b в виде положительного вещественного числа
    '''
    return a * b


def perimeter(a, b):
    '''
    Вычисляет периметр прямоугольника со смежными сторонами a, b
    
        Параметры:
            a (float): длина стороны a прямоугольника в виде положительного вещественного числа
            b (float): длина стороны b прямоугольника в виде положительного вещественного числа

        Возвращаемое значение:

            perimeter (float): периметр прямоугольника cо сторонами a, b в виде положительного вещественного числа
    '''
    return 2 * (a + b)


class RectangleTestCase(unittest.TestCase):
    def test_area_zero_a(self):
        self.assertEqual(area(0, 3.53498), 0)

        
    def test_area_zero_b(self):
        self.assertEqual(area(2.123, 0), 0)


    def test_area_int(self):
        self.assertEqual(area(3, 4), 12)


    def test_area_float(self):
        self.assertAlmostEqual(area(4.56, 6.46), 29.4576, places=4)


    def test_perimeter_int(self):
        self.assertEqual(perimeter(3, 4), 14)


    def test_perimeter_float(self):
        self.assertAlmostEqual(perimeter(4.56, 6.46), 22.04, places=4)
