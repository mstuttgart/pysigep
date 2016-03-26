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

    def __init__(self, nome, valor=None, obrigatorio=False):
        self.nome = nome
        self._valor = valor
        self.obrigatorio = obrigatorio

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, val):
        self._valor = val

    def validar(self, valor):
        if valor is None and self.obrigatorio:
            raise sigep_exceptions.ErroCampoObrigatorio(self.nome)
        return True

    def get_xml(self):
        valor = self.valor if self.valor is not None else ''
        return u'<{}>{}</{}>'.format(self.nome, valor, self.nome)


class CampoString(CampoBase):

    def __init__(self, nome, valor=None, obrigatorio=False, tamanho=0,
                 numerico=False):
        super(CampoString, self).__init__(nome, valor=valor,
                                          obrigatorio=obrigatorio)
        self.tamanho = tamanho
        self.numerico = numerico

        if valor:
            self.valor = valor

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, val):
        val = self._formata_valor(val)
        self._valor = val

    def _formata_valor(self, valor):
        if not isinstance(valor, basestring):
            raise sigep_exceptions.ErroTipoIncorreto(self.nome,
                                                     type(valor),
                                                     basestring)
        return valor.rstrip()

    def validar(self, valor):

        if self.tamanho != 0 and len(valor) != self.tamanho:
            raise sigep_exceptions.ErroCampoTamanhoIncorreto(self.nome,
                                                             self.tamanho,
                                                             len(valor))

        if self.numerico and not valor.isdigit():
            raise sigep_exceptions.ErroCampoNaoNumerico(self.nome)

        return super(CampoString, self).validar(valor)


class CampoUnicode(CampoString):

    def get_xml(self):
        valor = self.valor if self.valor is not None else ''
        return u'<{}><![CDATA[{}]]></{}>'.format(self.nome, valor, self.nome)


class CampoCEP(CampoString):

    def __init__(self, nome, valor=None, obrigatorio=False):
        super(CampoCEP, self).__init__(nome, valor=valor,
                                       obrigatorio=obrigatorio,
                                       tamanho=8, numerico=True)

    def _formata_valor(self, valor):
        valor = super(CampoCEP, self)._formata_valor(valor)
        valor = valor.replace('-', '')
        valor = valor.replace('.', '')
        return valor


class CampoCNPJ(CampoString):

    def __init__(self, nome, valor=None, obrigatorio=False):
        super(CampoCNPJ, self).__init__(nome, valor=valor,
                                        obrigatorio=obrigatorio,
                                        tamanho=14, numerico=True)

    def _formata_valor(self, valor):
        valor = super(CampoCNPJ, self)._formata_valor(valor)
        valor = valor.replace('-', '')
        valor = valor.replace('.', '')
        valor = valor.replace('/', '')
        return valor


class CampoBooleano(CampoBase):

    def __init__(self, nome, valor=None, obrigatorio=False):
        super(CampoBooleano, self).__init__(nome, valor=valor,
                                            obrigatorio=obrigatorio)

    def validar(self, valor):

        if not isinstance(valor, bool):
            raise sigep_exceptions.ErroTipoIncorreto(self.nome,
                                                     type(valor),
                                                     bool)
        return super(CampoBooleano, self).validar(valor)


class CampoInteiro(CampoBase):

    def __init__(self, nome, valor=None, obrigatorio=False):
        super(CampoInteiro, self).__init__(nome, valor=valor,
                                           obrigatorio=obrigatorio)

    def validar(self, valor):
        if not isinstance(valor, int):
            raise sigep_exceptions.ErroTipoIncorreto(self.nome,
                                                     type(valor),
                                                     int)
        return super(CampoInteiro, self).validar(valor)


class CampoDecimal(CampoBase):

    def __init__(self, nome, valor=None, obrigatorio=False):
        super(CampoDecimal, self).__init__(nome, valor=valor,
                                           obrigatorio=obrigatorio)

    def validar(self, valor):
        if not isinstance(valor, float):
            raise sigep_exceptions.ErroTipoIncorreto(self.nome,
                                                     type(valor),
                                                     float)
        return super(CampoDecimal, self).validar(valor)
