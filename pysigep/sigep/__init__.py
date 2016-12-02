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
    """ Retorna a etiqueta já com o dv
    >>> digito_verificador_etiqueta('DL76023727 BR')
    'DL760237272BR'
    >>> digito_verificador_etiqueta('DL74668653 BR')
    'DL746686536BR'
    >>> digito_verificador_etiqueta('DL760237272BR')
    'DL7602372722BR'
    >>> digito_verificador_etiqueta('DL76023')
    Traceback (most recent call last):
        ...
    IndexError: string index out of range
    """
    prefixo, numero, sufixo = etiqueta[0:2], etiqueta[2:10], etiqueta[10:].strip()
    multiplicadores = [8, 6, 4, 2, 3, 5, 9, 7]
    soma = sum([int(numero[i]) * multiplicadores[i] for i in range(8)]) % 11
    dv = str(5 if not soma else 0 if soma == 1 else 11 - soma)
    numero += dv
    return prefixo + numero + sufixo


def solicita_etiquetas(**kwargs):
    """ Retorna uma lista de etiquetas, já com o digito verificador
    >>> usuario = {'usuario': 'sigep', 'senha': 'n5f9t8',\
                   'identificador': '34028316000103', 'idServico': '104625',\
                   'qtdEtiquetas': 0, }
    >>> solicita_etiquetas(**usuario)
    Traceback (most recent call last):
        ...
    AttributeError: no such child: solicitaEtiquetasResponse
    >>> usuario['qtdEtiquetas'] = 1
    >>> print len(solicita_etiquetas(**usuario)) == 1
    True
    >>> etiqueta = solicita_etiquetas(**usuario)[0]
    >>> dv = etiqueta[10]
    >>> etiqueta_sem_dv = etiqueta[:10] + ' ' + etiqueta[-2:]
    >>> print dv == digito_verificador_etiqueta(etiqueta_sem_dv)[10]
    True
    >>> print len(solicita_etiquetas(**usuario)[0]) == 13
    True
    """

    path = 'SolicitaEtiquetas.xml'
    etiquetas = send(path, 'solicitaEtiquetasResponse', 'SIGEPWeb', **kwargs)
    etiquetas = str(etiquetas)
    prefixo, sufixo = etiquetas[:2], etiquetas[-3:]
    numero_min, numero_max = int(etiquetas[2:10]), int(etiquetas[16:-3])
    diferenca = numero_max - numero_min + 1
    etiquetas_list = [prefixo + str(numero_min + i).zfill(8) + sufixo
                      for i in range(diferenca)]
    etiquetas = [digito_verificador_etiqueta(etiqueta) for etiqueta in
                 etiquetas_list]
    return etiquetas


def busca_cliente(**kwargs):
    """ Retorna o cnpj e dados do contrato do cliente
    >>> usuario = {'idContrato': '9912208555',\
                   'idCartaoPostagem': '0057018901',\
                   'usuario': 'sigep', 'senha': 'n5f9t8', }
    >>> busca_cliente(**usuario) #doctest: +ELLIPSIS
    <Element return at 0x...>
    >>> busca_cliente(**usuario).cnpj
    34028316000103
    """
    return send('BuscaCliente.xml', 'buscaClienteResponse', 
                'SIGEPWeb', **kwargs)


def verifica_disponibilidade_servico(**kwargs):
    path = 'VerificaDisponibilidadeServico.xml'
    return send(path, 'verificaDisponibilidadeServicoResponse',
                'SIGEPWeb', **kwargs)


def consulta_cep(**kwargs):
    """ Retorna um objeto com os dados do CEP
    >>> cep = {'cep': '83010140', }
    >>> consulta_cep(**cep) #doctest: +ELLIPSIS
    <Element return at 0x...>
    >>> consulta_cep(**cep).bairro
    'Cruzeiro'
    >>> consulta_cep(**cep).cep
    83010140
    """
    path = 'ConsultaCep.xml'
    return send(path, 'consultaCEPResponse', 'SIGEPWeb', **kwargs)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
