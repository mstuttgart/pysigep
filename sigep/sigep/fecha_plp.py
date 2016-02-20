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

import xml.etree.ElementTree as Et

from sigep.base import RequestBaseAutentic
from sigep.base import ResponseBase
from sigep.campos import CampoString
from sigep.campos import CampoInteiro


class RequestFechaPLPVariosServicos(RequestBaseAutentic):

    def __init__(self, xml_plp, id_plp_cliente, num_cartao_postagem,
                 lista_etiquetas, usuario, senha):

        super(RequestFechaPLPVariosServicos, self).__init__(
            ResponseFechaPLPVariosServicos, usuario, senha)

        self._xml_plp = CampoString('xml', obrigatorio=True)
        self._id_plp_cliente = CampoInteiro('idPlpCliente',  obrigatorio=True)
        self._num_cartao_postagem = CampoString('cartaoPostagem',
                                                obrigatorio=True,
                                                tamanho=10)
        self._lista_etiquetas = []
        for etq in lista_etiquetas.split(','):
            obj_etq = CampoString('listaEtiquetas', obrigatorio=True,
                                  tamanho=12)
            obj_etq.valor = etq.valor[:10] + etq.valor[11:]
            self._lista_etiquetas.append(obj_etq)

        self._xml_plp = xml_plp
        self._id_plp_cliente = id_plp_cliente
        self._num_cartao_postagem = num_cartao_postagem

    @property
    def xml_plp(self):
        return self._xml_plp

    @property
    def id_plp_cliente(self):
        return self._id_plp_cliente

    @property
    def num_cartao_postagem(self):
        return self._num_cartao_postagem

    @property
    def lista_etiquetas(self):
        return self._lista_etiquetas

    def get_xml(self):

        xml = self.header
        xml += '<cli:fechaPlpVariosServicos>'
        xml += self.xml_plp.get_xml()
        xml += self.id_plp_cliente.get_xml()
        xml += self.num_cartao_postagem.get_xml()

        for etq in self.lista_etiquetas:
            xml += etq.get_xml()

        xml += super(RequestFechaPLPVariosServicos, self).get_xml()
        xml += '</<cli:fechaPlpVariosServicos>'
        xml += self.footer

        return xml


class ResponseFechaPLPVariosServicos(ResponseBase):

    def __init__(self):
        super(ResponseFechaPLPVariosServicos, self).__init__()
        self.plp_id = []

    def _parse_xml(self, xml):
        end = Et.fromstring(xml).find('.//return')
        self.plp_id = CampoInteiro(valor=end.text)