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

import os
import requests

from pysigep.utils import render_xml, sanitize_response, URLS


__title__ = 'pysigep'
__version__ = '0.0.4'
__author__ = 'Michell Stuttgart Faria'
__license__ = 'MIT License'
__copyright__ = 'Copyright 2016 Michell Stuttgart Faria'


# Version synonym
VERSION = __version__


def _url(api, ambiente):
    return URLS[api][ambiente]


def send(xml_path, xml_method, api, url,
         soap_action=None, encoding="utf-8", **kwargs):
    """
    >>> xml_path = 'ConsultaCep.xml'
    >>> xml_method = 'consultaCEPResponse'
    >>> api = 'SIGEPWeb'
    >>> kw = {'cep': '83010140', }
    >>> url = _url(1, api)
    >>> send(xml_path, xml_method, api, url, **kw)  #doctest: +ELLIPSIS
    <Element return at 0x...>
    >>> send(xml_path, xml_method, api, url, **kw).bairro
    'Cruzeiro'
    >>> kw['cep'] = '123'
    >>> send(xml_path, xml_method, api, url, **kw)
    {'mensagem_erro': 'BUSCA DEFINIDA COMO EXATA, 0 CEP DEVE TER 8 DIGITOS'}
    """
    path = os.path.join(os.path.dirname(__file__), 'templates')
    xml = render_xml(path, xml_path, kwargs)
    header = {'Content-type': 'text/xml; charset=;%s' % encoding}
    if soap_action:
        header['SOAPAction'] = soap_action
    resposta = requests.post(url, data=xml.encode(encoding),
                             headers=header, verify=False)
    xml_resp, obj_resp = sanitize_response(resposta.text)
    if soap_action == 'http://tempuri.org/CalcPrecoPrazo':
        return obj_resp.Body[xml_method]['CalcPrecoPrazoResult']['Servicos']
    if xml_method in dir(obj_resp.Body):
        return obj_resp.Body[xml_method]['return']

    return {"mensagem_erro": obj_resp.Body.Fault.faultstring}
