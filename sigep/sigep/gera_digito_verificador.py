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
from sigep.campos import CampoInteiro


class RequestGeraDigitoVerificador(RequestBaseAutentic):

    def __init__(self, etiquetas, usuario, senha):
        super(RequestGeraDigitoVerificador, self).__init__(
            ResponseGeraDigitoVerificador, usuario, senha)

        self._etiquetas = []

        for etq in etiquetas.valor.split(','):
            cmp_etq = CampoString('etiquetas', obrigatorio=True)
            cmp_etq.valor = etq
            self._etiquetas.append(cmp_etq)

    @property
    def etiquetas(self):
        return self._etiquetas

    def get_xml(self):

        xml = self.header
        xml += '<cli:geraDigitoVerificadorEtiquetas>'

        for etq in self.etiquetas:
            xml += etq.get_xml()

        xml += super(RequestGeraDigitoVerificador, self).get_xml()
        xml += '<cli:geraDigitoVerificadorEtiquetas>'
        xml += self.footer
        return xml


class ResponseGeraDigitoVerificador(ResponseBase):

    def __init__(self):
        super(ResponseGeraDigitoVerificador, self).__init__()
        self.digito_verificador = []

    def _parse_xml(self, xml):
        for end in Et.fromstring(xml).findall('.//return'):
            campo_int = CampoInteiro('digito_verificador')
            campo_int.valor = end.text()
            self.digito_verificador.append(campo_int)
