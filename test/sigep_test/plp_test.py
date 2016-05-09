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
from pysigep.sigep.plp import XmlPLP
from pysigep.sigep.plp import TagPLP
from pysigep.sigep.plp import TagRemetente
from pysigep.sigep.plp import TagObjetoPostal
from pysigep.sigep.plp import TagDestinatario
from pysigep.sigep.plp import TagNacional
from pysigep.sigep.plp import TagServicoAdicional
from pysigep.sigep.plp import TagDimesaoObjeto
from pysigep.sigep.plp import TagDimensionTipoObjeto
from pysigep.sigep.plp import TagDimensionAlturaLargura
from pysigep.sigep.plp import TagDimensionComprimento
from pysigep.sigep.plp import TagDimensionDiametro


class TestXmlPLP(TestCase):

    def test_get_xml(self):

        self.maxDiff = None

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

        xml = u'<?xml version=\"1.0\" encoding=\"UTF-8\" ?>'
        xml += u'<correioslog>'
        xml += u'<tipo_arquivo>Postagem</tipo_arquivo>'
        xml += u'<versao_arquivo>2.3</versao_arquivo>'

        xml += u'<plp>'
        xml += u'<id_plp></id_plp>'
        xml += u'<valor_global></valor_global>'
        xml += u'<mcu_unidade_postagem></mcu_unidade_postagem>'
        xml += u'<nome_unidade_postagem></nome_unidade_postagem>'
        xml += u'<cartao_postagem>0123456789</cartao_postagem>'
        xml += u'</plp>'

        xml += u'<remetente>'
        xml += u'<numero_contrato>0123456789</numero_contrato>'
        xml += u'<numero_diretoria>36</numero_diretoria>'
        xml += u'<codigo_administrativo>12345678</codigo_administrativo>'
        xml += u'<nome_remetente><![CDATA[Empresa Ltda]]></nome_remetente>'
        xml += u'<logradouro_remetente><![CDATA[Avenida Central]]>' \
               u'</logradouro_remetente>'
        xml += u'<numero_remetente>2370</numero_remetente>'
        xml += u'<complemento_remetente><![CDATA[sala 1205,12° andar]]>' \
               u'</complemento_remetente>'
        xml += u'<bairro_remetente><![CDATA[Centro]]></bairro_remetente>'
        xml += u'<cep_remetente>70002900</cep_remetente>'
        xml += u'<cidade_remetente><![CDATA[Brasília]]></cidade_remetente>'
        xml += u'<uf_remetente>PR</uf_remetente>'
        xml += u'<telefone_remetente>6112345008</telefone_remetente>'
        xml += u'<fax_remetente></fax_remetente>'
        xml += u'<email_remetente><![CDATA[cli@mail.com.br]]>' \
               u'</email_remetente>'
        xml += u'</remetente>'

        xml += u'<forma_pagamento></forma_pagamento>'

        xml += u'<objeto_postal>'

        xml += u'<numero_etiqueta>PH185560916BR</numero_etiqueta>'
        xml += u'<codigo_objeto_cliente></codigo_objeto_cliente>'
        xml += u'<codigo_servico_postagem>41068</codigo_servico_postagem>'
        xml += u'<cubagem>0.0</cubagem>'
        xml += u'<peso>200</peso>'
        xml += u'<rt1></rt1>'
        xml += u'<rt2></rt2>'

        xml += u'<destinatario>'
        xml += u'<nome_destinatario><![CDATA[Destino Ltda]]>' \
               u'</nome_destinatario>'
        xml += u'<telefone_destinatario>6212349644</telefone_destinatario>'
        xml += u'<celular_destinatario></celular_destinatario>'
        xml += u'<email_destinatario></email_destinatario>'
        xml += u'<logradouro_destinatario><![CDATA[Avenida Central]]>' \
               u'</logradouro_destinatario>'
        xml += u'<complemento_destinatario><![CDATA[Qd: 102 A Lt: 04]]>' \
               u'</complemento_destinatario>'
        xml += u'<numero_end_destinatario>1065</numero_end_destinatario>'
        xml += u'</destinatario>'

        xml += u'<nacional>'
        xml += u'<bairro_destinatario><![CDATA[Setor Industrial]]>' \
               u'</bairro_destinatario>'
        xml += u'<cidade_destinatario><![CDATA[Goiânia]]>' \
               u'</cidade_destinatario>'
        xml += u'<uf_destinatario>GO</uf_destinatario>'
        xml += u'<cep_destinatario>74000100</cep_destinatario>'
        xml += u'<codigo_usuario_postal></codigo_usuario_postal>'
        xml += u'<centro_custo_cliente></centro_custo_cliente>'
        xml += u'<numero_nota_fiscal>102030</numero_nota_fiscal>'
        xml += u'<serie_nota_fiscal></serie_nota_fiscal>'
        xml += u'<valor_nota_fiscal></valor_nota_fiscal>'
        xml += u'<natureza_nota_fiscal></natureza_nota_fiscal>'
        xml += u'<descricao_objeto><![CDATA[]]></descricao_objeto>'
        xml += u'<valor_a_cobrar>0.0</valor_a_cobrar>'
        xml += u'</nacional>'

        # O servico adicional 025 sempre deverá ser informado.
        xml += u'<servico_adicional>'
        xml += u'<codigo_servico_adicional>025</codigo_servico_adicional>'
        xml += u'<codigo_servico_adicional>001</codigo_servico_adicional>'
        xml += u'<codigo_servico_adicional>019</codigo_servico_adicional>'
        xml += u'<valor_declarado>99.0</valor_declarado>'
        xml += u'</servico_adicional>'

        xml += u'<dimensao_objeto>'
        xml += u'<tipo_objeto>002</tipo_objeto>'
        xml += u'<dimensao_altura>20</dimensao_altura>'
        xml += u'<dimensao_largura>30</dimensao_largura>'
        xml += u'<dimensao_comprimento>38</dimensao_comprimento>'
        xml += u'<dimensao_diametro>0</dimensao_diametro>'
        xml += u'</dimensao_objeto>'

        xml += u'<data_postagem_sara></data_postagem_sara>'
        xml += u'<status_processamento>0</status_processamento>'
        xml += u'<numero_comprovante_postagem></numero_comprovante_postagem>'
        xml += u'<valor_cobrado></valor_cobrado>'
        xml += u'</objeto_postal>'
        xml += u'</correioslog>'

        self.assertEqual(xml, tag.get_xml())


