from unittest import TestCase

from pysigep.utils import validar, trim


class TestUtils(TestCase):
    """Testa funcionalidades da classe Utils
    """

    def setUp(self):
        super(TestUtils, self).setUp()

    def test_validar(self):
        """Testa o funcionamento da funcao 'validar'
        """

        # Testando com CEP corretos
        validar('cep', '37503130')

        # Realizando os testes com CEP invalidos que lancam excecao
        self.assertRaises(ValueError, validar, 'cep', '3750313A')
        self.assertRaises(ValueError, validar, 'cep', '3750313')
        self.assertRaises(TypeError, validar, 'cep', 37503130)

        # Validamos Codigo Administrativo
        validar('codAdministrativo', '12345678')

        # Realizamos o teste com Codigo Admin invalido
        self.assertRaises(ValueError, validar,
                          'codAdministrativo', '123456789')
        self.assertRaises(ValueError, validar, 'codAdministrativo', '1234567')
        self.assertRaises(TypeError, validar, 'codAdministrativo', 12345678)

    def test_trim(self):
        """Testa funcionamento da funcao 'trim'
        """
        self.assertEqual(trim('37.503-130'), '37503130')
