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

    def __init__(self, nome, obrigatorio=False):
        self.nome = nome
        self._valor = None
        self._obrigatorio = obrigatorio

    @property
    def obrigatorio(self):
        return self._obrigatorio

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, val):
        val = self._formata_valor(val)
        if self._validar(val):
            self._valor = val

    def _formata_valor(self, valor):
        return valor

    def _validar(self, valor):
        if valor is None and self.obrigatorio:
            raise sigep_exceptions.ErroCampoObrigatorio(self.nome)
        return True

    def get_xml(self):
        return '<{}>{}</{}>'.format(self.nome, self.valor, self.nome)


class CampoString(CampoBase):

    def __init__(self, nome, obrigatorio=False, tamanho=0, numerico=False):
        super(CampoString, self).__init__(nome, obrigatorio=obrigatorio)
        self._tamanho = tamanho
        self._numerico = numerico

    @property
    def tamanho(self):
        return self._tamanho

    @property
    def numerico(self):
        return self._numerico

    def _formata_valor(self, valor):
        if not isinstance(valor, basestring):
            raise sigep_exceptions.ErroTipoIncorreto(self.nome,
                                                     type(valor),
                                                     basestring)
        return valor.rstrip()

    def _validar(self, valor):

        if self.tamanho != 0 and len(valor) != self.tamanho:
            raise sigep_exceptions.ErroCampoTamanhoIncorreto(self.nome,
                                                             self.tamanho,
                                                             len(valor))

        if self.numerico and not valor.isdigit():
            raise sigep_exceptions.ErroCampoNaoNumerico(self.nome)

        return super(CampoString, self)._validar(valor)


class CampoCEP(CampoString):

    def __init__(self, nome, obrigatorio=False):
        super(CampoCEP, self).__init__(nome, obrigatorio=obrigatorio,
                                       tamanho=8, numerico=True)

    def _formata_valor(self, valor):

        if not isinstance(valor, str):
            raise sigep_exceptions.ErroTipoIncorreto(self.nome,
                                                     type(valor),
                                                     str)
        valor = valor.replace('-', '')
        valor = valor.replace('.', '')
        return valor.rstrip()


class CampoBooleano(CampoBase):

    def __init__(self, nome, obrigatorio=False):
        super(CampoBooleano, self).__init__(nome, obrigatorio=obrigatorio)

    def _formata_valor(self, valor):
        return valor

    def _validar(self, valor):

        if not isinstance(valor, bool):
            raise sigep_exceptions.ErroTipoIncorreto(self.nome,
                                                     type(valor),
                                                     bool)
        return super(CampoBooleano, self)._validar(valor)
