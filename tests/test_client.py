from unittest import TestCase, mock

from pysigep.client import SOAPClient
from pysigep.utils import URLS, HOMOLOGACAO, PRODUCAO
from pysigep.utils import (HOMOG_USUARIO,
                           HOMOG_SENHA,
                           HOMOG_CODIGO_ADMIN,
                           HOMOG_CARTAO)


class MockClass:
    """Mock Class criada para simular o objeto retornado pela
    zeepe
    """

    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, k, v)


class TestClient(TestCase):

    def setUp(self):
        super(TestClient, self).setUp()

    def test_set_ambiente(self):

        self.cliente = SOAPClient(ambiente=HOMOLOGACAO,
                                  senha=HOMOG_SENHA,
                                  usuario=HOMOG_USUARIO)

        self.cliente.ambiente = PRODUCAO
        self.assertEqual(self.cliente.ambiente, PRODUCAO)
        self.assertEqual(self.cliente.url, URLS[PRODUCAO])

        self.cliente.ambiente = HOMOLOGACAO
        self.assertEqual(self.cliente.ambiente, HOMOLOGACAO)
        self.assertEqual(self.cliente.url, URLS[HOMOLOGACAO])

        with self.assertRaises(KeyError):
            self.cliente.ambiente = 3

    @mock.patch('zeep.Client')
    def test_consulta_cep(self, mk):
  
        end_esperado = {
            'bairro': 'Santo Antônio',
            'cep': '37503130',
            'cidade': 'Itajubá',
            'complemento': None,
            'complemento2': '- até 214/215',
            'end': 'Rua Geraldino Campista',
            'id': 0,
            'uf': 'MG',
            'unidadesPostagem': [],
        }

        # Sobrescrevemos o client para que o mock funcione
        self.cliente = SOAPClient(ambiente=HOMOLOGACAO,
                                  senha=HOMOG_SENHA,
                                  usuario=HOMOG_USUARIO)

        consulta_cep = self.cliente.consulta_cep

        # Criamos o mock para o valor de retorno
        mk.return_value.service.consultaCEP.return_value = MockClass(
            end_esperado)

        # Realizamos a consulta de CEP
        endereco = consulta_cep('37503-130')

        self.assertEqual(endereco.bairro, 'Santo Antônio')
        self.assertEqual(endereco.cep, '37503130')
        self.assertEqual(endereco.cidade, 'Itajubá')
        self.assertEqual(endereco.complemento, None)
        self.assertEqual(endereco.complemento2, '- até 214/215')
        self.assertEqual(endereco.end, 'Rua Geraldino Campista')
        self.assertEqual(endereco.id, 0)
        self.assertEqual(endereco.uf, 'MG')
        self.assertEqual(endereco.unidadesPostagem, [])

        self.assertRaises(ValueError, consulta_cep, '375031300')
        self.assertRaises(ValueError, consulta_cep, '3750313')
        self.assertRaises(TypeError, consulta_cep, 37503130)

    @mock.patch('zeep.Client')
    def test_verifica_disponibilidade_servico(self, mk):

        params = {
            'cod_administrativo': HOMOG_CODIGO_ADMIN,
            'numero_servico': '04162',
            'cep_origem': '70002900',
            'cep_destino': '70.002-900',
        }

        # Sobrescrevemos o client para que o mock funcione
        self.cliente = SOAPClient(ambiente=HOMOLOGACAO,
                                  senha=HOMOG_SENHA,
                                  usuario=HOMOG_USUARIO)

        service = mk.return_value.service

        service.verificaDisponibilidadeServico.return_value = True
        ret = self.cliente.verifica_disponibilidade_servico(**params)
        self.assertTrue(ret)

        service.verificaDisponibilidadeServico.return_value = False
        ret = self.cliente.verifica_disponibilidade_servico(**params)
        self.assertFalse(ret)

    @mock.patch('zeep.Client')
    def test_get_status_cartao_postagem(self, mk):

        params = {
            'numero_cartao_postagem': HOMOG_CARTAO,
        }

        # Sobrescrevemos o client para que o mock funcione
        self.cliente = SOAPClient(ambiente=HOMOLOGACAO,
                                  senha=HOMOG_SENHA,
                                  usuario=HOMOG_USUARIO)

        service = mk.return_value.service

        service.getStatusCartaoPostagem.return_value = 'Normal'
        ret = self.cliente.get_status_cartao_postagem(**params)
        self.assertEqual(ret, 'Normal')

        service.getStatusCartaoPostagem.return_value = 'Cancelado'
        ret = self.cliente.get_status_cartao_postagem(**params)
        self.assertEqual(ret, 'Cancelado')
