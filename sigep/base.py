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

    def __init__(self, response_class_ref):
        self._response_class_ref = response_class_ref

    @property
    def response_class_ref(self):
        return self._response_class_ref

    def get_data(self):
        raise NotImplementedError


class RequestBaseSIGEP(RequestBase):

    HEADER = '<soap:Envelope ' \
             'xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\" ' \
             'xmlns:cli=\"http://cliente.bean.master.sigep.bsb.correios.com' \
             '.br/\"><soap:Header/><soap:Body>'

    FOOTER = '</soap:Body></soap:Envelope>'

    def __init__(self, response_class_ref):
        super(RequestBaseSIGEP, self).__init__(response_class_ref)

    def get_data(self):
        raise NotImplementedError


class RequestBaseSIGEPAuthentication(RequestBaseSIGEP):

    def __init__(self, response_class_ref, usuario, senha):
        super(RequestBaseSIGEPAuthentication, self).__init__(
            response_class_ref)
        self.usuario = CampoString('usuario', obrigatorio=True)
        self.senha = CampoString('senha', obrigatorio=True)

        self.usuario.valor = usuario
        self.senha.valor = senha

    def get_data(self):
        xml = self.usuario.get_xml()
        xml += self.senha.get_xml()
        return xml


class RequestBaseFrete(RequestBase):

    HEADER = '<soap:Envelope xmlns:xsi=\"http://www.w3.org/2001/' \
                       'XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/' \
                       '2001/XMLSchema\" xmlns:soap=\"http://' \
                       'schemas.xmlsoap.org/soap/envelope/\"><soap:Body>'
    FOOTER = '</soap:Body></soap:Envelope>'

    def __init__(self, response_class_ref):
        super(RequestBaseFrete, self).__init__(response_class_ref)

    def get_data(self):
        raise NotImplementedError


class RequestBaseRastreamento(RequestBase):

    def __init__(self, response_class_ref):
        super(RequestBaseRastreamento, self).__init__(response_class_ref)

    def get_data(self):
        raise NotImplementedError


class ResponseBase(object):

    def __init__(self):
        self.status_code = None
        self.encoding = None
        self._xml = None
        self.body_request = None
        self.resposta = None

    @property
    def xml(self):
        return self._xml

    @xml.setter
    def xml(self, value):
        self._xml = value
        self._parse_xml(value)

    def _parse_xml(self, xml):
        raise NotImplementedError
