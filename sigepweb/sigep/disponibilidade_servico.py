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

from sigepweb.base import RequestBaseSIGEPAuthentication
from sigepweb.base import ResponseBase
from sigepweb.campos import CampoString
from sigepweb.campos import CampoCEP


class RequestDisponibilidadeServico(RequestBaseSIGEPAuthentication):

    def __init__(self, cod_administrativo, numero_servico, cep_origem,
                 cep_destino, usuario, senha):

        super(RequestDisponibilidadeServico, self).__init__(
            ResponseDisponibilidadeServico, usuario, senha)

        self.cod_administrativo = CampoString('codAdministrativo',
                                              obrigatorio=True,
                                              valor=cod_administrativo,
                                              tamanho=8)
        self.numero_servico = CampoString('numeroServico',
                                          valor=numero_servico,
                                          obrigatorio=True,
                                          numerico=True)
        self.cep_origem = CampoCEP('cepOrigem', valor=cep_origem,
                                   obrigatorio=True)
        self.cep_destino = CampoCEP('cepDestino', valor=cep_destino,
                                    obrigatorio=True)

    def get_data(self):

        xml = RequestBaseSIGEPAuthentication.HEADER
        xml += '<cli:verificaDisponibilidadeServico>'
        xml += self.cod_administrativo.get_xml()
        xml += self.numero_servico.get_xml()
        xml += self.cep_origem.get_xml()
        xml += self.cep_destino.get_xml()
        xml += super(RequestDisponibilidadeServico, self).get_data()
        xml += '</cli:verificaDisponibilidadeServico>'
        xml += RequestBaseSIGEPAuthentication.FOOTER

        return xml


class ResponseDisponibilidadeServico(ResponseBase):

    def __init__(self):
        super(ResponseDisponibilidadeServico, self).__init__()

    def _parse_xml(self, xml):
        for end in Et.fromstring(xml).findall('.//return'):
            self.resposta = {
                'disponibilidade': True if end.text == 'true' else False,
            }
