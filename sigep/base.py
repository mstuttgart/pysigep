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

from campos import CampoString


class TagBase(object):

    def get_xml(self):
        raise NotImplementedError


class RequestBase(object):

    def __init__(self, response_obj):
        self._response = response_obj
        self._header = None
        self._footer = None

    @property
    def header(self):
        return self._header

    @property
    def footer(self):
        return self._footer

    @property
    def response(self):
        return self._response

    def get_xml(self):
        raise NotImplementedError


class RequestBaseSIGEP(RequestBase):

    def __init__(self, response_obj):
        super(RequestBaseSIGEP, self).__init__(response_obj)
        self._header = \
            '''<soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\"
            xmlns:cli=\"http://cliente.bean.master.sigep.bsb.correios.com.br/\">
            <soap:Header/><soap:Body>'''
        self._footer = '</soap:Body></soap:Envelope>'


class RequestBaseSIGEPAutentic(RequestBaseSIGEP):

    def __init__(self, response_obj, usuario, senha):
        super(RequestBaseSIGEPAutentic, self).__init__(response_obj)
        self._usuario = CampoString('usuario', obrigatorio=True)
        self._senha = CampoString('senha', obrigatorio=True)

        self._usuario.valor = usuario
        self._senha.valor = senha

    @property
    def usuario(self):
        return self._usuario

    @property
    def senha(self):
        return self._senha

    def get_xml(self):
        xml = self.usuario.get_xml()
        xml += self.senha.get_xml()
        return xml


class RequestBaseFrete(RequestBase):

    def __init__(self, response_obj):
        super(RequestBaseFrete, self).__init__(response_obj)
        self._header = '''<soap:Envelope xmlns:xsi=\"http://www.w3.org/2001/
        XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\"
        xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\"><soap:Body>'''
        self._footer = '</soap:Body></soap:Envelope>'


class ResponseBase(object):

    def __init__(self):
        self.status_code = None
        self.encoding = None
        self._xml = None
        self.body_request = None

    @property
    def xml(self):
        return self._xml

    @xml.setter
    def xml(self, value):
        self._xml = value
        self._parse_xml(value)

    def _parse_xml(self, xml):
        raise NotImplementedError