class TestTagPLP(TestCase):

    def test_get_xml(self):

        xml = '<plp>'
        xml += '<id_plp></id_plp>'
        xml += '<valor_global></valor_global>'
        xml += '<mcu_unidade_postagem></mcu_unidade_postagem>'
        xml += '<nome_unidade_postagem></nome_unidade_postagem>'
        xml += '<cartao_postagem>0123456789</cartao_postagem>'
        xml += '</plp>'

        tag = TagPLP()
        tag.cartao_postagem.valor = '0123456789'

        self.assertEqual(xml, tag.get_xml())


class TestTagRemetente(TestCase):

    def test_get_xml(self):

        self.maxDiff = None
        xml = u'<remetente>'
        xml += u'<numero_contrato>0123456789</numero_contrato>'
        xml += u'<numero_diretoria>36</numero_diretoria>'
        xml += u'<codigo_administrativo>12345678</codigo_administrativo>'
        xml += u'<nome_remetente><![CDATA[Empresa Ltda]]></nome_remetente>'
        xml += u'<logradouro_remetente><![CDATA[Avenida Central]]>' \
               u'</logradouro_remetente>'
        xml += u'<numero_remetente>2370</numero_remetente>'
        xml += u'<complemento_remetente><![CDATA[sala 1205,12° andar]]>' \
               u'</complemento_remetente>'
        xml += u'<bairro_remetente><![CDATA[Centro]]></bairro_remetente>'
        xml += u'<cep_remetente>70002900</cep_remetente>'
        xml += u'<cidade_remetente><![CDATA[Brasília]]></cidade_remetente>'
        xml += u'<uf_remetente>PR</uf_remetente>'
        xml += u'<telefone_remetente>6112345008</telefone_remetente>'
        xml += u'<fax_remetente></fax_remetente>'
        xml += u'<email_remetente><![CDATA[cli@mail.com.br]]>' \
               u'</email_remetente>'
        xml += u'</remetente>'

        tag = TagRemetente()
        tag.numero_contrato.valor = '0123456789'
        tag.numero_diretoria.valor = 36
        tag.codigo_administrativo.valor = '12345678'
        tag.nome.valor = u'Empresa Ltda'
        tag.logradouro.valor = u'Avenida Central'
        tag.numero.valor = '2370'
        tag.complemento.valor = u'sala 1205,12° andar'
        tag.bairro.valor = 'Centro'
        tag.cep.valor = '70002900'
        tag.cidade.valor = u'Brasília'
        tag.uf.valor = 'PR'
        tag.telefone.valor = '6112345008'
        tag.email.valor = 'cli@mail.com.br'

        self.assertEqual(xml, tag.get_xml())


