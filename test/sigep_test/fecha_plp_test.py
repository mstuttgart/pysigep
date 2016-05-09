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

from pysigep.base import RequestBaseSIGEPAuthentication
from pysigep.sigep.fecha_plp import RequestFechaPLPVariosServicos
from pysigep.sigep.fecha_plp import ResponseFechaPLPVariosServicos
from pysigep.sigep.plp import XmlPLP, TagObjetoPostal, TagDimesaoObjeto


class TestRequestFechaPLPVariosServicos(TestCase):

    def test_get_data(self):

        self.maxDiff = None

        # Incializamos objeto postal
        obj_post = TagObjetoPostal('41068')
        obj_post.numero_etiqueta.valor = 'PH185560916BR'
        obj_post.codigo_servico_postagem.valor = '41068'
        obj_post.cubagem.valor = 0.0000
        obj_post.peso.valor = 200

        obj_post.destinatario.nome.valor = 'Destino Ltda'
        obj_post.destinatario.logradouro.valor = 'Avenida Central'
        obj_post.destinatario.complemento.valor = 'Qd: 102 A Lt: 04'
        obj_post.destinatario.numero.valor = '1065'
        obj_post.destinatario.telefone.valor = '6212349644'

        obj_post.nacional.bairro.valor = 'Setor Industrial'
        obj_post.nacional.cep.valor = '74000100'
        obj_post.nacional.cidade.valor = u'Goiânia'
        obj_post.nacional.uf.valor = 'GO'
        obj_post.nacional.numero_nfe.valor = '102030'
        obj_post.nacional.valor_a_cobrar.valor = 0.0

        obj_post.servico_adicional.add_codigo_servico_adicional('001')
        obj_post.servico_adicional.add_codigo_servico_adicional('019')
        obj_post.servico_adicional.valor_declarado.valor = 99.0

        obj_post.dimensao_objeto.tipo_objeto.valor = \
            TagDimesaoObjeto.TIPO_CAIXA
        obj_post.dimensao_objeto.altura.valor = 20
        obj_post.dimensao_objeto.largura.valor = 30
        obj_post.dimensao_objeto.comprimento.valor = 38
        obj_post.dimensao_objeto.diametro.valor = 0

        obj_post.status_processamento.valor = '0'

        # Inicializamos o xml da PLP
        tag = XmlPLP()
        tag.plp.cartao_postagem.valor = '0123456789'

        tag.remetente.numero_contrato.valor = '0123456789'
        tag.remetente.numero_diretoria.valor = 36
        tag.remetente.codigo_administrativo.valor = '12345678'
        tag.remetente.nome.valor = u'Empresa Ltda'
        tag.remetente.logradouro.valor = u'Avenida Central'
        tag.remetente.numero.valor = '2370'
        tag.remetente.complemento.valor = u'sala 1205,12° andar'
        tag.remetente.bairro.valor = 'Centro'
        tag.remetente.cep.valor = '70002900'
        tag.remetente.cidade.valor = u'Brasília'
        tag.remetente.uf.valor = 'PR'
        tag.remetente.telefone.valor = '6112345008'
        tag.remetente.email.valor = 'cli@mail.com.br'

        tag.lista_objeto_postal.append(obj_post)

        etiquetas = ['PH185560916BR']

        req = RequestFechaPLPVariosServicos(tag.get_xml(), 123, '0123456789',
                                            etiquetas, 'sigep', 'n5f9t8')

        xml = RequestBaseSIGEPAuthentication.HEADER
        xml += '<cli:fechaPlpVariosServicos>'
        xml += '<xml>%s</xml>' % tag.get_xml()
        xml += '<idPlpCliente>123</idPlpCliente>'
        xml += '<cartaoPostagem>0123456789</cartaoPostagem>'
        xml += '<listaEtiquetas>PH18556091BR</listaEtiquetas>'
        xml += '<usuario>sigep</usuario>'
        xml += '<senha>n5f9t8</senha>'
        xml += '</cli:fechaPlpVariosServicos>'
        xml += RequestBaseSIGEPAuthentication.FOOTER

        self.assertEqual(xml, req.get_data())


class TestResponseFechaPLPVariosServicos(TestCase):

    def test__parse_xml(self):

        xml = '''<S:Envelope
        xmlns:S=\"http://schemas.xmlsoap.org/soap/envelope/\">
        <S:Body>
        <ns2:fechaPlpResponse xmlns:ns2=\"http://cliente.bean.master.sigep.bsb
        .correios.com.br/\">
        <return>1545168</return>
        </ns2:fechaPlpResponse>
        </S:Body>
        </S:Envelope>'''.replace('\n', '')

        resp = ResponseFechaPLPVariosServicos()
        resp._parse_xml(xml)
        self.assertEqual(resp.resposta['id_plp'], '1545168')
