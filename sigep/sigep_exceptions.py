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
        self.msg = u'Campo %s deve ser %s . Tipo encontrado: %s' % \
                   (nome_campo, str(tipo_correto), str(tipo))

    def __str__(self):
        return self.msg


class ErroCampoObrigatorio(SigepBaseException):

    def __init__(self, nome_campo):
        self.msg = u'Campo %s é de envio obrigatorio, mas não foi ' \
                   u'preenchido!' % nome_campo

    def __str__(self):
        return self.msg


class ErroCampoNaoNumerico(SigepBaseException):

    def __init__(self, nome_campo):
        self.msg = u'Campo %s não é constituído apenas por números!' % \
                   nome_campo

    def __str__(self):
        return self.msg


class ErroCampoTamanhoIncorreto(SigepBaseException):

    def __init__(self, nome_campo, tamanho_esperado, tamanho):
        self.msg = u'Campo %s possui tamanho incorreto. Esperado é %d mas o' \
                   u' encontrado foi %d.' % (nome_campo, tamanho_esperado,
                                             tamanho)

    def __str__(self):
        return self.msg


class ErroSemConexaoComInternet(SigepBaseException):

    def __init__(self, msg):
        self.msg = u'Falha na conexão com a Internet. %s' % msg

    def __str__(self):
        return self.msg


class ErroConexaoComServidor(SigepBaseException):

    def __init__(self, msg):
        self.msg = u'Erro de conexão com o servidor. %s' % msg

    def __str__(self):
        return self.msg


class ErroConexaoTimeOut(SigepBaseException):

    def __init__(self, msg):
        self.msg = u'Erro de timeout. %s' % msg

    def __str__(self):
        return self.msg


class ErroRequisicao(SigepBaseException):

    def __init__(self, msg):
        self.msg = u'Falha na requisição. %s' % msg

    def __str__(self):
        return self.msg


class ErroSSL(SigepBaseException):

    def __init__(self, msg):
        self.msg = u'Erro SSL. %s' % msg

    def __str__(self):
        return self.msg


class ErroValidacaoXML(SigepBaseException):

    def __init__(self, msg):
        self.msg = u'Erro durante validação do XML. %s' % msg

    def __str__(self):
        return self.msg
