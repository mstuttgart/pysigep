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
from sigepweb.frete.consulta_frete import RequestCalcPrecoPrazo
from sigepweb.frete.consulta_frete import ResponseCalcPrecoPrazo
from sigepweb.webservices.webservice_frete import WebserviceFrete


class TestWebserviceFrete(TestCase):

    def test_request(self):
        server = WebserviceFrete()
        req = RequestCalcPrecoPrazo('40436,40215', '99200000', '37503130', '2',
                                    RequestCalcPrecoPrazo.FORMATO_CAIXA_PACOTE,
                                    100.0, 100.0, 100.0, 0.0, False, 0.00,
                                    False)

        self.assertIsInstance(server.request(req), ResponseCalcPrecoPrazo)
