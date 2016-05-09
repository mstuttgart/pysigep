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

from sigepweb.base import RequestBaseSIGEPAuthentication
from sigepweb.base import ResponseBase
from sigepweb.campos import CampoString


class RequestGeraDigitoVerificadorSIGEP(RequestBaseSIGEPAuthentication):

    def __init__(self, etiquetas, usuario, senha):
        super(RequestGeraDigitoVerificadorSIGEP, self).__init__(
            ResponseGeraDigitoVerificador, usuario, senha)

        self.etiquetas = [
            CampoString('etiquetas', valor=etq, obrigatorio=True)
            for etq in etiquetas.split(',')]

    def get_data(self):
        xml = RequestBaseSIGEPAuthentication.HEADER
        xml += '<cli:geraDigitoVerificadorEtiquetas>'
        for etq in self.etiquetas:
            xml += etq.get_xml()
        xml += super(RequestGeraDigitoVerificadorSIGEP, self).get_data()
        xml += '<cli:geraDigitoVerificadorEtiquetas>'
        xml += RequestBaseSIGEPAuthentication.FOOTER
        return xml


class ResponseGeraDigitoVerificador(ResponseBase):

    def __init__(self):
        super(ResponseGeraDigitoVerificador, self).__init__()

    def _parse_xml(self, xml):
        self.resposta = {
            'lista_digitos': [int(end.text) for end in Et.fromstring(
                xml).findall('.//return')]
        }
