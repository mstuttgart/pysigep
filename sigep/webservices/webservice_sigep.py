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

import requests
from webservice_base import WebserviceBase
from sigep import sigep_exceptions


class WebserviceSIGEP(WebserviceBase):
    AMBIENTE_PRODUCAO = 'PRODUCAO'
    AMBIENTE_HOMOLOGACAO = 'HOMOLOGACAO'

    def __init__(self, ambiente):

        amb = {
            WebserviceSIGEP.AMBIENTE_HOMOLOGACAO:
                'https://apphom.correios.com.br/SigepMasterJPA/'
                'AtendeClienteService/AtendeCliente?wsdl',

            WebserviceSIGEP.AMBIENTE_PRODUCAO:
                'https://apps.correios.com.br/SigepMasterJPA/'
                'AtendeClienteService/AtendeCliente?wsdl'
        }

        try:
            super(WebserviceSIGEP, self).__init__(amb[ambiente])
            self._ambiente = ambiente
        except KeyError as exp:
            print exp.message
            super(WebserviceSIGEP, self).__init__(
                amb[WebserviceSIGEP.AMBIENTE_HOMOLOGACAO])
            self._ambiente = WebserviceSIGEP.AMBIENTE_HOMOLOGACAO

    @property
    def ambiente(self):
        return self._ambiente

    def request(self, obj_param, ssl_verify=False):
        try:

            resposta = requests.post(self.url, data=obj_param.get_xml(),
                                     headers={'Content-type': 'text/xml'},
                                     verify=ssl_verify)

            if not resposta.ok:
                msg = WebserviceSIGEP._parse_error(
                    resposta.text.encode('utf8'))
                raise sigep_exceptions.ErroValidacaoXML(msg)

            # Criamos um response dinamicamente para cada tipo de classe
            response = obj_param.response()

            response.status_code = resposta.status_code
            response.encoding = resposta.encoding
            response.xml = resposta.text.encode('utf8')
            response.body_request = resposta.request.body
            return response

        except requests.ConnectionError as exc:
            raise sigep_exceptions.ErroConexaoComServidor(exc.message)

        except requests.Timeout as exc:
            raise sigep_exceptions.ErroConexaoTimeOut(exc.message)

        except requests.exceptions.InvalidSchema as exc:
            raise sigep_exceptions.ErroInvalidSchema(exc.message)

        except requests.exceptions.RequestException as exc:
            raise sigep_exceptions.ErroRequisicao(exc.message)

    @staticmethod
    def _parse_error(xml):
        import xml.etree.ElementTree as Et
        return Et.fromstring(xml).findtext('.//faultstring')
