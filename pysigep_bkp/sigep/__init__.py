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

import os

from lxml import etree
from pysigep import send, _url
from pysigep.utils import render_xml, _valida

API = 'SIGEPWeb'


def digito_verificador_etiqueta(etiqueta):
    """ Retorna a etiqueta já com o dv
    :param:
        etiqueta -> string, i.e.: 'DL76023727 BR'
    :return:
        etiqueta com o dv -> string, i.e.: 'DL760237272BR'
    """
    _valida('digito_verificador_etiqueta', API, etiqueta)
    prefixo, numero, sufixo = etiqueta[0:2], etiqueta[2:10], etiqueta[10:].strip()
    multiplicadores = [8, 6, 4, 2, 3, 5, 9, 7]
    soma = sum([int(numero[i]) * multiplicadores[i] for i in range(8)]) % 11
    dv = str(5 if not soma else 0 if soma == 1 else 11 - soma)
    numero += dv
    return prefixo + numero + sufixo


def solicita_etiquetas_com_dv(**kwargs):
    """ Retorna uma lista de etiquetas, já com o digito verificador

    :params:
        kwargs: {'usuario': 'sigep', 'senha': 'n5f978',
                 'identificador': '34028316000103',
                 'idServico': '104625', 'qtdEtiquetas': '10'}
    :return:
        lista com as etiquetas já com o digito verificador.
    """

    _valida('solicita_etiquetas_com_dv', API, kwargs)
    url = _url(kwargs['ambiente'], API)
    path = 'SolicitaEtiquetas.xml'
    etiquetas = send(path, 'solicitaEtiquetasResponse', API, url, **kwargs)
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
    """Retorna um objeto xml a partir da resposta dos Correios

    :params:
        kwargs: {'idContrato': '1234567890', 'idCartaoPostagem': '1234567890',
                 'usuario': 'usuario', 'senha': 'senha'}
    :return:
        objeto xml com os campos: cnpj, e contratos (objeto contendo informações dos
        contratos do cliente.
        No caso de erro retorna um dict {'mensagem_erro': 'mensagem do erro'}
    """
    _valida('busca_cliente', API, kwargs)
    url = _url(kwargs['ambiente'], API)
    return send('BuscaCliente.xml', 'buscaClienteResponse',
                API, url, **kwargs)


def verifica_disponibilidade_servico(**kwargs):
    """Retorna um booleano, informando se o serviço esta ou não disponível

    :params:
        kwargs: {'codAdministrativo': '12345678',
                 'numeroServico': '40215,81019', 'cepOrigem': '12345678',
                 'cepDestino': '12345678', 'usuario': 'usuario',
                 'senha': 'senha'}
    :return:
        Boolean ou dict {'mensagem_erro': 'mensagem do erro'}
    """
    _valida('verifica_disponibilidade_servico', API, kwargs)
    url = _url(kwargs['ambiente'], API)
    path = 'VerificaDisponibilidadeServico.xml'
    return send(path, 'verificaDisponibilidadeServicoResponse',
                API, url, **kwargs)


def cep_consulta(**kwargs):
    """Retorna um objeto xml a partir da resposta dos Correios

    :params:
        kwargs: {'cep': '12345678'}
    :return:
        objeto xml com os campos: bairro, cep, cidade, complemento,
        complemento2, end, id, uf.
        No caso de erro retorna um dict {'mensagem_erro': 'mensagem do erro'}
    """
    _valida('cep_consulta', API, kwargs)
    ambiente = kwargs['ambiente'] if 'ambiente' in kwargs else 1
    url = _url(ambiente, API)
    path = 'ConsultaCep.xml'
    return send(path, 'consultaCEPResponse', API, url, **kwargs)


def fecha_plp_servicos_validation_schema():
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    validation_file = open(os.path.join(BASE_DIR, 'correios/data/layout.xsd'))
    schema_root = etree.XML(validation_file.read())
    return etree.XMLSchema(schema_root)


def fecha_plp_servicos(**kwargs):
    _valida('fecha_plp_servicos', API, kwargs)
    url = _url(kwargs['ambiente'], API)
    path = 'FechaPlpVariosServicos.xml'
    path = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(path, 'templates')
    xml = render_xml(
        path, "PLP.xml", kwargs,
        validation_schema=fecha_plp_servicos_validation_schema()
    )
    kwargs["xml"] = '<?xml version="1.0" encoding="ISO-8859-1" ?>' + xml
    return send("FechaPlpVariosServicos.xml", 'fechaPlpVariosServicosResponse',
                API, url, encoding="ISO-8859-1", **kwargs)


def solicita_xml_plp(**kwargs):
    _valida('solicita_xml_plp', API, kwargs)
    url = _url(kwargs['ambiente'], API)
    path = 'SolicitaXmlPlp.xml'
    return send(path, 'solicitaXmlPlpResponse', API, url, **kwargs)
