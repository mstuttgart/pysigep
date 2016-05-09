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

from sigepweb.base import RequestBaseSIGEPAuthentication
from sigepweb.base import ResponseBase
from sigepweb.campos import CampoString
from sigepweb.campos import CampoInteiro


class RequestFechaPLPVariosServicos(RequestBaseSIGEPAuthentication):

    def __init__(self, xml_plp, id_plp_cliente, num_cartao_postagem,
                 etiquetas, usuario, senha):

        super(RequestFechaPLPVariosServicos, self).__init__(
            ResponseFechaPLPVariosServicos, usuario, senha)

        self.xml_plp = CampoString('xml', valor=xml_plp, obrigatorio=True)
        self.id_plp_cliente = CampoInteiro('idPlpCliente',
                                           valor=id_plp_cliente,
                                           obrigatorio=True)
        self.num_cartao_postagem = CampoString('cartaoPostagem',
                                               obrigatorio=True,
                                               valor=num_cartao_postagem,
                                               tamanho=10)
        self.lista_etiquetas = []
        for etq in etiquetas:
            obj_etq = CampoString('listaEtiquetas',
                                  valor=etq[:10] + etq[11:],
                                  obrigatorio=True,
                                  tamanho=12)
            self.lista_etiquetas.append(obj_etq)

    def get_data(self):
        xml = RequestBaseSIGEPAuthentication.HEADER
        xml += '<cli:fechaPlpVariosServicos>'
        xml += self.xml_plp.get_xml()
        xml += self.id_plp_cliente.get_xml()
        xml += self.num_cartao_postagem.get_xml()

        for etq in self.lista_etiquetas:
            xml += etq.get_xml()

        xml += super(RequestFechaPLPVariosServicos, self).get_data()
        xml += '</cli:fechaPlpVariosServicos>'
        xml += RequestBaseSIGEPAuthentication.FOOTER
        return xml


class ResponseFechaPLPVariosServicos(ResponseBase):

    def __init__(self):
        super(ResponseFechaPLPVariosServicos, self).__init__()

    def _parse_xml(self, xml):
        for end in Et.fromstring(xml).findall('.//return'):
            self.resposta = {
                'id_plp': end.text,
            }
