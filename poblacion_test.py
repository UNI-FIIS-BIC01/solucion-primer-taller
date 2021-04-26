from unittest import TestCase, mock
import io
import sys

import poblacion


class PoblacionTest(TestCase):

    @mock.patch('poblacion.input', create=True)
    def test_poblacion(self, input_mock):
        input_mock.side_effect = ["7.9", "1.05"]
        resultado_test = io.StringIO()
        sys.stdout = resultado_test

        poblacion.iniciar()

        with open('test/poblacion_test.txt') as archivo_test:
            resultado_esperado = archivo_test.readlines()

        resultado_actual = resultado_test.getvalue().strip().split('\n')
        self.assertEqual(len(resultado_esperado), len(resultado_actual))

        for linea_esperada, linea_actual in zip(resultado_esperado, resultado_actual):
            self.assertEqual(linea_esperada.strip(), linea_actual.strip())
