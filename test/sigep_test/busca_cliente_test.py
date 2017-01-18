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

import mock
from pysigep.exceptions import AmbienteObrigatorioError
from pysigep.sigep import busca_cliente
from pysigep.utils import PRODUCAO, HOMOLOGACAO
from requests.models import Response

resposta_xml = '''\
<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
<S:Body>
    <ns2:buscaClienteResponse xmlns:ns2="http://cliente.bean.master.sigep.bsb.correios.com.br/">
        <return>
            <cnpj>{cnpj}</cnpj>
            <contratos>
                <cartoesPostagem>
                    <codigoAdministrativo>{codigoAdministrativo}</codigoAdministrativo>
                    <numero>{numero}</numero>
                    <servicos>
                        <codigo>{codigo_servico}</codigo>
                        <descricao>{descricao_servico}</descricao>
                        <id>{id_servico}</id>
                    </servicos>
                </cartoesPostagem>
                <codigoDiretoria>{codigoDiretoria}</codigoDiretoria>
            </contratos>
        </return>
    </ns2:buscaClienteResponse>
</S:Body>
</S:Envelope>'''


def fake_post(mock_data):
    def wrap(url, data, headers, verify):
        response = Response()
        response.status_code = 200
        response._content = resposta_xml.format(**mock_data)
        response._content_consumed = True
        return response
    return wrap


class TestBuscaCliente(TestCase):
    def setUp(self):
        self.kwargs = {
            'idContrato': '0000000000',
            'idCartaoPostagem': '0000000000',
            'usuario': 'sigep',
            'senha': 'n5f9t8',
        }

    def test_busca_cliente_demanda_ambiente(self):
        with self.assertRaises(AmbienteObrigatorioError):
            busca_cliente(**self.kwargs)

    def test_busca_cliente(self):
        mock_data = {
            'cnpj': '11410937000151',
            'codigoAdministrativo': '121212',
            'numero': '343434',
            'codigo_servico': '565656',
            'descricao_servico': 'SEDEX - CONTRATO',
            'id_servico': '787878',
            'codigoDiretoria': '36',
        }
        with mock.patch('pysigep.requests.post', new=fake_post(mock_data)):
            self.kwargs['ambiente'] = PRODUCAO
            retorno = busca_cliente(**self.kwargs)
            assert retorno.cnpj == 11410937000151
            assert len(retorno.contratos) == 1

            contrato = retorno.contratos[0]
            assert contrato.codigoDiretoria == 36
            assert len(contrato.cartoesPostagem) == 1

            cartao = contrato.cartoesPostagem[0]
            assert cartao.codigoAdministrativo == 121212
            assert cartao.numero == 343434
            assert len(cartao.servicos) == 1

            servico = cartao.servicos[0]
            assert servico.codigo == 565656
            assert servico.descricao == 'SEDEX - CONTRATO'
            assert servico.id == 787878
