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
from sigepweb.base import RequestBaseFrete
from sigepweb.frete.consulta_frete import RequestCalcPrecoPrazo
from sigepweb.frete.consulta_frete import ResponseCalcPrecoPrazo


class TestRequestCalcPrecoPrazo(TestCase):

    def test_get_data(self):
        req = RequestCalcPrecoPrazo('40436,40215', '99200000', '37503130', '2',
                                    RequestCalcPrecoPrazo.FORMATO_CAIXA_PACOTE,
                                    100.0, 100.0, 100.0, 0.0,
                                    False, 0.00, False)

        xml = RequestBaseFrete.HEADER
        xml += '<CalcPrecoPrazo xmlns=\"http://tempuri.org/\">'
        xml += '<nCdEmpresa></nCdEmpresa>'
        xml += '<sDsSenha></sDsSenha>'
        xml += '<nCdServico>40436,40215</nCdServico>'
        xml += '<sCepOrigem>99200000</sCepOrigem>'
        xml += '<sCepDestino>37503130</sCepDestino>'
        xml += '<nVlPeso>2</nVlPeso>'
        xml += '<nCdFormato>1</nCdFormato>'
        xml += '<nVlComprimento>100.0</nVlComprimento>'
        xml += '<nVlAltura>100.0</nVlAltura>'
        xml += '<nVlLargura>100.0</nVlLargura>'
        xml += '<nVlDiametro>0.0</nVlDiametro>'
        xml += '<sCdMaoPropria>N</sCdMaoPropria>'
        xml += '<nVlValorDeclarado>0.0</nVlValorDeclarado>'
        xml += '<sCdAvisoRecebimento>N</sCdAvisoRecebimento>'
        xml += '</CalcPrecoPrazo>'
        xml += RequestBaseFrete.FOOTER

        self.assertEqual(xml, req.get_data())


class TestResponseCalcPrecoPrazo(TestCase):

    def test_parse_xml(self):
        resp = ResponseCalcPrecoPrazo()
        self.maxDiff = None

        xml = '''<?xml version=\"1.0\" encoding=\"utf-8\"?>
<soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\"
               xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"
               xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
    <soap:Body>
        <CalcPrecoPrazoResponse xmlns=\"http://tempuri.org/\">
            <CalcPrecoPrazoResult>
                <Servicos>
                    <cServico>
                        <Codigo>40436</Codigo>
                        <Valor>0,00</Valor>
                        <PrazoEntrega>0</PrazoEntrega>
                        <ValorMaoPropria>0,00</ValorMaoPropria>
                        <ValorAvisoRecebimento>0,00</ValorAvisoRecebimento>
                        <ValorValorDeclarado>0,00</ValorValorDeclarado>
                        <EntregaDomiciliar/>
                        <EntregaSabado/>
                        <Erro>-34</Erro>
                        <MsgErro>Codigo Administrativo ou Senha invalidos.
                        </MsgErro>
                        <ValorSemAdicionais>0,00</ValorSemAdicionais>
                        <obsFim/>
                    </cServico>
                    <cServico>
                        <Codigo>40215</Codigo>
                        <Valor>0,00</Valor>
                        <PrazoEntrega>0</PrazoEntrega>
                        <ValorMaoPropria>0,00</ValorMaoPropria>
                        <ValorAvisoRecebimento>0,00</ValorAvisoRecebimento>
                        <ValorValorDeclarado>0,00</ValorValorDeclarado>
                        <EntregaDomiciliar/>
                        <EntregaSabado/>
                        <Erro>-23</Erro>
                        <MsgErro>%s
                        </MsgErro>
                        <ValorSemAdicionais>0,00</ValorSemAdicionais>
                        <obsFim/>
                    </cServico>
                </Servicos>
            </CalcPrecoPrazoResult>
        </CalcPrecoPrazoResponse>
    </soap:Body>
</soap:Envelope>''' % 'A soma resultante do comprimento + largura + ' \
                      'altura nao deve superar a 200 cm.'
        saida = {
            '40436': {
                'Valor': 0.0,
                'PrazoEntrega': 0,
                'ValorMaoPropria': 0.0,
                'ValorAvisoRecebimento': 0.0,
                'ValorValorDeclarado': 0.0,
                'EntregaDomiciliar': '',
                'EntregaSabado': '',
                'Erro': '-34',
                'MsgErro': 'Codigo Administrativo ou Senha invalidos.',
                'ValorSemAdicionais': 0.00,
                'obsFim': '',
            },
            '40215': {
                'Valor': 0.0,
                'PrazoEntrega': 0,
                'ValorMaoPropria': 0.0,
                'ValorAvisoRecebimento': 0.0,
                'ValorValorDeclarado': 0.0,
                'EntregaDomiciliar': '',
                'EntregaSabado': '',
                'Erro': '-23',
                'MsgErro': 'A soma resultante do comprimento + largura + '
                           'altura nao deve superar a 200 cm.',
                'ValorSemAdicionais': 0.0,
                'obsFim': '',
            }
        }

        resp._parse_xml(xml)
        self.assertDictEqual(saida, resp.resposta)
