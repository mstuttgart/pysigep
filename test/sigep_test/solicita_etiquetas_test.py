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
from sigepweb.sigep.solicita_etiquetas import RequestSolicitaEtiquetaSIGEP
from sigepweb.sigep.solicita_etiquetas import ResponseSolicitaEtiqueta


class TestRequestSolicitaEtiqueta(TestCase):

    def test_get_data(self):

        login = 'sigep'
        senha = 'n5f9t8'
        cnpj = '12345678000196'
        id_servico = 104625

        req = RequestSolicitaEtiquetaSIGEP(cnpj, id_servico, 1, login, senha)

        xml = RequestBaseSIGEPAuthentication.HEADER
        xml += '<cli:solicitaEtiquetas>'
        xml += '<tipoDestinatario>%s</tipoDestinatario>' % \
               req.tipo_destinatario.valor
        xml += '<identificador>%s</identificador>' % req.cnpj.valor
        xml += '<idServico>%d</idServico>' % req.id_servico.valor
        xml += '<qtdEtiquetas>%d</qtdEtiquetas>' % req.qtd_etiquetas.valor
        xml += '<usuario>%s</usuario>' % login
        xml += '<senha>%s</senha>' % senha
        xml += '</<cli:solicitaEtiquetas>'
        xml += RequestBaseSIGEPAuthentication.FOOTER

        self.assertEqual(req.get_data(), xml)


class TestResponseSolicitaEtiqueta(TestCase):

    def test__parse_xml(self):
        xml = '''<S:Envelope xmlns:S=\"http://schemas.xmlsoap.org/soap/envelope/\">
<S:Body>
<ns2:solicitaEtiquetasResponse
xmlns:ns2=\"http://cliente.bean.master.sigep.bsb.correios.com.br/\">
<return>DL76023726 BR,DL76023727 BR</return>
</ns2:solicitaEtiquetasResponse>
</S:Body>
</S:Envelope>'''

        resp = ResponseSolicitaEtiqueta()
        resp._parse_xml(xml)
        self.assertEqual(resp.resposta['lista_etiquetas'][0], 'DL76023726 BR')
        self.assertEqual(resp.resposta['lista_etiquetas'][1], 'DL76023727 BR')
