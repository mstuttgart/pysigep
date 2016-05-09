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
import requests
from pysigep import sigep_exceptions


class WebserviceBase(object):

    def __init__(self, url):
        self._url = url

    @property
    def url(self):
        return self._url

    def request(self, obj_param, ssl_verify=False):

        try:
            resposta = requests.post(self.url, data=obj_param.get_data(),
                                     headers={'Content-type': 'text/xml'},
                                     verify=ssl_verify)

            if not resposta.ok:
                msg = WebserviceBase._parse_error(resposta.text.encode('utf8'))
                raise sigep_exceptions.ErroValidacaoXML(msg)

            # Criamos um response dinamicamente para cada tipo de classe
            response = obj_param.response_class_ref()

            response.status_code = resposta.status_code
            response.encoding = resposta.encoding
            response.xml = resposta.text.encode('utf8')
            response.body_request = resposta.request.body
            return response

        except requests.ConnectionError as exc:
            raise sigep_exceptions.ErroConexaoComServidor(exc.message)

        except requests.Timeout as exc:
            raise sigep_exceptions.ErroConexaoTimeOut(exc.message)

        except requests.exceptions.RequestException as exc:
            raise sigep_exceptions.ErroRequisicao(exc.message)

    @staticmethod
    def _parse_error(xml):
        return Et.fromstring(xml).findtext('.//faultstring')
