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

from sigep.base import RequestBaseSIGEPAutentic
from sigep.base import ResponseBase
from sigep.campos import CampoCNPJ
from sigep.campos import CampoString
from sigep.campos import CampoInteiro


class RequestSolicitaEtiquetaSIGEP(RequestBaseSIGEPAutentic):

    def __init__(self, cnpj, id_servico, qtd_etiquetas, usuario, senha):
        super(RequestSolicitaEtiquetaSIGEP, self).__init__(
            ResponseSolicitaEtiqueta, usuario, senha)

        self._tipo_destinatario = CampoString('tipoDestinatario',
                                              obrigatorio=True,
                                              tamanho=1)
        self._cnpj = CampoCNPJ('identificador', obrigatorio=True)
        self._id_servico = CampoInteiro('idServico', obrigatorio=True)
        self._qtd_etiquetas = CampoInteiro('qtdEtiquetas', obrigatorio=True)

        self._tipo_destinatario.valor = 'c'
        self._cnpj.valor = cnpj
        self._id_servico.valor = id_servico
        self._qtd_etiquetas.valor = qtd_etiquetas

    @property
    def tipo_destinatario(self):
        return self._tipo_destinatario

    @property
    def cnpj(self):
        return self._cnpj

    @property
    def id_servico(self):
        return self._id_servico

    @property
    def qtd_etiquetas(self):
        return self._qtd_etiquetas

    def get_xml(self):

        xml = self.header
        xml += '<cli:solicitaEtiquetas>'
        xml += self.tipo_destinatario.get_xml()
        xml += self.cnpj.get_xml()
        xml += self.id_servico.get_xml()
        xml += self.qtd_etiquetas.get_xml()
        xml += super(RequestSolicitaEtiquetaSIGEP, self).get_xml()
        xml += '</<cli:solicitaEtiquetas>'
        xml += self.footer

        return xml


class ResponseSolicitaEtiqueta(ResponseBase):

    def __init__(self):
        super(ResponseSolicitaEtiqueta, self).__init__()
        self.intervalo_etiquetas = CampoString('intervalo_etiquetas',
                                               obrigatorio=True)

    def _parse_xml(self, xml):
        end = Et.fromstring(xml).find('.//return')
        self.intervalo_etiquetas.valor = end.text
