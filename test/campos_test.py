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
from sigepweb.sigep_exceptions import ErroCampoObrigatorio
from sigepweb.sigep_exceptions import ErroCampoTamanhoIncorreto
from sigepweb.sigep_exceptions import ErroCampoNaoNumerico
from sigepweb.sigep_exceptions import ErroTipoIncorreto
from sigepweb.campos import CampoBase
from sigepweb.campos import CampoString
from sigepweb.campos import CampoUnicode
from sigepweb.campos import CampoCEP
from sigepweb.campos import CampoCNPJ
from sigepweb.campos import CampoBooleano
from sigepweb.campos import CampoInteiro
from sigepweb.campos import CampoDecimal


class TestCampoBase(TestCase):

    def test_valor(self):
        campo_base = CampoBase('campo_base', obrigatorio=True)
        campo_base.valor = 'TESTE'
        self.assertEqual(campo_base.valor, 'TESTE')

    def test_validar(self):
        campo_base = CampoBase('campo_base', obrigatorio=True)
        self.assertRaises(ErroCampoObrigatorio, campo_base.validar, None)

        campo_base = CampoBase('campo_base', obrigatorio=False)
        self.assertEqual(campo_base.validar('Teste'), True)


class TestCampoString(TestCase):

    def test__formata_valor(self):
        campo_string = CampoString('campo_string')
        self.assertRaises(ErroTipoIncorreto, campo_string._formata_valor, 5)
        self.assertEqual(campo_string._formata_valor('Teste  '), 'Teste')

    def test_validar(self):

        campo_string = CampoString('campo_string', tamanho=3)
        self.assertRaises(ErroCampoTamanhoIncorreto, campo_string.validar,
                          'Teste')

        campo_string = CampoString('campo_string', tamanho=5)
        self.assertEqual(campo_string.validar('Teste'), True)


class TestCampoUnicode(TestCase):

    def test_get_xml(self):
        campo_unicode = CampoUnicode('nome_remetente', valor=u'Empresa Ltda')
        self.assertEqual(campo_unicode.get_xml(), '<nome_remetente>'
                                                  '<![CDATA[Empresa Ltda]]>'
                                                  '</nome_remetente>')


class TestCampoCEP(TestCase):

    def test__formata_valor(self):
        campo_cep = CampoCEP('campo_cep')
        self.assertRaises(ErroTipoIncorreto, campo_cep._formata_valor, 5)
        self.assertEqual(campo_cep._formata_valor('37.800-503'), '37800503')

    def test_validar(self):
        campo_cep = CampoCEP('cep')
        self.assertEqual(campo_cep.validar('37800503'), True)
        self.assertRaises(ErroCampoTamanhoIncorreto, campo_cep.validar,
                          '3780050')
        self.assertRaises(ErroCampoNaoNumerico, campo_cep.validar,
                          '378005AB')


class TestCampoCNPJ(TestCase):

    def test__formata_valor(self):
        campo_cnpj = CampoCNPJ('campo_cnpj')
        self.assertRaises(ErroTipoIncorreto, campo_cnpj._formata_valor, 5)
        self.assertEqual(campo_cnpj._formata_valor('12.345.678./0001-96'),
                         '12345678000196')

    def test_validar(self):
        campo_cnpj = CampoCNPJ('campo_cnpj')
        self.assertEqual(campo_cnpj.validar('12345678000196'), True)
        self.assertRaises(ErroCampoTamanhoIncorreto, campo_cnpj.validar,
                          '1234567800019')
        self.assertRaises(ErroCampoNaoNumerico, campo_cnpj.validar,
                          '123456780001AB')


class TestCampoBoolean(TestCase):

    def test_validar(self):
        campo_bool = CampoBooleano('boolean_teste')
        self.assertEqual(campo_bool.validar(True), True)
        self.assertRaises(ErroTipoIncorreto, campo_bool.validar, 'True')
        self.assertRaises(ErroTipoIncorreto, campo_bool.validar, 1)


class TestCampoInteiro(TestCase):

    def test_validar(self):
        campo_int = CampoInteiro('int_teste')
        self.assertEqual(campo_int.validar(20), True)
        self.assertRaises(ErroTipoIncorreto, campo_int.validar, 'True')
        self.assertRaises(ErroTipoIncorreto, campo_int.validar, 10.5)


class TestCampoDecimal(TestCase):

    def test_validar(self):
        campo_dec = CampoDecimal('decimal_teste')
        self.assertEqual(campo_dec.validar(20.5), True)
        self.assertRaises(ErroTipoIncorreto, campo_dec.validar, 'True')
        self.assertRaises(ErroTipoIncorreto, campo_dec.validar, 10)
