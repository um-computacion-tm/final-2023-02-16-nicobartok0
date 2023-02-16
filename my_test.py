import unittest

from base import Base
from fecha import Fecha
from persona import Persona
from service import Service


class MyTest(unittest.TestCase):

    def setUp(self):
        self.fecha1 = Fecha(2022, 3, 14)
        self.fecha2 = Fecha(2024, 6, 1)
        self.fecha3 = Fecha()
        self.fecha4 = Fecha(1995, 11, 11)
        self.persona1 = Persona(5, 'Perez', self.fecha1)
        self.persona2 = Persona(2, 'Gomez', self.fecha2)
        self.persona3 = Persona(1, 'Diaz', self.fecha3)
        self.persona4 = Persona(4, 'Zen', self.fecha4)

    def test_service_add(self):
        base = Base()
        service = Service()
        service.add(self.persona1, base)
        self.assertEqual(base.data[self.persona1.id], self.persona1)

    def test_order_by_fecha(self):
        control = [self.persona4, self.persona1, self.persona3, self.persona2]
        base = Base()
        service = Service()
        service.add(self.persona1, base)
        service.add(self.persona2, base)
        service.add(self.persona3, base)
        service.add(self.persona4, base)
        resultado = service.order_by_fecha(base)
        self.assertListEqual(resultado, control)

    def test_order_by_apellido(self):
        control = [self.persona3, self.persona2, self.persona1, self.persona4]
        base = Base()
        service = Service()
        service.add(self.persona1, base)
        service.add(self.persona2, base)
        service.add(self.persona3, base)
        service.add(self.persona4, base)
        resultado = service.order_by_apellido(base)
        self.assertListEqual(resultado, control)

    def test_compare_fecha_1(self):
        self.assertEqual(self.fecha1.compare_to(self.fecha2), -1)

    def test_compare_fecha_2(self):
        self.assertEqual(self.fecha3.compare_to(self.fecha3), 0)

    def test_compare_fecha_3(self):
        self.assertEqual(self.fecha3.compare_to(self.fecha4), 1)


if __name__ == '__main__':
    unittest.main()
