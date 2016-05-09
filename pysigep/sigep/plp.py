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

from pysigep.base import TagBase
from pysigep.campos import CampoCEP
from pysigep.campos import CampoString
from pysigep.campos import CampoUnicode
from pysigep.campos import CampoInteiro
from pysigep.campos import CampoDecimal


class XmlPLP(TagBase):
    def __init__(self):
        self.forma_pagamento = CampoString(nome='forma_pagamento', valor='')
        self.plp = TagPLP()
        self.remetente = TagRemetente()
        self.lista_objeto_postal = []

    def get_xml(self):
        xml = '<?xml version=\"1.0\" encoding=\"UTF-8\" ?>'
        xml += '<correioslog>'
        xml += '<tipo_arquivo>Postagem</tipo_arquivo>'
        xml += '<versao_arquivo>2.3</versao_arquivo>'
        xml += self.plp.get_xml()
        xml += self.remetente.get_xml()
        xml += self.forma_pagamento.get_xml()

        for obj_post in self.lista_objeto_postal:
            xml += obj_post.get_xml()

        xml += '</correioslog>'

        return xml


class TagPLP(TagBase):

    def __init__(self):
        super(TagPLP, self).__init__()
        self.cartao_postagem = CampoString('cartao_postagem',
                                           obrigatorio=True,
                                           tamanho=10)

    def get_xml(self):
        xml = '<plp>'
        xml += '<id_plp></id_plp>'
        xml += '<valor_global></valor_global>'
        xml += '<mcu_unidade_postagem></mcu_unidade_postagem>'
        xml += '<nome_unidade_postagem></nome_unidade_postagem>'
        xml += self.cartao_postagem.get_xml()
        xml += '</plp>'

        return xml


class TagRemetente(TagBase):

    def __init__(self):
        super(TagRemetente, self).__init__()

        self.numero_contrato = CampoString('numero_contrato', tamanho=10,
                                           obrigatorio=True)
        self.numero_diretoria = CampoInteiro('numero_diretoria',
                                             obrigatorio=True)
        self.codigo_administrativo = CampoString('codigo_administrativo',
                                                 obrigatorio=True, tamanho=8)
        self.nome = CampoUnicode('nome_remetente', obrigatorio=True,
                                 tamanho=50)
        self.logradouro = CampoUnicode('logradouro_remetente', tamanho=40,
                                       obrigatorio=True)
        self.numero = CampoString('numero_remetente', tamanho=5,
                                  obrigatorio=True)
        self.complemento = CampoUnicode('complemento_remetente', tamanho=20,
                                        obrigatorio=False)
        self.bairro = CampoUnicode('bairro_remetente', obrigatorio=True,
                                   tamanho=20)
        self.cep = CampoCEP('cep_remetente', obrigatorio=True)
        self.cidade = CampoUnicode('cidade_remetente', tamanho=30,
                                   obrigatorio=True)
        self.uf = CampoString('uf_remetente', obrigatorio=True, tamanho=2)
        self.telefone = CampoString('telefone_remetente',
                                    obrigatorio=False, tamanho=12)
        self.fax = CampoString('fax_remetente', obrigatorio=False, tamanho=12)
        self.email = CampoUnicode('email_remetente', tamanho=50,
                                  obrigatorio=False)

    def get_xml(self):

        xml = '<remetente>'
        xml += self.numero_contrato.get_xml()
        xml += self.numero_diretoria.get_xml()
        xml += self.codigo_administrativo.get_xml()
        xml += self.nome.get_xml()
        xml += self.logradouro.get_xml()
        xml += self.numero.get_xml()
        xml += self.complemento.get_xml()
        xml += self.bairro.get_xml()
        xml += self.cep.get_xml()
        xml += self.cidade.get_xml()
        xml += self.uf.get_xml()
        xml += self.telefone.get_xml()
        xml += self.fax.get_xml()
        xml += self.email.get_xml()
        xml += '</remetente>'

        return xml


