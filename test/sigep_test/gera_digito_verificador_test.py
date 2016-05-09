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

from unittest import TestCase

from sigepweb.base import RequestBaseSIGEPAuthentication
from sigepweb.sigep.gera_digito_verificador import \
    RequestGeraDigitoVerificadorSIGEP
from sigepweb.sigep.gera_digito_verificador import \
    ResponseGeraDigitoVerificador


class TestRequestGeraDigitoVerificador(TestCase):

    def test__init__(self):
        etiquetas = 'DL76023727 BR,DL76023728 BR'
        req = RequestGeraDigitoVerificadorSIGEP(etiquetas, 'sigep', 'n5f9t8')

        self.assertEqual(len(req.etiquetas), 2)
        self.assertEqual(req.etiquetas[0].valor, 'DL76023727 BR')
        self.assertEqual(req.etiquetas[1].valor, 'DL76023728 BR')

    def test_etiquetas(self):
        self.test__init__()

    def test_get_data(self):
        etiquetas = 'DL76023727 BR,DL76023728 BR'
        req = RequestGeraDigitoVerificadorSIGEP(etiquetas, 'sigep', 'n5f9t8')

        xml = RequestBaseSIGEPAuthentication.HEADER
        xml += '<cli:geraDigitoVerificadorEtiquetas>'
        xml += '<etiquetas>%s</etiquetas>' % 'DL76023727 BR'
        xml += '<etiquetas>%s</etiquetas>' % 'DL76023728 BR'
        xml += '<usuario>%s</usuario>' % 'sigep'
        xml += '<senha>%s</senha>' % 'n5f9t8'
        xml += '<cli:geraDigitoVerificadorEtiquetas>'
        xml += RequestBaseSIGEPAuthentication.FOOTER

        self.assertEqual(req.get_data(), xml)


class TestResponseGeraDigitoVerificador(TestCase):

    def test_parse_xml(self):
        resp = ResponseGeraDigitoVerificador()

        xml = '''<S:Envelope
        xmlns:S=\"http://schemas.xmlsoap.org/soap/envelope/\">
 <S:Body>
 <ns2:geraDigitoVerificadorEtiquetasResponse
xmlns:ns2=\"http://cliente.bean.master.sigep.bsb.correios.com.br/\">
 <return>6</return>
 <return>7</return>
 </ns2:geraDigitoVerificadorEtiquetasResponse>
 </S:Body>
</S:Envelope>'''

        resp._parse_xml(xml)

        self.assertEqual(len(resp.resposta['lista_digitos']), 2)
        self.assertEqual(resp.resposta['lista_digitos'][0], 6)
        self.assertEqual(resp.resposta['lista_digitos'][1], 7)
