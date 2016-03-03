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
from sigep.sigep.plp import TagDimesaoObjeto
from sigep.sigep.plp import TagDimensionTipoObjeto
from sigep.sigep.plp import TagDimensionAlturaLargura
from sigep.sigep.plp import TagDimensionComprimento
from sigep.sigep.plp import TagDimensionDiametro


class TestTagDimesaoObjeto(TestCase):

    def test_get_xml(self):

        obj = TagDimesaoObjeto()
        obj.tipo_objeto.valor = TagDimesaoObjeto.TIPO_CAIXA
        obj.altura.valor = 20
        obj.largura.valor = 30
        obj.comprimento.valor = 38
        obj.diametro.valor = 0

        xml = '<dimensao_objeto>'
        xml += '<tipo_objeto>002</tipo_objeto>'
        xml += '<dimensao_altura>20</dimensao_altura>'
        xml += '<dimensao_largura>30</dimensao_largura>'
        xml += '<dimensao_comprimento>38</dimensao_comprimento>'
        xml += '<dimensao_diametro>0</dimensao_diametro>'
        xml += '</dimensao_objeto>'

        self.assertEqual(xml, obj.get_xml())


class TestTagDimensionTipoObjeto(TestCase):

    def test_update_tags(self):
        obj = TagDimensionTipoObjeto('tipo_objeto', obrigatorio=True,
                                     tamanho=3)

        altura = TagDimensionAlturaLargura('dimensao_altura', valor=2)
        largura = TagDimensionAlturaLargura('dimensao_largura', valor=11)
        comprimento = TagDimensionComprimento('dimensao_comprimento', valor=16)
        diametro = TagDimensionDiametro('dimensao_diametro', valor=2)

        obj.tags.append(altura)
        obj.tags.append(largura)
        obj.tags.append(comprimento)
        obj.tags.append(diametro)
        obj.valor = TagDimesaoObjeto.TIPO_CAIXA

        obj.update_tags('002')

        self.assertEqual(obj.tags[0].obrigatorio, True)
        self.assertEqual(obj.tags[1].obrigatorio, True)
        self.assertEqual(obj.tags[2].obrigatorio, True)
        self.assertEqual(obj.tags[3].obrigatorio, False)


class TestTagDimensionAlturaLargura(TestCase):

    def test_update(self):
        obj = TagDimensionAlturaLargura('dimensao_altura', valor=2)
        obj.update('001')
        self.assertEqual(obj.obrigatorio, False)
        obj.update('002')
        self.assertEqual(obj.obrigatorio, True)
        obj.update('003')
        self.assertEqual(obj.obrigatorio, False)


class TestTagDimensionComprimento(TestCase):

    def test_update(self):
        obj = TagDimensionComprimento('dimensao_comprimento', valor=16)
        obj.update('001')
        self.assertEqual(obj.obrigatorio, False)
        obj.update('002')
        self.assertEqual(obj.obrigatorio, True)
        obj.update('003')
        self.assertEqual(obj.obrigatorio, True)


class TestTagDimensionDiametro(TestCase):

    def test_update(self):
        obj = TagDimensionDiametro('dimensao_diametro', valor=2)
        obj.update('001')
        self.assertEqual(obj.obrigatorio, False)
        obj.update('002')
        self.assertEqual(obj.obrigatorio, False)
        obj.update('003')
        self.assertEqual(obj.obrigatorio, True)
