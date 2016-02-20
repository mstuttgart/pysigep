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

from sigep.base import TagBase
from sigep.campos import CampoCEP
from sigep.campos import CampoString
from sigep.campos import CampoInteiro
from sigep.campos import CampoDecimal


class XmlPLP(TagBase):
    def __init__(self):
        self._forma_pagamento = CampoString(valor='')
        self.plp = TagPLP()
        self.remetente = TagRemetente()
        self.lista_objeto_postal = []

    @property
    def forma_pagamento(self):
        return self._forma_pagamento

    def get_xml(self):
        xml = '<?xml version=\"1.0\" encoding=\"ISO-8859-1\" ?>'
        xml += '<correioslog>'
        xml += '<tipo_arquivo>Postagem</tipo_arquivo>'
        xml += '<versao_arquivo>2.3</versao_arquivo>'
        xml += self.plp.get_xml()
        xml += self.remetente.get_xml()

        for obj_post in self.lista_objeto_postal:
            xml += obj_post.get_xml()

        xml += '</correioslog>'


class TagPLP(TagBase):
    def __init__(self):
        super(TagPLP, self).__init__()
        self._cartao_postagem = CampoString('cartao_postagem',
                                            obrigatorio=True,
                                            tamanho=10)

    @property
    def cartao_postagem(self):
        return self._cartao_postagem

    def get_xml(self):
        xml = '<plp>'
        xml += '<id_plp/>'
        xml += '<valor_global/>'
        xml += '<mcu_unidade_postagem/>'
        xml += '<nome_unidade_postagem/>'
        xml += self.cartao_postagem.get_xml()
        xml += '</plp>'


class TagRemetente(TagBase):
    def __init__(self):
        super(TagRemetente, self).__init__()
        self._numero_contrato = CampoString('numero_contrato',
                                            obrigatorio=True, tamanho=10)
        self._numero_diretoria = CampoInteiro('numero_diretoria',
                                              obrigatorio=True)
        self._codigo_administrativo = CampoString('codigo_administrativo',
                                                  obrigatorio=True, tamanho=8)
        self._nome = CampoString('nome_remetente', obrigatorio=True, tamanho=50)
        self._logradouro = CampoString('logradouro_remetente',
                                       obrigatorio=True, tamanho=40)
        self._numero = CampoString('numero_remetente',
                                   obrigatorio=True, tamanho=5)
        self._complemento = CampoString('complemento_remetente',
                                        obrigatorio=False,
                                        tamanho=20)
        self._bairro = CampoString('bairro_remetente', obrigatorio=True,
                                   tamanho=20)
        self._cep = CampoCEP('cep_remetente', obrigatorio=True)
        self._cidade = CampoString('cidade_remetente',
                                   obrigatorio=True, tamanho=30)
        self._uf = CampoString('uf_remetente', obrigatorio=True, tamanho=2)
        self._telefone = CampoString('telefone_remetente',
                                     obrigatorio=False, tamanho=12)
        self._fax = CampoString('fax_remetente', obrigatorio=False, tamanho=12)
        self._email = CampoString('email_remetente', obrigatorio=False,
                                  tamanho=50)

    @property
    def numero_contrato(self):
        return self._numero_contrato

    @property
    def numero_diretoria(self):
        return self._numero_diretoria

    @property
    def codigo_administrativo(self):
        return self._codigo_administrativo

    @property
    def nome(self):
        return self._nome

    @property
    def logradouro(self):
        return self._logradouro

    @property
    def numero(self):
        return self._numero

    @property
    def complemento(self):
        return self._complemento

    @property
    def bairro(self):
        return self._bairro

    @property
    def cep(self):
        return self._cep

    @property
    def cidade(self):
        return self._cidade

    @property
    def uf(self):
        return self._uf

    @property
    def telefone(self):
        return self._telefone

    @property
    def fax(self):
        return self._fax

    @property
    def email(self):
        return self._email

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

    def __init__(self, numero_servico, tipo_objeto):
        self._numero_etiqueta = CampoString('numero_etiqueta', obrigatorio=True,
                                            tamanho=13)
        self._codigo_objeto_cliente = CampoString('codigo_objeto_cliente',
                                                  tamanho=20)
        self._codigo_servico_postagem = CampoString('codigo_servico_postagem',
                                                    obrigatorio=True,
                                                    tamanho=5)
        self._cubagem = CampoDecimal('cubagem')
        self._peso = CampoInteiro('peso', obrigatorio=True)
        self._rt1 = CampoString('rt1', tamanho=255)
        self._rt2 = CampoString('rt2', tamanho=255)
        self._destinatario = TagDestinatario()
        self._nacional = TagNacional(numero_servico)
        self._servico_adicional = TagServicoAdcional()
        self._dimensao_objeto = TagDimesaoObjeto()
        self._data_postagem_sara = CampoString('data_postagem_sara')
        self._status_processamento = CampoString('status_processamento',
                                                 tamanho=1)
        self._numero_comprovante_postagem = \
            CampoInteiro('numero_comprovante_postagem')
        self._valor_cobrado = CampoDecimal('valor_cobrado')

    @property
    def numero_etiqueta(self):
        return self._numero_etiqueta

    @property
    def codigo_objeto_cliente(self):
        return self._codigo_objeto_cliente

    @property
    def codigo_servico_postagem(self):
        return self._codigo_servico_postagem

    @property
    def cubagem(self):
        return self._cubagem

    @property
    def peso(self):
        return self._peso

    @property
    def rt1(self):
        return self._rt1

    @property
    def rt2(self):
        return self._rt2

    @property
    def destinatario(self):
        return self._destinatario

    @property
    def nacional(self):
        return self._nacional

    @property
    def servico_adicional(self):
        return self._servico_adicional

    @property
    def dimensao_objeto(self):
        return self._dimensao_objeto

    @property
    def data_postagem_sara(self):
        return self._data_postagem_sara

    @property
    def status_processamento(self):
        return self._status_processamento

    @property
    def numero_comprovante_postagem(self):
        return self._numero_comprovante_postagem

    @property
    def valor_cobrado(self):
        return self._valor_cobrado

    def get_xml(self):

        xml = u'<objeto_postal>'
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
        xml += u'</objeto_postal>'

        return xml


