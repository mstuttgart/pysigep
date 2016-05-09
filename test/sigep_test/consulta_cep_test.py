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
from sigepweb.base import RequestBaseSIGEP
from sigepweb.sigep.consulta_cep import RequestConsultaCEP
from sigepweb.sigep.consulta_cep import ResponseBuscaCEP


class TestRequestConsultaCEP(TestCase):

    def test_get_data(self):
        req_cep = RequestConsultaCEP('37.503-005')

        xml = RequestBaseSIGEP.HEADER
        xml += '<cli:consultaCEP>'
        xml += '<cep>%s</cep>' % '37503005'
        xml += '</cli:consultaCEP>'
        xml += RequestBaseSIGEP.FOOTER

        self.assertEqual(xml, req_cep.get_data())


class TestResponseBuscaCEP(TestCase):

    def test_parse_xml(self):

        xml = '''<S:Envelope
        xmlns:S=\"http://schemas.xmlsoap.org/soap/envelope/\">
        <S:Body>
        <ns2:consultaCEPResponse
        xmlns:ns2=\"http://cliente.bean.master.sigep.bsb.correios.com.br/\">
            <return>
                <bairro>Asa Norte</bairro>
                <cep>70002900</cep>
                <cidade>Brasília</cidade>
                <complemento/>
                <complemento2/>
                <end>SBN Quadra 1 Bloco A</end>
                <id>0</id>
                <uf>DF</uf>
            </return>
        </ns2:consultaCEPResponse>
        </S:Body>
        </S:Envelope>'''.replace('\n', '')

        resp_cep = ResponseBuscaCEP()
        resp_cep._parse_xml(xml)

        self.assertEqual(resp_cep.resposta['logradouro'], u'SBN Quadra 1 '
                                                          u'Bloco A')
        self.assertEqual(resp_cep.resposta['bairro'], u'Asa Norte')
        self.assertEqual(resp_cep.resposta['cidade'], u'Brasília')
        self.assertEqual(resp_cep.resposta['uf'], u'DF')
        self.assertEqual(resp_cep.resposta['complemento'], u'')
        self.assertEqual(resp_cep.resposta['complemento_2'], u'')
