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

from sigepweb.base import RequestBaseFrete
from sigepweb.base import ResponseBase
from sigepweb.campos import CampoCEP
from sigepweb.campos import CampoString
from sigepweb.campos import CampoInteiro
from sigepweb.campos import CampoDecimal


class RequestCalcPrecoPrazo(RequestBaseFrete):

    FORMATO_CAIXA_PACOTE = 1
    FORMATO_ROLO_PRISMA = 2
    FORMATO_ENVELOPE = 3

    def __init__(self, nCdServico, sCepOrigem, sCepDestino, nVlPeso,
                 nCdFormato, nVlComprimento, nVlAltura, nVlLargura,
                 nVlDiametro, sCdMaoPropria, nVlValorDeclarado,
                 sCdAvisoRecebimento):

        super(RequestCalcPrecoPrazo, self).__init__(ResponseCalcPrecoPrazo)

        self.ncdempresa = CampoString('nCdEmpresa', valor='')
        self.sdssenha = CampoString('sDsSenha', valor='')
        self.nCdServico = CampoString('nCdServico', valor=nCdServico,
                                      obrigatorio=True)
        self.sCepOrigem = CampoCEP('sCepOrigem', valor=sCepOrigem,
                                   obrigatorio=True)
        self.sCepDestino = CampoCEP('sCepDestino', valor=sCepDestino,
                                    obrigatorio=True)
        self.nVlPeso = CampoString('nVlPeso', valor=nVlPeso, obrigatorio=True)
        self.nCdFormato = CampoInteiro('nCdFormato', valor=nCdFormato,
                                       obrigatorio=True)
        self.nVlComprimento = CampoDecimal('nVlComprimento',
                                           valor=nVlComprimento,
                                           obrigatorio=True)
        self.nVlAltura = CampoDecimal('nVlAltura', valor=nVlAltura,
                                      obrigatorio=True)
        self.nVlLargura = CampoDecimal('nVlLargura', valor=nVlLargura,
                                       obrigatorio=True)
        self.nVlDiametro = CampoDecimal('nVlDiametro', valor=nVlDiametro,
                                        obrigatorio=True)
        self.sCdMaoPropria = CampoString('sCdMaoPropria', obrigatorio=True,
                                         valor='S' if sCdMaoPropria else 'N')
        self.nVlValorDeclarado = CampoDecimal('nVlValorDeclarado',
                                              valor=nVlValorDeclarado)
        self.sCdAvisoRecebimento = CampoString('sCdAvisoRecebimento',
                                               valor='S' if sCdAvisoRecebimento
                                               else 'N')

    def get_data(self):

        xml = RequestBaseFrete.HEADER
        xml += '<CalcPrecoPrazo xmlns=\"http://tempuri.org/\">'
        xml += self.ncdempresa.get_xml()
        xml += self.sdssenha.get_xml()
        xml += self.nCdServico.get_xml()
        xml += self.sCepOrigem.get_xml()
        xml += self.sCepDestino.get_xml()
        xml += self.nVlPeso.get_xml()
        xml += self.nCdFormato.get_xml()
        xml += self.nVlComprimento.get_xml()
        xml += self.nVlAltura.get_xml()
        xml += self.nVlLargura.get_xml()
        xml += self.nVlDiametro.get_xml()
        xml += self.sCdMaoPropria.get_xml()
        xml += self.nVlValorDeclarado.get_xml()
        xml += self.sCdAvisoRecebimento.get_xml()
        xml += '</CalcPrecoPrazo>'
        xml += RequestBaseFrete.FOOTER

        return xml


class ResponseCalcPrecoPrazo(ResponseBase):

    def __init__(self):
        super(ResponseCalcPrecoPrazo, self).__init__()
        self.resposta = {}

    def _parse_xml(self, xml):

        str_find = '{http://schemas.xmlsoap.org/soap/envelope/}Body/' \
                   '{http://tempuri.org/}CalcPrecoPrazoResponse/' \
                   '{http://tempuri.org/}CalcPrecoPrazoResult/'\
                   '{http://tempuri.org/}Servicos/' \
                   '{http://tempuri.org/}cServico'

        for end in Et.fromstring(xml).findall(str_find):

            self.resposta[end.findtext('{http://tempuri.org/}Codigo')] = {
                'Valor': self._format_float_tag(end, 'Valor'),
                'PrazoEntrega': int(end.findtext(
                    '{http://tempuri.org/}PrazoEntrega')),
                'ValorMaoPropria':
                    self._format_float_tag(end, 'ValorMaoPropria'),
                'ValorAvisoRecebimento':
                    self._format_float_tag(end, 'ValorAvisoRecebimento'),
                'ValorValorDeclarado':
                    self._format_float_tag(end, 'ValorValorDeclarado'),
                'EntregaDomiciliar': end.findtext(
                    '{http://tempuri.org/}EntregaDomiciliar').rstrip(),
                'EntregaSabado': end.findtext(
                    '{http://tempuri.org/}EntregaSabado').rstrip(),
                'Erro': end.findtext('{http://tempuri.org/}Erro').rstrip(),
                'MsgErro': end.findtext(
                    '{http://tempuri.org/}MsgErro').rstrip(),
                'ValorSemAdicionais':
                    self._format_float_tag(end, 'ValorSemAdicionais'),
                'obsFim': end.findtext('{http://tempuri.org/}obsFim').rstrip(),
            }

    @staticmethod
    def _format_float_tag(elem, tag):
        return float(elem.findtext(
            '{http://tempuri.org/}' + tag).replace(',', '.'))