class TagDestinatario(TagBase):

    def __init__(self):
        super(TagRemetente, self).__init__()
        self._nome = CampoString('nome_destinatario', obrigatorio=True,
                                 tamanho=50)
        self._telefone = CampoString('telefone_destinatario', tamanho=12)
        self._celular = CampoString('celular_destinatario', tamanho=12)
        self._email = CampoString('email_destinatario', tamanho=50)
        self._logradouro = CampoString('logradouro_destinatario',
                                       obrigatorio=True, tamanho=50)
        self._numero = CampoString('numero_end_destinatario', obrigatorio=True,
                                   tamanho=5)
        self._complemento = CampoString('complemento_destinatario', tamanho=30)

    @property
    def nome(self):
        return self._nome

    @property
    def logradouro(self):
        return self._logradouro

    @property
    def numero(self):
        return self._numero

    @property
    def complemento(self):
        return self._complemento

    @property
    def telefone(self):
        return self._telefone

    @property
    def celular(self):
        return self._celular

    @property
    def email(self):
        return self._email

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

        obrigatorio = True if numero_servico == '41068' else False

        self._bairro = CampoString(obrigatorio=True, tamanho=20)
        self._cep = CampoCEP(obrigatorio=True)
        self._cidade = CampoString(obrigatorio=True, tamanho=30)
        self._uf = CampoString(obrigatorio=True, tamanho=2)
        self._codigo_usuario_postal = CampoString(valor='', tamanho=20)
        self._centro_custo_cliente = CampoString(valor='', tamanho=20)
        self._numero_nfe = CampoString(valor='', obrigatorio=obrigatorio)
        self._serie_nfe = CampoString(valor='', obrigatorio=obrigatorio)
        self._valor_nfe = CampoDecimal(minimo=0, maximo=999999999)
        self._natureza_nfe = CampoString(valor='', tamanho=20)
        self._descricao_objeto = CampoString(valor='', tamanho=20)
        self._valor_a_cobrar = CampoDecimal(minimo=0, maximo=999999999)

    def set_numero_servico(self, numero_servico):
        obrigatorio = True if numero_servico == '41068' else False
        self._numero_nfe.obrigatorio = obrigatorio
        self._serie_nfe.obrigatorio = obrigatorio

    @property
    def bairro(self):
        return self._bairro

    @property
    def cep(self):
        return self._cep

    @property
    def cidade(self):
        return self._cidade

    @property
    def uf(self):
        return self._uf

    @property
    def codigo_usuario_postal(self):
        return self._codigo_usuario_postal

    @property
    def centro_custo_cliente(self):
        return self._centro_custo_cliente

    @property
    def numero_nfe(self):
        return self._numero_nfe

    @property
    def serie_nfe(self):
        return self._serie_nfe

    @property
    def valor_nfe(self):
        return self._valor_nfe

    @property
    def natureza_nfe(self):
        return self._natureza_nfe

    @property
    def descricao_objeto(self):
        return self._descricao_objeto

    @property
    def valor_a_cobrar(self):
        return self._valor_a_cobrar

    def get_xml(self):
        xml = u'<nacional>'

        xml += u'<bairro_destinatario><![CDATA[%s]]></bairro_destinatario>' % \
               self.bairro.valor
        xml += u'<cidade_destinatario><![CDATA[%s]]></cidade_destinatario>' % \
               self.cidade.valor
        xml += u'<uf_destinatario>%s</uf_destinatario>' % self.uf.valor
        xml += u'<cep_destinatario><![CDATA[%s]]></cep_destinatario>' % \
               self.cep.valor
        xml += u'<codigo_usuario_postal>%s</codigo_usuario_postal>' % \
               self.codigo_usuario_postal.valor
        xml += u'<centro_custo_cliente>%s</centro_custo_cliente>' % \
               self.centro_custo_cliente.valor
        xml += u'<numero_nota_fiscal>%s</numero_nota_fiscal>' % \
               self.numero_nfe.valor
        xml += u'<serie_nota_fiscal>%s</serie_nota_fiscal>' % \
               self.serie_nfe.valor
        xml += u'<valor_nota_fiscal>%1.2%f</valor_nota_fiscal>' % \
               self.valor_nfe.valor
        xml += u'<natureza_nota_fiscal><![CDATA[%s]]></natureza_nota_fiscal>' % \
               self.natureza_nfe.valor
        xml += u'<descricao_objeto><![CDATA[%s]]></descricao_objeto>' % \
               self.descricao_objeto.valor
        xml += u'<valor_a_cobrar>1.2%f</valor_a_cobrar>' % \
               self.valor_a_cobrar.valor
        xml += u'</nacional>'

        return xml


