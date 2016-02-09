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
import sigep_exceptions


class CampoBase(object):

    def __init__(self, valor=None, obrigatorio=False):
        self._valor = valor
        self.obrigatorio = obrigatorio

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, val):
        self._valor = val

    def validar(self):
        if self.valor is None and self.obrigatorio:
            raise sigep_exceptions.ErroCampoObrigatorio(
                u'Campo obrigatório vazio')
        return True


class CampoString(CampoBase):

    def __init__(self, valor=None, obrigatorio=False, tamanho=0,
                 numerico=False):
        super(CampoString, self).__init__(valor=valor, obrigatorio=obrigatorio)
        self.tamanho = tamanho
        self.numerico = numerico

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, val):
        self._valor = val.rstrip()

    def validar(self):

        if not isinstance(self.valor, str):
            raise sigep_exceptions.ErroTipoIncorreto('Campo deve ser string')

        if len(self.valor) != self.tamanho:
            raise sigep_exceptions.ErroCampoTamanhoIncorreto(self.valor,
                                                             self.tamanho,
                                                             len(self.valor))

        return super(CampoString, self).validar()


class CampoCEP(CampoString):

    def __init__(self, valor=None, obrigatorio=False):
        super(CampoCEP, self).__init__(valor=valor, obrigatorio=obrigatorio,
                                       tamanho=8, numerico=True)

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, val):
        val = val.replace('-', '')
        val = val.replace('.', '')
        self._valor = val.rstrip()
