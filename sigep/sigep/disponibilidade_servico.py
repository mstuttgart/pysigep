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
from sigep.campos import CampoString
from sigep.campos import CampoCEP
from sigep.campos import CampoBooleano


class RequestDisponibilidadeServico(RequestBaseSIGEPAutentic):

    def __init__(self, cod_administrativo, numero_servico, cep_origem,
                 cep_destino, usuario, senha):

        super(RequestDisponibilidadeServico, self).__init__(
            ResponseDisponibilidadeServico, usuario, senha)

        self.cod_administrativo = CampoString('codAdministrativo',
                                              obrigatorio=True,
                                              tamanho=8)
        self.numero_servico = CampoString('numeroServico',
                                          obrigatorio=True,
                                          numerico=True)
        self.cep_origem = CampoCEP('cepOrigem', obrigatorio=True)
        self.cep_destino = CampoCEP('cepDestino', obrigatorio=True)

        self.cod_administrativo.valor = cod_administrativo
        self.numero_servico.valor = numero_servico
        self.cep_origem.valor = cep_origem
        self.cep_destino.valor = cep_destino

    def get_xml(self):

        xml = self.header
        xml += '<cli:verificaDisponibilidadeServico>'
        xml += self.cod_administrativo.get_xml()
        xml += self.numero_servico.get_xml()
        xml += self.cep_origem.get_xml()
        xml += self.cep_destino.get_xml()
        xml += super(RequestDisponibilidadeServico, self).get_xml()
        xml += '</cli:verificaDisponibilidadeServico>'
        xml += self.footer

        return xml


class ResponseDisponibilidadeServico(ResponseBase):

    def __init__(self):
        super(ResponseDisponibilidadeServico, self).__init__()
        self.disponivel = CampoBooleano('disponivel', obrigatorio=True)

    def _parse_xml(self, xml):
        end = Et.fromstring(xml).find('.//return')
        self.disponivel.valor = True if end.text == 'true' else False