class TagServicoAdcional(TagBase):

    def __init__(self):

        self._lista_codigo_servico_adicional = [
            CampoString('codigo_servico_adicional', valor='025', tamanho=3)]

        self._valor_declarado = CampoDecimal('valor_declarado', minimo=0,
                                             maximo=999999999)

    @property
    def lista_codigo_servico_adicional(self):
        return self._lista_codigo_servico_adicional

    def add_codigo_servico_adicional(self, valor):
        self._codigo_servico_adicional.append(CampoString(
            valor=valor, tamanho=3))

        self._valor_declarado.obrigatorio = True if valor == '019' else False

    @property
    def valor_declarado(self):
        return self._valor_declarado

    def get_xml(self):

        xml = u'<servico_adicional>'
        for serv_adic in self._codigo_servico_adicional:
            xml += serv_adic.get_xml()
        xml += self.valor_declarado.get_xml()
        xml += u'</servico_adicional>'

        return xml


class TagDimesaoObjeto(TagBase):
    TIPO_ENVELOPE = '001'
    TIPO_CAIXA = '002'
    TIPO_CILINDRO = '003'

    def __init__(self):
        tipo_objeto = TagDimesaoObjeto.TIPO_CAIXA
        self.tipo_objeto = CampoString(obrigatorio=True, valor=tipo_objeto,
                                       tamanho=3)
        self._altura = CampoInteiro(obrigatorio=True if tipo_objeto == '002'
        else False, valor=2, minimo=2, maximo=105)
        self._largura = CampoInteiro(obrigatorio=True if tipo_objeto == '002'
        else False, valor=11, minimo=11, maximo=105)
        self._comprimento = CampoInteiro(
            obrigatorio=True if tipo_objeto != '001'
            else False, valor=16, minimo=16, maximo=105)
        self._diametro = CampoInteiro(obrigatorio=True if tipo_objeto == '003'
        else False, valor=2, minimo=2, maximo=105)

    def set_tipo_objeto(self, tipo_objeto):
        self._altura.obrigatorio = True if tipo_objeto == '002' else False
        self._largura.obrigatorio = True if tipo_objeto == '002' else False
        self._comprimento.obrigatorio = True if tipo_objeto != '001' else False
        self._diametro.obrigatorio = True if tipo_objeto == '003' else False

        self._comprimento.minimo = 16 if tipo_objeto != '003' else 18

    @property
    def tipo_objeto(self):
        return self.tipo_objeto

    @property
    def altura(self):
        return self._altura

    @property
    def largura(self):
        return self._largura

    @property
    def comprimento(self):
        return self._comprimento

    @property
    def diametro(self):
        return self._diametro

    def get_xml(self):
        xml = u'<dimensao_objeto>\n'
        xml += u'<tipo_objeto>%s</tipo_objeto>\n' % self.codigo.valor
        xml += u'<dimensao_altura>%d</dimensao_altura>\n' % self.altura.valor
        xml += u'<dimensao_largura>%d</dimensao_largura>\n' % self.largura.valor
        xml += u'<dimensao_comprimento>%d</dimensao_comprimento>\n' % \
               self.comprimento.valor
        xml += u'<dimensao_diametro>%d</dimensao_diametro>\n' % self.diametro.valor
        xml += u'</dimensao_objeto>\n'

        return xml