class TestTagObjetoPostal(TestCase):

    def test_get_xml(self):

        self.maxDiff = None

        tag = TagObjetoPostal('41068')
        tag.numero_etiqueta.valor = 'PH185560916BR'
        tag.codigo_servico_postagem.valor = '41068'
        tag.cubagem.valor = 0.0000
        tag.peso.valor = 200

        tag.destinatario.nome.valor = 'Destino Ltda'
        tag.destinatario.logradouro.valor = 'Avenida Central'
        tag.destinatario.complemento.valor = 'Qd: 102 A Lt: 04'
        tag.destinatario.numero.valor = '1065'
        tag.destinatario.telefone.valor = '6212349644'

        tag.nacional.bairro.valor = 'Setor Industrial'
        tag.nacional.cep.valor = '74000100'
        tag.nacional.cidade.valor = u'Goiânia'
        tag.nacional.uf.valor = 'GO'
        tag.nacional.numero_nfe.valor = '102030'
        tag.nacional.valor_a_cobrar.valor = 0.0

        tag.servico_adicional.add_codigo_servico_adicional('001')
        tag.servico_adicional.add_codigo_servico_adicional('019')
        tag.servico_adicional.valor_declarado.valor = 99.0

        tag.dimensao_objeto.tipo_objeto.valor = TagDimesaoObjeto.TIPO_CAIXA
        tag.dimensao_objeto.altura.valor = 20
        tag.dimensao_objeto.largura.valor = 30
        tag.dimensao_objeto.comprimento.valor = 38
        tag.dimensao_objeto.diametro.valor = 0

        tag.status_processamento.valor = '0'

        xml = u'<objeto_postal>'

        xml += u'<numero_etiqueta>PH185560916BR</numero_etiqueta>'
        xml += u'<codigo_objeto_cliente></codigo_objeto_cliente>'
        xml += u'<codigo_servico_postagem>41068</codigo_servico_postagem>'
        xml += u'<cubagem>0.0</cubagem>'
        xml += u'<peso>200</peso>'
        xml += u'<rt1></rt1>'
        xml += u'<rt2></rt2>'

        xml += u'<destinatario>'
        xml += u'<nome_destinatario><![CDATA[Destino Ltda]]>' \
               u'</nome_destinatario>'
        xml += u'<telefone_destinatario>6212349644</telefone_destinatario>'
        xml += u'<celular_destinatario></celular_destinatario>'
        xml += u'<email_destinatario></email_destinatario>'
        xml += u'<logradouro_destinatario><![CDATA[Avenida Central]]>' \
               u'</logradouro_destinatario>'
        xml += u'<complemento_destinatario><![CDATA[Qd: 102 A Lt: 04]]>' \
               u'</complemento_destinatario>'
        xml += u'<numero_end_destinatario>1065</numero_end_destinatario>'
        xml += u'</destinatario>'

        xml += u'<nacional>'
        xml += u'<bairro_destinatario><![CDATA[Setor Industrial]]>' \
               u'</bairro_destinatario>'
        xml += u'<cidade_destinatario><![CDATA[Goiânia]]>' \
               u'</cidade_destinatario>'
        xml += u'<uf_destinatario>GO</uf_destinatario>'
        xml += u'<cep_destinatario>74000100</cep_destinatario>'
        xml += u'<codigo_usuario_postal></codigo_usuario_postal>'
        xml += u'<centro_custo_cliente></centro_custo_cliente>'
        xml += u'<numero_nota_fiscal>102030</numero_nota_fiscal>'
        xml += u'<serie_nota_fiscal></serie_nota_fiscal>'
        xml += u'<valor_nota_fiscal></valor_nota_fiscal>'
        xml += u'<natureza_nota_fiscal></natureza_nota_fiscal>'
        xml += u'<descricao_objeto><![CDATA[]]></descricao_objeto>'
        xml += u'<valor_a_cobrar>0.0</valor_a_cobrar>'
        xml += u'</nacional>'

        # O servico adicional 025 sempre deverá ser informado.
        xml += u'<servico_adicional>'
        xml += u'<codigo_servico_adicional>025</codigo_servico_adicional>'
        xml += u'<codigo_servico_adicional>001</codigo_servico_adicional>'
        xml += u'<codigo_servico_adicional>019</codigo_servico_adicional>'
        xml += u'<valor_declarado>99.0</valor_declarado>'
        xml += u'</servico_adicional>'

        xml += u'<dimensao_objeto>'
        xml += u'<tipo_objeto>002</tipo_objeto>'
        xml += u'<dimensao_altura>20</dimensao_altura>'
        xml += u'<dimensao_largura>30</dimensao_largura>'
        xml += u'<dimensao_comprimento>38</dimensao_comprimento>'
        xml += u'<dimensao_diametro>0</dimensao_diametro>'
        xml += u'</dimensao_objeto>'

        xml += u'<data_postagem_sara></data_postagem_sara>'
        xml += u'<status_processamento>0</status_processamento>'
        xml += u'<numero_comprovante_postagem></numero_comprovante_postagem>'
        xml += u'<valor_cobrado></valor_cobrado>'
        xml += u'</objeto_postal>'

        self.assertEqual(xml, tag.get_xml())


