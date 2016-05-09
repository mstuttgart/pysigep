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

import xml.etree.cElementTree as Et

from pysigep.base import RequestBaseSIGEPAuthentication
from pysigep.base import ResponseBase
from pysigep.campos import CampoString


class RequestStatusCartaoPostagem(RequestBaseSIGEPAuthentication):

    def __init__(self, num_cartao_postagem, usuario, senha):
        super(RequestStatusCartaoPostagem, self).__init__(
            ResponseStatusCartaoPostagem, usuario, senha)

        self.numero_cartao_postagem = CampoString('numeroCartaoPostagem',
                                                  obrigatorio=True,
                                                  valor=num_cartao_postagem,
                                                  tamanho=10,
                                                  numerico=True)

    def get_data(self):
        xml = RequestBaseSIGEPAuthentication.HEADER
        xml += '<cli:getStatusCartaoPostagem>'
        xml += self.numero_cartao_postagem.get_xml()
        xml += super(RequestStatusCartaoPostagem, self).get_data()
        xml += '</cli:getStatusCartaoPostagem>'
        xml += RequestBaseSIGEPAuthentication.FOOTER
        return xml


class ResponseStatusCartaoPostagem(ResponseBase):

    def __init__(self):
        super(ResponseStatusCartaoPostagem, self).__init__()

    def _parse_xml(self, xml):
        for end in Et.fromstring(xml).findall('.//return'):
            self.resposta = {
                'status': end.text,
            }
