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

from pysigep.base import RequestBaseSIGEPAuthentication
from pysigep.base import ResponseBase
from pysigep.campos import CampoCNPJ
from pysigep.campos import CampoString
from pysigep.campos import CampoInteiro


class RequestSolicitaEtiquetaSIGEP(RequestBaseSIGEPAuthentication):

    def __init__(self, cnpj, id_servico, qtd_etiquetas, usuario, senha):
        super(RequestSolicitaEtiquetaSIGEP, self).__init__(
            ResponseSolicitaEtiqueta, usuario, senha)

        self.tipo_destinatario = CampoString('tipoDestinatario', valor='c',
                                             obrigatorio=True, tamanho=1)
        self.cnpj = CampoCNPJ('identificador', valor=cnpj, obrigatorio=True)
        self.id_servico = CampoInteiro('idServico', valor=id_servico,
                                       obrigatorio=True)
        self.qtd_etiquetas = CampoInteiro('qtdEtiquetas', valor=qtd_etiquetas,
                                          obrigatorio=True)

    def get_data(self):
        xml = RequestBaseSIGEPAuthentication.HEADER
        xml += '<cli:solicitaEtiquetas>'
        xml += self.tipo_destinatario.get_xml()
        xml += self.cnpj.get_xml()
        xml += self.id_servico.get_xml()
        xml += self.qtd_etiquetas.get_xml()
        xml += super(RequestSolicitaEtiquetaSIGEP, self).get_data()
        xml += '</<cli:solicitaEtiquetas>'
        xml += RequestBaseSIGEPAuthentication.FOOTER
        return xml


class ResponseSolicitaEtiqueta(ResponseBase):

    def __init__(self):
        super(ResponseSolicitaEtiqueta, self).__init__()

    def _parse_xml(self, xml):
        for end in Et.fromstring(xml).findall('.//return'):
            self.resposta = {
                'lista_etiquetas': [etq for etq in end.text.split(',')],
            }