class TestTagDestinatario(TestCase):

    def test_get_xml(self):

        self.maxDiff = None

        xml = u'<destinatario>'
        xml += u'<nome_destinatario><![CDATA[João]]></nome_destinatario>'
        xml += u'<telefone_destinatario>353136232888</telefone_destinatario>'
        xml += u'<celular_destinatario>003591419415</celular_destinatario>'
        xml += u'<email_destinatario></email_destinatario>'
        xml += u'<logradouro_destinatario><![CDATA[Rua Geraldino Campista]]>' \
               u'</logradouro_destinatario>'
        xml += u'<complemento_destinatario><![CDATA[]]>' \
               u'</complemento_destinatario>'
        xml += u'<numero_end_destinatario>123</numero_end_destinatario>'
        xml += u'</destinatario>'

        tag = TagDestinatario()
        tag.nome.valor = u'João'
        tag.logradouro.valor = 'Rua Geraldino Campista'
        tag.numero.valor = '123'
        tag.telefone.valor = '353136232888'
        tag.celular.valor = '003591419415'

        self.assertEqual(xml, tag.get_xml())


class TestTagNacional(TestCase):

    def test_get_xml(self):

        self.maxDiff = None

        xml = u'<nacional>'
        xml += u'<bairro_destinatario><![CDATA[Vila Poddis]]>' \
               u'</bairro_destinatario>'
        xml += u'<cidade_destinatario><![CDATA[Itajubá]]>' \
               u'</cidade_destinatario>'
        xml += u'<uf_destinatario>MG</uf_destinatario>'
        xml += u'<cep_destinatario>37503003</cep_destinatario>'
        xml += u'<codigo_usuario_postal></codigo_usuario_postal>'
        xml += u'<centro_custo_cliente></centro_custo_cliente>'
        xml += u'<numero_nota_fiscal>112</numero_nota_fiscal>'
        xml += u'<serie_nota_fiscal>1</serie_nota_fiscal>'
        xml += u'<valor_nota_fiscal></valor_nota_fiscal>'
        xml += u'<natureza_nota_fiscal></natureza_nota_fiscal>'
        xml += u'<descricao_objeto><![CDATA[]]></descricao_objeto>'
        xml += u'<valor_a_cobrar>0.0</valor_a_cobrar>'
        xml += u'</nacional>'

        tag_nac = TagNacional('41068')
        tag_nac.bairro.valor = 'Vila Poddis'
        tag_nac.cep.valor = '37503003'
        tag_nac.cidade.valor = u'Itajubá'
        tag_nac.uf.valor = 'MG'
        tag_nac.numero_nfe.valor = '112'
        tag_nac.serie_nfe.valor = '1'

        self.assertEqual(xml, tag_nac.get_xml())


class TestTagServicoAdicional(TestCase):

    def test_add_codigo_servico_adicional(self):
        serv_add = TagServicoAdicional()
        serv_add.add_codigo_servico_adicional('019')
        serv_add.add_codigo_servico_adicional('014')

        self.assertEqual(serv_add.lista_codigo_servico_adicional[0].valor,
                         '019')
        self.assertEqual(serv_add.lista_codigo_servico_adicional[1].valor,
                         '014')

    def test_get_xml(self):

        xml = '<servico_adicional>'
        xml += '<codigo_servico_adicional>025</codigo_servico_adicional>'
        xml += '<codigo_servico_adicional>019</codigo_servico_adicional>'
        xml += '<valor_declarado>20.0</valor_declarado>'
        xml += '</servico_adicional>'

        serv_add = TagServicoAdicional()
        serv_add.add_codigo_servico_adicional('019')
        serv_add.valor_declarado.valor = 20.0

        self.assertEqual(xml, serv_add.get_xml())


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
