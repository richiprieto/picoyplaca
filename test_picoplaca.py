import unittest
from picoplaca import PicoPlaca

class TestPicoPlaca(unittest.TestCase):
    #False puede circular
    #True no puede circular
    def setUp(self):
        self.picoplaca = PicoPlaca("abc-1234","2019-01-29","07:00")

    def test_valida_hora(self):
        self.assertEqual(self.picoplaca.valida_hora(),True)
        self.picoplaca.hora="06:59"
        self.assertEqual(self.picoplaca.valida_hora(),False)
        self.picoplaca.hora="08:13"
        self.assertEqual(self.picoplaca.valida_hora(),True)
        self.picoplaca.hora = "09:30"
        self.assertEqual(self.picoplaca.valida_hora(),True)
        self.picoplaca.hora = "09:31"
        self.assertEqual(self.picoplaca.valida_hora(),False)
        self.picoplaca.hora="15:59"
        self.assertEqual(self.picoplaca.valida_hora(),False)
        self.picoplaca.hora="16:00"
        self.assertEqual(self.picoplaca.valida_hora(),True)
        self.picoplaca.hora = "17:27"
        self.assertEqual(self.picoplaca.valida_hora(),True)
        self.picoplaca.hora = "19:30"
        self.assertEqual(self.picoplaca.valida_hora(),True)
        self.picoplaca.hora = "19:31"
        self.assertEqual(self.picoplaca.valida_hora(),False)

    def test_valida_fecha(self):
        self.assertEqual(self.picoplaca.valida_fecha(),True)
        self.picoplaca.fecha = "2019-02-26"
        self.assertEqual(self.picoplaca.valida_fecha(),True)
        self.picoplaca.fecha = "2019-03-14"
        self.assertEqual(self.picoplaca.valida_fecha(),True)
        self.picoplaca.fecha = "2019-04-04"
        self.assertEqual(self.picoplaca.valida_fecha(),True)
        self.picoplaca.fecha = "2019-05-31"
        self.assertEqual(self.picoplaca.valida_fecha(),True)
        self.picoplaca.fecha = "2019-06-01"
        self.assertEqual(self.picoplaca.valida_fecha(),False)
        self.picoplaca.fecha = "2019-07-28"
        self.assertEqual(self.picoplaca.valida_fecha(),False)

    def test_prediccion(self):
        self.picoplaca.fecha = "2019-01-26"
        self.assertEqual(self.picoplaca.prediccion(),False)
        self.picoplaca.placa = "abc-1232"
        self.picoplaca.fecha = "2019-01-28"
        self.picoplaca.hora = "07:00"
        self.assertEqual(self.picoplaca.prediccion(),True)
        self.picoplaca.placa = "abc-8910"
        self.picoplaca.fecha = "2019-08-30"
        self.picoplaca.hora = "07:00"
        self.assertEqual(self.picoplaca.prediccion(),True)
        self.picoplaca.hora = "06:00"
        self.assertEqual(self.picoplaca.prediccion(),False)

if __name__ == '__main__':
    unittest.main()
