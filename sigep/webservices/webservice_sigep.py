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

from webservice_base import WebserviceBase


class WebserviceSIGEP(WebserviceBase):
    AMBIENTE_PRODUCAO = 'PRODUCAO'
    AMBIENTE_HOMOLOGACAO = 'HOMOLOGACAO'

    def __init__(self, ambiente):

        amb = {
            WebserviceSIGEP.AMBIENTE_HOMOLOGACAO:
                'https://apphom.correios.com.br/SigepMasterJPA/'
                'AtendeClienteService/AtendeCliente?wsdl',

            WebserviceSIGEP.AMBIENTE_PRODUCAO:
                'https://apps.correios.com.br/SigepMasterJPA/'
                'AtendeClienteService/AtendeCliente?wsdl'
        }

        try:
            super(WebserviceSIGEP, self).__init__(amb[ambiente])
        except KeyError as exp:
            print exp.message
            super(WebserviceSIGEP, self).__init__(
                amb[WebserviceSIGEP.AMBIENTE_HOMOLOGACAO])
            ambiente = WebserviceSIGEP.AMBIENTE_HOMOLOGACAO

        self.ambiente = ambiente
