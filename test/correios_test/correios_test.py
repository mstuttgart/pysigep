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
import os

from pysigep.correios import calcular_preco_prazo
from pysigep.correios import sign_chancela


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
            'nCdEmpresa': '08082650', 'sDsSenha': 'n5f9t8',
            'nCdServico': '40215', 'sCepOrigem': '05311900',
            'sCepDestino': '83010140', 'nVlPeso': 1, 'nCdFormato': 1,
            'nVlComprimento': 20, 'nVlAltura': 20, 'nVlLargura': 20,
            'nVlDiametro': 20, 'sCdMaoPropria': 'S',
            'nVlValorDeclarado': 0, 'sCdAvisoRecebimento': 'S',
        }

        path = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(path, 'chancela.txt')

        with open(path, 'r') as chancela:
            self.chancela = chancela.read()

    def test_sign_chancela(self):
        path = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(path, 'chancela_signed.txt')
        chancela = sign_chancela(self.chancela, self.usuario_correio)

        with open(path, 'r') as chancela_signed:
            chancela_right = chancela_signed.read()

        self.assertEqual(chancela, chancela_right,
                         'A assinatura da chancela esta incorreta')

    def test_calcular_preco_prazo(self):
        codigo = calcular_preco_prazo(**self.usuario_correio).cServico.Codigo
        self.assertEqual(40215, codigo)
        self.usuario_correio['sCepDestino'] = '12345678'
        erro = calcular_preco_prazo(**self.usuario_correio).cServico.Erro
        self.assertEqual(8, erro)
