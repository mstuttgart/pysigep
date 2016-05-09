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
from pysigep.base import TagBase, RequestBaseRastreamento
from pysigep.base import RequestBase
from pysigep.base import RequestBaseFrete
from pysigep.base import RequestBaseSIGEP
from pysigep.base import RequestBaseSIGEPAuthentication
from pysigep.base import ResponseBase


class TestTagBase(TestCase):

    def test_get_xml(self):
        tag = TagBase()
        self.assertRaises(NotImplementedError, tag.get_xml)


class TestRequestBase(TestCase):

    def test_response(self):
        req = RequestBase(ResponseBase)
        self.assertEqual(req.response_class_ref, ResponseBase)

    def test_get_data(self):
        req = RequestBase(ResponseBase)
        self.assertRaises(NotImplementedError, req.get_data)


class TestRequestBaseSIGEP(TestCase):

    def test_get_data(self):
        req = RequestBaseSIGEP(ResponseBase)
        self.assertRaises(NotImplementedError, req.get_data)


class TestRequestBaseAutentic(TestCase):

    def test_response(self):
        req = RequestBaseSIGEPAuthentication(ResponseBase, 'sigep', '12345')
        self.assertEqual(req.response_class_ref, ResponseBase)

    def test_get_data(self):

        req = RequestBaseSIGEPAuthentication(ResponseBase, 'sigep', '12345')
        xml = u'<usuario>%s</usuario>' % req.usuario.valor
        xml += u'<senha>%s</senha>' % req.senha.valor

        self.assertEqual(req.get_data(), xml)


class TestRequestBaseFrete(TestCase):

    def test_get_data(self):
        req = RequestBaseFrete(ResponseBase)
        self.assertRaises(NotImplementedError, req.get_data)


class TestRequestBaseRastreamento(TestCase):

    def test_get_data(self):
        req = RequestBaseRastreamento(ResponseBase)
        self.assertRaises(NotImplementedError, req.get_data)


class TestResponseBase(TestCase):

    def test__parse_xml(self):
        resp = ResponseBase()
        self.assertRaises(NotImplementedError, resp._parse_xml, '')
