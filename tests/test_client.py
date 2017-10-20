# -*- coding: utf-8 -*-
import unittest

from pysigep.client import Client
from pysigep.utils import URLS, HOMOLOGACAO, PRODUCAO


class TestClient(unittest.TestCase):

    def setUp(self):
        super(TestClient, self).setUp()

        self.cliente = Client(ambiente=HOMOLOGACAO,
                              senha='123',
                              usuario='admin')

    def test_consulta_cep(self):

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

        self.cliente.set_ambiente(PRODUCAO)
        self.assertEqual(self.cliente.url_ambiente, URLS[PRODUCAO])

        self.cliente.set_ambiente(HOMOLOGACAO)
        self.assertEqual(self.cliente.url_ambiente, URLS[HOMOLOGACAO])

        with self.assertRaises(KeyError):
            self.cliente.set_ambiente(3)
