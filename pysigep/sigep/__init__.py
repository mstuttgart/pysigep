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

from pysigep import send


def digito_verificador_etiqueta(etiqueta):
    prefixo, numero, sufixo = etiqueta[0:2], etiqueta[2:10], etiqueta[10:].strip()
    multiplicadores = [8, 6, 4, 2, 3, 5, 9, 7]
    soma = sum([int(numero[i]) * multiplicadores[i] for i in range(8)]) % 11
    dv = str(5 if not soma else 0 if soma == 1 else 11 - soma)
    numero += dv
    return prefixo + numero + sufixo


def solicita_etiquetas(**kwargs):
    path = 'SolicitaEtiquetas.xml'
    etiquetas = send(path, 'solicitaEtiquetasResponse', 'SIGEPWeb', **kwargs)
    etiquetas = str(etiquetas)
    prefixo, sufixo = etiquetas[:2], etiquetas[-3:]
    print int(etiquetas[2:10]), int(etiquetas[16:-3])
    numero_min, numero_max = int(etiquetas[2:10]), int(etiquetas[16:-3])
    diferenca = numero_max - numero_min + 1
    etiquetas_list = [prefixo + str(numero_min + i).zfill(8) + sufixo
                      for i in range(diferenca)]
    etiquetas = [digito_verificador_etiqueta(etiqueta) for etiqueta in
                 etiquetas_list]
    return etiquetas


def busca_cliente(**kwargs):
    return send('BuscaCliente.xml', 'buscaClienteResponse', 
                'SIGEPWeb', **kwargs)


def verifica_disponibilidade_servico(**kwargs):
    path = 'VerificaDisponibilidadeServico.xml'
    return send(path, 'verificaDisponibilidadeServicoResponse',
                'SIGEPWeb', **kwargs)


def consulta_cep(**kwargs):
    path = 'ConsultaCep.xml'
    return send(path, 'consultaCEPResponse', 'SIGEPWeb', **kwargs)
