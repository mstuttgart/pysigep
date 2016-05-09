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
from sigepweb.sigep.disponibilidade_servico import \
    RequestDisponibilidadeServico
from sigepweb.sigep.disponibilidade_servico import \
    ResponseDisponibilidadeServico


class TestRequestDisponibilidadeServico(TestCase):

    def test_get_data(self):
        LOGIN = 'sigep'
        SENHA = 'n5f9t8'
        COD_ADMIN = '08082650'

        res_disp = RequestDisponibilidadeServico(COD_ADMIN, '40436',
                                                 '99200-000', '99200-000',
                                                 LOGIN, SENHA)

        xml = RequestBaseSIGEPAuthentication.HEADER
        xml += '<cli:verificaDisponibilidadeServico>'
        xml += '<codAdministrativo>%s</codAdministrativo>' % \
               res_disp.cod_administrativo.valor
        xml += '<numeroServico>%s</numeroServico>' % \
               res_disp.numero_servico.valor
        xml += '<cepOrigem>%s</cepOrigem>' % res_disp.cep_origem.valor
        xml += '<cepDestino>%s</cepDestino>' % res_disp.cep_destino.valor
        xml += super(RequestDisponibilidadeServico, res_disp).get_data()
        xml += '</cli:verificaDisponibilidadeServico>'
        xml += RequestBaseSIGEPAuthentication.FOOTER

        self.assertEqual(xml, res_disp.get_data())


class TestResponseDisponibilidadeServico(TestCase):

    def test_parse_xml(self):

        xml = '''<S:Envelope
        xmlns:S=\"http://schemas.xmlsoap.org/soap/envelope/\">
<S:Body>
<ns2:verificaDisponibilidadeServicoResponse
xmlns:ns2=\"http://cliente.bean.master.sigep.bsb.correios.com.br/\">
<return>true</return>
</ns2:verificaDisponibilidadeServicoResponse>
</S:Body>
</S:Envelope>'''

        resp_disp = ResponseDisponibilidadeServico()
        resp_disp._parse_xml(xml)

        self.assertEqual(resp_disp.resposta['disponibilidade'], True)

        xml = '''<S:Envelope
        xmlns:S=\"http://schemas.xmlsoap.org/soap/envelope/\">
<S:Body>
<ns2:verificaDisponibilidadeServicoResponse
xmlns:ns2=\"http://cliente.bean.master.sigep.bsb.correios.com.br/\">
<return>false</return>
</ns2:verificaDisponibilidadeServicoResponse>
</S:Body>
</S:Envelope>'''

        resp_disp._parse_xml(xml)
        self.assertEqual(resp_disp.resposta['disponibilidade'], False)
