# -*- coding: utf-8 -*-
# #############################################################################
#
# The MIT License (MIT)
#
# Copyright (c) 2016 Michell Stuttgart
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
###############################################################################

from unittest import TestCase
import doctest
from pysigep.correios import sign_chancela
from pysigep import correios


class TestCorreios(TestCase):

    def setUp(self):
        self.usuario_correio = {
            'usuario': 'sigep', 'senha': 'n5f9t8',
            'codAdministrativo': '08082650',
            'cepOrigem': '70002900', 'cepDestino': '81350120',
            'numeroServico': '40215', 'idContrato': '9912208555',
            'idCartaoPostagem': '0057018901',
            'cnpj': '34028316000103', 'nome': 'Foo Bar Baz',
            'ano_assinatura': '2008', 'contrato': '9912208555',
            'origem': 'SC', 'postagem': 'RS',
        }

        chancela = open('chancela.txt', 'r')
        self.chancela = chancela.read()
        chancela.close()

    def test_sign_chancela(self):
        chancela = sign_chancela(self.chancela, self.usuario_correio)
        chancela_signed = open('chancela_signed.txt', 'r')
        chancela_right = chancela_signed.read()
        chancela_signed.close()
        self.assertEqual(chancela, chancela_right,
                         'A assinatura da chancela esta incorreta')

    def test_get_eventos(self):
        assert doctest.testmod(correios, raise_on_error=True)
