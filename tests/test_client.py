# -*- coding: utf-8 -*-
from unittest import TestCase, mock

from pysigep.client import Client
from pysigep.utils import URLS, HOMOLOGACAO, PRODUCAO


class TestClient(TestCase):

    def setUp(self):
        super(TestClient, self).setUp()

        self.cliente = Client(ambiente=HOMOLOGACAO,
                              senha='123',
                              usuario='admin')

    def test_consulta_cep(self):

        with mock.patch('zeep.client.Client')as mk:

            mk(URLS[HOMOLOGACAO]).service.consultaCEP.return_value = {
                'bairro': 'Santo Antônio',
                'cep': '37503130',
                'cidade': 'Itajubá',
                'complemento': None,
                'complemento2': '- até 214/215',
                'end': 'Rua Geraldino Campista',
                'id': 0,
                'uf': 'MG',
                'unidadesPostagem': []
            }

            endereco = self.cliente.consulta_cep('37503-130')

            self.assertEqual(endereco['bairro'], 'Santo Antônio')
            self.assertEqual(endereco['cep'], '37503130')
            self.assertEqual(endereco['cidade'], 'Itajubá')
            self.assertEqual(endereco['complemento'], None)
            self.assertEqual(endereco['complemento2'], '- até 214/215')
            self.assertEqual(endereco['end'], 'Rua Geraldino Campista')
            self.assertEqual(endereco['id'], 0)
            self.assertEqual(endereco['uf'], 'MG')
            self.assertEqual(endereco['unidadesPostagem'], [])

    def test_set_ambiente(self):
        self.cliente.ambiente = PRODUCAO
        self.assertEqual(self.cliente.ambiente, PRODUCAO)
        self.assertEqual(self.cliente.url, URLS[PRODUCAO])

        self.cliente.ambiente = HOMOLOGACAO
        self.assertEqual(self.cliente.ambiente, HOMOLOGACAO)
        self.assertEqual(self.cliente.url, URLS[HOMOLOGACAO])

        with self.assertRaises(KeyError):
            self.cliente.ambiente = 3
