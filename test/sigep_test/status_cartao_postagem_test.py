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
from sigepweb.sigep.status_cartao_postagem import RequestStatusCartaoPostagem
from sigepweb.sigep.status_cartao_postagem import ResponseStatusCartaoPostagem


class TestRequestStatusCartaoPostagem(TestCase):

    def test_get_data(self):
        login = 'sigep'
        senha = 'n5f9t8'
        cartao_postagem = '0057018901'

        req_status = RequestStatusCartaoPostagem(cartao_postagem, login,
                                                 senha)

        xml = RequestBaseSIGEPAuthentication.HEADER
        xml += '<cli:getStatusCartaoPostagem>'
        xml += '<numeroCartaoPostagem>%s</numeroCartaoPostagem>' % \
               cartao_postagem
        xml += '<usuario>%s</usuario>' % login
        xml += '<senha>%s</senha>' % senha
        xml += '</cli:getStatusCartaoPostagem>'
        xml += RequestBaseSIGEPAuthentication.FOOTER

        self.assertEqual(xml, req_status.get_data())


class TestResponseStatusCartaoPostagem(TestCase):

    def test_parse_xml(self):
        xml = '''<S:Envelope
        xmlns:S=\"http://schemas.xmlsoap.org/soap/envelope/\">
<S:Body>
<ns2:getStatusCartaoPostagemResponse
xmlns:ns2=\"http://cliente.bean.master.sigep.bsb.correios.com.br/\">
<return>Normal</return>
</ns2:getStatusCartaoPostagemResponse>
</S:Body>
</S:Envelope>
'''
        resp_status = ResponseStatusCartaoPostagem()
        resp_status._parse_xml(xml)

        self.assertEqual(resp_status.resposta['status'], 'Normal')
