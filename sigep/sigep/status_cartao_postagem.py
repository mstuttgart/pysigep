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

import xml.etree.ElementTree as Et

from sigep.base import RequestBaseAutentic
from sigep.base import ResponseBase
from sigep.campos import CampoString


class RequestStatusCartaoPostagem(RequestBaseAutentic):

    def __init__(self, num_cartao_postagem, usuario, senha):
        super(RequestStatusCartaoPostagem, self).__init__(
            ResponseStatusCartaoPostagem, usuario, senha)

        self._numero_cartao_postagem = CampoString('numeroCartaoPostagem',
                                                   obrigatorio=True,
                                                   tamanho=10,
                                                   numerico=True)

        self._numero_cartao_postagem.valor = num_cartao_postagem

    @property
    def numero_cartao_postagem(self):
        return self._numero_cartao_postagem

    def get_xml(self):
        xml = self.header
        xml += '<cli:getStatusCartaoPostagem>'
        xml += self.numero_cartao_postagem.get_xml()
        xml += super(RequestStatusCartaoPostagem, self).get_xml()
        xml += '</cli:getStatusCartaoPostagem>'
        xml += self.footer
        return xml


class ResponseStatusCartaoPostagem(ResponseBase):

    def __init__(self):
        super(ResponseStatusCartaoPostagem, self).__init__()
        self.status = CampoString('status', obrigatorio=True)

    def _parse_xml(self, xml):
        end = Et.fromstring(xml).find('.//return')
        self.status.valor = end.text
