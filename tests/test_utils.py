from unittest import TestCase

from pysigep.utils import validar, trim


class TestUtils(TestCase):
    """Testa funcionalidades da classe Utils
    """

    def setUp(self):
        super(TestUtils, self).setUp()

    def test_validar_cep(self):

        # Testando com CEP corretos
        validar('cep', '37503130')

        # Realizando os testes com CEP invalidos que lancam excecao
        self.assertRaises(ValueError, validar, 'cep', '3750313A')
        self.assertRaises(ValueError, validar, 'cep', '3750313')

    def test_validar_cod_administrativo(self):

        # Validamos Codigo Administrativo
        validar('codAdministrativo', '12345678')

        # Realizamos o teste com Codigo Admin invalido
        self.assertRaises(ValueError, validar,
                          'codAdministrativo', '123456789')
        self.assertRaises(ValueError, validar, 'codAdministrativo', '1234567')

    def test_validar_etiqueta(self):

        # Validamos uma etiqueta correta
        validar('etiqueta', 'DL76023727 BR')

        # Validamos etiquetas invalidas
        with self.assertRaises(ValueError):
            validar('etiqueta', 'DL76023727BR')

        with self.assertRaises(ValueError):
            validar('etiqueta', 'DL760237275BR')

        with self.assertRaises(ValueError):
            validar('etiqueta', '3L76023727 BR')

        with self.assertRaises(ValueError):
            validar('etiqueta', 'DLA6023727 BR')

    def test_trim(self):
        self.assertEqual(trim('37.503-130'), '37503130')
