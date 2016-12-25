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

from pysigep.sigep import solicita_etiquetas_com_dv
from pysigep.sigep import digito_verificador_etiqueta


class TesteSolicitaEtiqueta(TestCase):

    def test_solicita_etiquetas(self):

        solicitacao = {
            'usuario': 'sigep',
            'senha': 'n5f9t8',
            'identificador': '34028316000103',
            'idServico': '104625',
            'qtdEtiquetas': '10',
        }
        with self.assertRaises(Exception):
            solicita_etiquetas_com_dv(**solicitacao)

        solicitacao['ambiente'] = 1
        etiquetas = solicita_etiquetas_com_dv(**solicitacao)

        self.assertEqual(len(etiquetas), 10, 'Qtd. de etiquetas errada, '
                                             'Expected: %s, Got: %d' %
                         (solicitacao['qtdEtiquetas'], len(etiquetas)))

    def test_digito_verificador_etiqueta(self):
        etiqueta = 'DL76023727 BR'
        etiqueta_c_dv = digito_verificador_etiqueta(etiqueta)
        self.assertEqual(etiqueta_c_dv,
                         'DL760237272BR',
                         'DV incorreto,'
                         ' expect.: 2, got: %s' % (etiqueta_c_dv[10]))
