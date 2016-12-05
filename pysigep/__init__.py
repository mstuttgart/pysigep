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


def send(xml_path, xml_method, api, soap_action=None, ambiente=1, **kwargs):
    """
    >>> xml_path = 'ConsultaCep.xml'
    >>> xml_method = 'consultaCEPResponse'
    >>> api = 'SIGEPWeb'
    >>> kw = {'cep': '83010140', }
    >>> send(xml_path, xml_method, api, **kw)  #doctest: +ELLIPSIS
    <Element return at 0x...>
    >>> send(xml_path, xml_method, api, **kw).bairro
    'Cruzeiro'
    >>> kw['cep'] = '123'
    >>> send(xml_path, xml_method, api, **kw)
    Traceback (most recent call last):
        ...
    AttributeError: no such child: consultaCEPResponse
    """

    path = os.path.join(os.path.dirname(__file__), 'templates')
    xml = render_xml(path, xml_path, kwargs)
    url = URLS[ambiente][api]
    header = {'Content-type': 'text/xml; charset=utf-8;'}
    if soap_action:
        header['SOAPAction'] = soap_action
    resposta = requests.post(url, data=xml, headers=header, verify=False)
    text = sanitize_response(resposta.text)
    if soap_action == 'http://tempuri.org/CalcPrecoPrazo':
        return text[1].Body[xml_method]['CalcPrecoPrazoResult']['Servicos']
    return text[1].Body[xml_method]['return']