class TagObjetoPostal(TagBase):

    def __init__(self, numero_servico):
        self.numero_etiqueta = CampoString('numero_etiqueta', obrigatorio=True,
                                           tamanho=13)
        self.codigo_objeto_cliente = CampoString('codigo_objeto_cliente',
                                                 tamanho=20)
        self.codigo_servico_postagem = CampoString('codigo_servico_postagem',
                                                   obrigatorio=True,
                                                   tamanho=5)
        self.cubagem = CampoDecimal('cubagem')
        self.peso = CampoInteiro('peso', obrigatorio=True)
        self.rt1 = CampoString('rt1', tamanho=255)
        self.rt2 = CampoString('rt2', tamanho=255)
        self.destinatario = TagDestinatario()
        self.nacional = TagNacional(numero_servico)
        self.servico_adicional = TagServicoAdicional()
        self.dimensao_objeto = TagDimesaoObjeto()
        self.data_postagem_sara = CampoString('data_postagem_sara')
        self.status_processamento = CampoString('status_processamento',
                                                tamanho=1)
        self.numero_comprovante_postagem = \
            CampoInteiro('numero_comprovante_postagem')
        self.valor_cobrado = CampoDecimal('valor_cobrado')

    def get_xml(self):
        xml = '<objeto_postal>'
        xml += self.numero_etiqueta.get_xml()
        xml += self.codigo_objeto_cliente.get_xml()
        xml += self.codigo_servico_postagem.get_xml()
        xml += self.cubagem.get_xml()
        xml += self.peso.get_xml()
        xml += self.rt1.get_xml()
        xml += self.rt2.get_xml()
        xml += self.destinatario.get_xml()
        xml += self.nacional.get_xml()
        xml += self.servico_adicional.get_xml()
        xml += self.dimensao_objeto.get_xml()
        xml += self.data_postagem_sara.get_xml()
        xml += self.status_processamento.get_xml()
        xml += self.numero_comprovante_postagem.get_xml()
        xml += self.valor_cobrado.get_xml()
        xml += '</objeto_postal>'
        return xml


class TagDestinatario(TagBase):

    def __init__(self):
        super(TagDestinatario, self).__init__()
        self.nome = CampoUnicode('nome_destinatario', obrigatorio=True,
                                 tamanho=50)
        self.telefone = CampoString('telefone_destinatario', tamanho=12,
                                    valor='')
        self.celular = CampoString('celular_destinatario', tamanho=12,
                                   valor='')
        self.email = CampoString('email_destinatario', tamanho=50, valor='')
        self.logradouro = CampoUnicode('logradouro_destinatario',
                                       obrigatorio=True, tamanho=50)
        self.numero = CampoString('numero_end_destinatario', obrigatorio=True,
                                  tamanho=5)
        self.complemento = CampoUnicode('complemento_destinatario',
                                        tamanho=30, valor='')

    def get_xml(self):

        xml = '<destinatario>'
        xml += self.nome.get_xml()
        xml += self.telefone.get_xml()
        xml += self.celular.get_xml()
        xml += self.email.get_xml()
        xml += self.logradouro.get_xml()
        xml += self.complemento.get_xml()
        xml += self.numero.get_xml()
        xml += '</destinatario>'

        return xml


class TagNacional(TagBase):

    def __init__(self, numero_servico):
        super(TagNacional, self).__init__()
        obrigatorio = True if numero_servico == '41068' else False

        self.bairro = CampoUnicode('bairro_destinatario', obrigatorio=True,
                                   tamanho=20)
        self.cep = CampoCEP('cep_destinatario', obrigatorio=True)
        self.cidade = CampoUnicode('cidade_destinatario', obrigatorio=True,
                                   tamanho=30)
        self.uf = CampoString('uf_destinatario', obrigatorio=True, tamanho=2)
        self.codigo_usuario_postal = CampoString('codigo_usuario_postal',
                                                 valor='', tamanho=20)
        self.centro_custo_cliente = CampoString('centro_custo_cliente',
                                                valor='', tamanho=20)
        self.numero_nfe = CampoString('numero_nota_fiscal', valor='',
                                      obrigatorio=obrigatorio)
        self.serie_nfe = CampoString('serie_nota_fiscal', valor='',
                                     obrigatorio=obrigatorio)
        self.valor_nfe = CampoDecimal('valor_nota_fiscal')
        self.natureza_nfe = CampoString('natureza_nota_fiscal', valor='',
                                        tamanho=20)
        self.descricao_objeto = CampoUnicode('descricao_objeto', valor='',
                                             tamanho=20)
        self.valor_a_cobrar = CampoDecimal('valor_a_cobrar', valor=0.00)

    def get_xml(self):
        xml = '<nacional>'
        xml += self.bairro.get_xml()
        xml += self.cidade.get_xml()
        xml += self.uf.get_xml()
        xml += self.cep.get_xml()
        xml += self.codigo_usuario_postal.get_xml()
        xml += self.centro_custo_cliente.get_xml()
        xml += self.numero_nfe.get_xml()
        xml += self.serie_nfe.get_xml()
        xml += self.valor_nfe.get_xml()
        xml += self.natureza_nfe.get_xml()
        xml += self.descricao_objeto.get_xml()
        xml += self.valor_a_cobrar.get_xml()
        xml += '</nacional>'
        return xml


