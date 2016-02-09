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
from sigep.sigep_exceptions import ErroTipoIncorreto
from sigep.sigep_exceptions import ErroCampoTamanhoIncorreto
from sigep.campos import CampoBase
from sigep.campos import CampoString


class TestCampoBase(TestCase):

    def test_validar(self):

        campo = CampoBase(obrigatorio=True)
        self.assertRaises(ErroCampoObrigatorio, campo.validar)

        campo.obrigatorio = False
        self.assertEqual(campo.validar(), True)


class TestCampoString(CampoBase):

    def test_validar(self):

        if isinstance(self.valor, str):
            raise ErroTipoIncorreto('Campo deve ser string')

        if len(self.tamanho) != self.tamanho:
            raise ErroCampoTamanhoIncorreto(self.valor, self.tamanho,
                                            len(self.valor))
        super(CampoString, self).validar()
