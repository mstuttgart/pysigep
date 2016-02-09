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


class SigepBaseException(Exception):
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return repr(self.message)


class ErroSemConexaoComInternet(SigepBaseException):
    def __init__(self, msg, *args):
        self.message = u'Falha na conexão com a Internet'

    def __str__(self):
        return repr(self.message)


class ErroConexaoComServidor(SigepBaseException):
    def __str__(self):
        return repr(self.message)


class ErroConexaoTimeOut(SigepBaseException):
    def __str__(self):
        return repr(self.message)


class ErroRequisicao(SigepBaseException):
    def __str__(self):
        return repr(self.message)


class ErroSSL(SigepBaseException):
    def __str__(self):
        return repr(self.message)


class ErroInvalidSchema(SigepBaseException):
    def __str__(self):
        return repr(self.message)


class ErroURLInvalida(SigepBaseException):
    def __str__(self):
        return repr(self.message)


class ErroTamanhoParamentroIncorreto(SigepBaseException):
    def __str__(self):
        return repr(self.message)


class ErroTipoIncorreto(SigepBaseException):
    def __str__(self):
        return repr(self.message)


class ErroValidacaoXML(SigepBaseException):
    def __str__(self):
        return repr(self.message)


class ErroCampoObrigatorio(SigepBaseException):
    def __init__(self, nome_campo):
        self.message = 'Campo ' + nome_campo + u'é de envio obrigatorio, ' \
                                               u'mas não foi preenchido!'

    def __str__(self):
        return repr(self.message)


class ErroCampoTamanhoIncorreto(SigepBaseException):
    def __init__(self, nome_campo, tamanho_esperado, tamanho):
        self.message = 'Campo ' + nome_campo + u'possui tamanho incorreto.' \
                                               u'Esperado é ' + \
                       str(tamanho_esperado) + u'mas o encontrado foi ' + \
                       str(tamanho)

    def __str__(self):
        return repr(self.message)
