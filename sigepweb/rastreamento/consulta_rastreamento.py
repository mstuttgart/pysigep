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

import xml.etree.cElementTree as Et

from sigepweb.base import RequestBaseRastreamento
from sigepweb.base import ResponseBase
from sigepweb.campos import CampoString


class RequestRastreamento(RequestBaseRastreamento):

    TIPO_LISTA_DE_OBJETOS = 'L'
    TIPO_INTERVALO_DE_OBJETOS = 'F'
    TODOS_RESULTADOS = 'T'
    ULTIMO_RESULTADO = 'U'

    def __init__(self, usuario, senha, tipo, resultado, lista_etiquetas):
        super(RequestRastreamento, self).__init__(ResponseRastreamento)

        self.usuario = CampoString('Usuario', obrigatorio=True, valor=usuario)
        self.senha = CampoString('Senha', obrigatorio=True, valor=senha)
        self.tipo = CampoString('Tipo', obrigatorio=True, valor=tipo,
                                tamanho=1)
        self.resultado = CampoString('Resultado', obrigatorio=True, tamanho=1,
                                     valor=resultado)

        aux = ''
        for etq in lista_etiquetas:
            aux += etq

        self.objetos = CampoString('Objetos', obrigatorio=True, valor=aux)

    def get_data(self):

        data = {
            self.usuario.nome: self.usuario.valor,
            self.senha.nome: self.senha.valor,
            self.tipo.nome: self.tipo.valor,
            self.resultado.nome: self.resultado.valor,
            self.objetos.nome: self.objetos.valor,
        }

        return data


class ResponseRastreamento(ResponseBase):

    def __init__(self):
        super(ResponseRastreamento, self).__init__()

    def _parse_xml(self, xml):

        # Necessario pois o decode do rastreamento é diferente
        xml = xml.decode('utf8').encode('iso-8859-1')

        self.resposta = {}
        for end in Et.fromstring(xml).findall('.'):
            self.resposta['versao'] = end.findtext('versao')
            self.resposta['qtd'] = end.findtext('qtd')
            self.resposta['tipo_pesquisa'] = end.findtext('TipoPesquisa')
            self.resposta['tipo_resultado'] = end.findtext('TipoResultado')

            self.resposta['objetos'] = {}

            for obj in end.findall('objeto'):
                self.resposta['objetos'][obj.findtext('numero')] = []

                for evento in obj.findall('evento'):
                    ev = {
                        'tipo': evento.findtext('tipo'),
                        'status': evento.findtext('status'),
                        'data': evento.findtext('data'),
                        'hora': evento.findtext('hora'),
                        'descricao': evento.findtext('descricao').rstrip(),
                        'recebedor': evento.findtext('recebedor').rstrip(),
                        'documento': evento.findtext('documento').rstrip(),
                        'comentario': evento.findtext('comentario').rstrip(),
                        'local': evento.findtext('local'),
                        'codigo': evento.findtext('codigo'),
                        'cidade': evento.findtext('cidade'),
                        'uf': evento.findtext('uf'),
                    }

                    self.resposta['objetos'][obj.findtext('numero')].append(ev)
