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
from sigep.sigep_exceptions import ErroCampoObrigatorio
from sigep.sigep_exceptions import ErroCampoTamanhoIncorreto
from sigep.sigep_exceptions import ErroCampoNaoNumerico
from sigep.campos import CampoBase
from sigep.campos import CampoString


class TestCampoBase(TestCase):

    def test_validar(self):

        campo_base = CampoBase('campo_base', obrigatorio=True)
        self.assertRaises(ErroCampoObrigatorio, campo_base.validar)

        campo_base.obrigatorio = False
        self.assertEqual(campo_base.validar(), True)


class TestCampoString(TestCase):

    def test_validar(self):

        campo_string = CampoString('campo_string')
        campo_string.valor = 'Teste'
        campo_string.tamanho = '3'

        self.assertRaises(ErroCampoTamanhoIncorreto, campo_string.validar)

        campo_string.tamanho = 5
        self.assertEqual(campo_string.validar(), True)

        campo_string.numerico = True
        campo_string.valor = '254TE'
        self.assertRaises(ErroCampoNaoNumerico, campo_string.validar)
