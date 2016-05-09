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
from pysigep.sigep_exceptions import ErroValidacaoXML
from pysigep.sigep_exceptions import ErroConexaoComServidor
from pysigep.sigep_exceptions import ErroConexaoTimeOut
from pysigep.sigep_exceptions import ErroRequisicao
from pysigep.sigep.consulta_cep import RequestConsultaCEP
from pysigep.sigep.consulta_cep import ResponseBuscaCEP
from pysigep.webservices.webservice_sigep import WebserviceSIGEP


class TestWebserviceSIGEP(TestCase):

    def test__init__(self):
        wb = WebserviceSIGEP(WebserviceSIGEP.AMBIENTE_HOMOLOGACAO)
        self.assertEqual(wb.ambiente, WebserviceSIGEP.AMBIENTE_HOMOLOGACAO)

        wb = WebserviceSIGEP(WebserviceSIGEP.AMBIENTE_PRODUCAO)
        self.assertEqual(wb.ambiente, WebserviceSIGEP.AMBIENTE_PRODUCAO)

        wb = WebserviceSIGEP('HOMOLOG')
        self.assertEqual(wb.ambiente, WebserviceSIGEP.AMBIENTE_HOMOLOGACAO)

    def test_ambiente(self):
        self.test__init__()

    def test_request(self):
        req_cep = RequestConsultaCEP('37.503-130')
        wb = WebserviceSIGEP(WebserviceSIGEP.AMBIENTE_HOMOLOGACAO)

        try:
            res = wb.request(req_cep)
        except ErroConexaoComServidor as exc:
            print exc.message
        except ErroConexaoTimeOut as exc:
            print exc.message
        except ErroRequisicao as exc:
            print exc.message

        self.assertIsInstance(res, ResponseBuscaCEP)

        req_cep = RequestConsultaCEP('37.503-130')
        wb = WebserviceSIGEP(WebserviceSIGEP.AMBIENTE_PRODUCAO)
        res = wb.request(req_cep)

        self.assertIsInstance(res, ResponseBuscaCEP)

        req_cep = RequestConsultaCEP('37.000-000')
        self.assertRaises(ErroValidacaoXML, wb.request, req_cep)
