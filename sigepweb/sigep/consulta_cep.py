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

from sigepweb.base import RequestBaseSIGEP
from sigepweb.base import ResponseBase
from sigepweb.campos import CampoCEP


class RequestConsultaCEP(RequestBaseSIGEP):

    def __init__(self, cep):
        super(RequestConsultaCEP, self).__init__(ResponseBuscaCEP)
        self.cep = CampoCEP('cep', valor=cep, obrigatorio=True)

    def get_data(self):
        xml = RequestBaseSIGEP.HEADER
        xml += '<cli:consultaCEP>'
        xml += self.cep.get_xml()
        xml += '</cli:consultaCEP>'
        xml += RequestBaseSIGEP.FOOTER
        return xml


class ResponseBuscaCEP(ResponseBase):

    def __init__(self):
        super(ResponseBuscaCEP, self).__init__()

    def _parse_xml(self, xml):

        end = Et.fromstring(xml).find('.//return')
        self.resposta = {
            'logradouro': end.findtext('end'),
            'bairro': end.findtext('bairro'),
            'cidade': end.findtext('cidade'),
            'uf': end.findtext('uf'),
            'complemento': end.findtext('complemento'),
            'complemento_2': end.findtext('complemento2')
        }
