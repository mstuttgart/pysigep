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
from pysigep.sigep import verifica_disponibilidade_servico
from pysigep.utils import PRODUCAO, HOMOLOGACAO
from requests.models import Response

resposta_xml = '''\
<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
    <S:Body>
        <ns2:verificaDisponibilidadeServicoResponse
        xmlns:ns2="http://cliente.bean.master.sigep.bsb.correios.com.br/">
            <return>{retorno}</return>
        </ns2:verificaDisponibilidadeServicoResponse>
    </S:Body>
</S:Envelope>'''


def fake_requests_post(retorno):
    def wrap(url, data, headers, verify):
        response = Response()
        response.status_code = 200
        response._content = resposta_xml.format(retorno=retorno)
        response._content_consumed = True
        return response
    return wrap


class TestVerificaDisponibilidadeServico(TestCase):
    def setUp(self):
        self.kwargs = {
            'codAdministrativo': '08082650',
            'numeroServico': '40215',
            'cepOrigem': '70002900',
            'cepDestino': '81350120',
            'usuario': 'sigep',
            'senha': 'n5f9t8',
        }

    def test_verifica_disponibilidade_servico_demanda_ambiente(self):
        with self.assertRaises(AmbienteObrigatorioError):
            verifica_disponibilidade_servico(**self.kwargs)

    def test_verifica_disponibilidade_servico_resposta_positiva(self):
        with mock.patch('pysigep.requests.post',
                        new=fake_requests_post(retorno='true')):
            self.kwargs['ambiente'] = PRODUCAO
            retorno = verifica_disponibilidade_servico(**self.kwargs)
            assert retorno

    def test_verifica_disponibilidade_servico_resposta_negativa(self):
        with mock.patch('pysigep.requests.post',
                        new=fake_requests_post(retorno='false')):
            self.kwargs['ambiente'] = PRODUCAO
            retorno = verifica_disponibilidade_servico(**self.kwargs)
            assert not retorno

    def test_verifica_disponibilidade_servico(self):
        self.kwargs['ambiente'] = HOMOLOGACAO
        retorno = verifica_disponibilidade_servico(**self.kwargs)
        self.assertNotIn('mensagem_erro', retorno)
