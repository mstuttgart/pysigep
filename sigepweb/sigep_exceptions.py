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
    pass


class ErroTipoIncorreto(SigepBaseException):

    def __init__(self, nome_campo, tipo, tipo_correto):
        self.message = u'Campo %s deve ser %s . Tipo encontrado: %s' \
                       % (nome_campo, str(tipo_correto), str(tipo))

    def __str__(self):
        return self.message


class ErroCampoObrigatorio(SigepBaseException):

    def __init__(self, nome_campo):
        self.message = u'Campo %s é de envio obrigatorio, mas não foi ' \
                   u'preenchido!' % nome_campo

    def __str__(self):
        return self.message


class ErroCampoNaoNumerico(SigepBaseException):

    def __init__(self, nome_campo):
        self.message = u'Campo %s não é constituído apenas por números!' % \
                   nome_campo

    def __str__(self):
        return self.message


class ErroCampoTamanhoIncorreto(SigepBaseException):

    def __init__(self, nome_campo, tamanho_esperado, tamanho):
        self.message = u'Campo %s possui tamanho incorreto. Esperado é %d ' \
                       u'mas o encontrado foi %d.' % (nome_campo,
                                                      tamanho_esperado,
                                                      tamanho)

    def __str__(self):
        return self.message


class ErroSemConexaoComInternet(SigepBaseException):

    def __init__(self, message):
        self.message = u'Falha na conexão com a Internet. %s' % message

    def __str__(self):
        return self.message


class ErroConexaoComServidor(SigepBaseException):

    def __init__(self, message):
        self.message = u'Erro de conexão com o servidor. %s' % message

    def __str__(self):
        return self.message


class ErroConexaoTimeOut(SigepBaseException):

    def __init__(self, message):
        self.message = u'Erro de timeout. %s' % message

    def __str__(self):
        return self.message


class ErroRequisicao(SigepBaseException):

    def __init__(self, message):
        self.message = u'Falha na requisição. %s' % message

    def __str__(self):
        return self.message


class ErroSSL(SigepBaseException):

    def __init__(self, message):
        self.message = u'Erro SSL. %s' % message

    def __str__(self):
        return self.message


class ErroValidacaoXML(SigepBaseException):

    def __init__(self, message):
        self.message = u'Erro durante validação do XML. %s' % message

    def __str__(self):
        return self.message