class TagServicoAdicional(TagBase):

    def __init__(self):
        self.lista_codigo_servico_adicional = []
        self.valor_declarado = CampoDecimal('valor_declarado',
                                            obrigatorio=True, valor=0.0)

    def add_codigo_servico_adicional(self, valor):
        self.lista_codigo_servico_adicional.append(CampoString(
            'codigo_servico_adicional', valor=valor, tamanho=3))

    def get_xml(self):
        xml = '<servico_adicional>'
        xml += '<codigo_servico_adicional>025</codigo_servico_adicional>'

        for serv_adicional in self.lista_codigo_servico_adicional:
            xml += serv_adicional.get_xml()

        xml += self.valor_declarado.get_xml()
        xml += '</servico_adicional>'
        return xml


class TagDimesaoObjeto(TagBase):

    TIPO_ENVELOPE = '001'
    TIPO_CAIXA = '002'
    TIPO_CILINDRO = '003'

    def __init__(self):
        self.tipo_objeto = TagDimensionTipoObjeto('tipo_objeto',
                                                  obrigatorio=True,
                                                  tamanho=3)

        self.altura = TagDimensionAlturaLargura('dimensao_altura', valor=2)
        self.largura = TagDimensionAlturaLargura('dimensao_largura', valor=11)
        self.comprimento = TagDimensionComprimento('dimensao_comprimento',
                                                   valor=16)
        self.diametro = TagDimensionDiametro('dimensao_diametro', valor=2)

        self.tipo_objeto.tags.append(self.altura)
        self.tipo_objeto.tags.append(self.largura)
        self.tipo_objeto.tags.append(self.comprimento)
        self.tipo_objeto.tags.append(self.diametro)

        self.tipo_objeto.valor = TagDimesaoObjeto.TIPO_CAIXA

    def get_xml(self):
        xml = '<dimensao_objeto>'
        xml += self.tipo_objeto.get_xml()
        xml += self.altura.get_xml()
        xml += self.largura.get_xml()
        xml += self.comprimento.get_xml()
        xml += self.diametro.get_xml()
        xml += '</dimensao_objeto>'
        return xml


class TagDimensionTipoObjeto(CampoString):

    def __init__(self, nome, valor=None, obrigatorio=False, tamanho=0,
                 numerico=False):

        super(TagDimensionTipoObjeto, self).__init__(nome,
                                                     valor=valor,
                                                     numerico=numerico,
                                                     obrigatorio=obrigatorio,
                                                     tamanho=tamanho)

        self.tags = []

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, val):
        val = self._formata_valor(val)
        self.update_tags(val)
        self._valor = val

    def update_tags(self, tipo_objeto):
        for tag in self.tags:
            tag.update(tipo_objeto)


class TagDimensionAlturaLargura(CampoInteiro):

    def update(self, tipo_objeto):
        self.obrigatorio = True if tipo_objeto == '002' else False


class TagDimensionComprimento(CampoInteiro):

    def update(self, tipo_objeto):
        self.obrigatorio = True if tipo_objeto != '001' else False


class TagDimensionDiametro(CampoInteiro):

    def update(self, tipo_objeto):
        self.obrigatorio = True if tipo_objeto == '003' else False
