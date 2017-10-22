# -*- coding: utf-8 -*-
from unittest import TestCase, mock

from pysigep.client import Client
from pysigep.utils import URLS, HOMOLOGACAO, PRODUCAO
from pysigep.utils import HOMOG_USUARIO, HOMOG_SENHA, HOMOG_CODIGO_ADMIN


class MockClass:

    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, k, v)


class TestClient(TestCase):

    def setUp(self):
        super(TestClient, self).setUp()

    def test_set_ambiente(self):

        self.cliente = Client(ambiente=HOMOLOGACAO,
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

    def test_consulta_cep(self):

        with mock.patch('zeep.Client')as mk:

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

            self.cliente = Client(ambiente=HOMOLOGACAO,
                                  senha=HOMOG_SENHA,
                                  usuario=HOMOG_USUARIO)

            mk.return_value.service.consultaCEP.return_value = MockClass(
                end_esperado)

            endereco = self.cliente.consulta_cep('37503-130')

            self.assertEqual(endereco.bairro, 'Santo Antônio')
            self.assertEqual(endereco.cep, '37503130')
            self.assertEqual(endereco.cidade, 'Itajubá')
            self.assertEqual(endereco.complemento, None)
            self.assertEqual(endereco.complemento2, '- até 214/215')
            self.assertEqual(endereco.end, 'Rua Geraldino Campista')
            self.assertEqual(endereco.id, 0)
            self.assertEqual(endereco.uf, 'MG')
            self.assertEqual(endereco.unidadesPostagem, [])

    def test_verifica_disponibilidade_servico(self):

        with mock.patch('zeep.Client') as mk:

            params = {
                'cod_administrativo': HOMOG_CODIGO_ADMIN,
                'numero_servico': '04162',
                'cep_origem': '70002900',
                'cep_destino': '70002900',
            }

            self.cliente = Client(ambiente=HOMOLOGACAO,
                                  senha=HOMOG_SENHA,
                                  usuario=HOMOG_USUARIO)

            mk.return_value.service.verificaDisponibilidadeServico.return_value = True
            ret = self.cliente.verifica_disponibilidade_servico(**params)
            self.assertTrue(ret)

            mk.return_value.service.verificaDisponibilidadeServico.return_value = False
            ret = self.cliente.verifica_disponibilidade_servico(**params)
            self.assertFalse(ret)
