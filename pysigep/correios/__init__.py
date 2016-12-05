# -*- coding: utf-8 -*-
# © 2016 Alessandro Fernandes Martini, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from pysigep import send


def calcular_preco_prazo(**kwargs):
    """
    >>> request = {'nCdEmpresa': '08082650', 'sDsSenha': 'n5f9t8',\
        'nCdServico': '40215', 'sCepOrigem': '05311900',\
        'sCepDestino': '83010140', 'nVlPeso': 1, 'nCdFormato': 1,\
        'nVlComprimento': 20, 'nVlAltura': 20, 'nVlLargura': 20,\
        'nVlDiametro': 20, 'sCdMaoPropria': 'S',\
        'nVlValorDeclarado': 0, 'sCdAvisoRecebimento': 'S'}
    >>> calcular_preco_prazo(**request).cServico.Codigo
    40215
    >>> (calcular_preco_prazo(**request).cServico.ValorMaoPropria) > 0
    True
    >>> request['nVlPeso'] = 99999999999999
    >>> calcular_preco_prazo(**request)  #doctest: +ELLIPSIS
    <Element Servicos at 0x...>
    >>> request['nVlPeso'] = 0
    >>> calcular_preco_prazo(**request)  #doctest: +ELLIPSIS
    <Element Servicos at 0x...>
    >>> request['sCepDestino'] = '12345678'
    >>> calcular_preco_prazo(**request).cServico.Erro
    8
    """
    path = 'CalcularPrecoPrazo.xml'
    return send(path, 'CalcPrecoPrazoResponse', 'CalcularFretePrazo',
                soap_action='http://tempuri.org/CalcPrecoPrazo', **kwargs)


def get_eventos(**kwargs):
    """
    >>> user = {'usuario': 'ECT', 'senha': 'SRO',\
                'objetos': ['PL207893158BR']}
    >>> get_eventos(**user) #doctest: +ELLIPSIS
    <Element return at 0x...>
    >>> get_eventos(**user).objeto.evento.destino.cidade
    'Rio De Janeiro'
    """
    path = 'BuscaEventos.xml'
    return send(path, 'buscaEventosListaResponse', 'BuscaEventos',
                soap_action='eventos', **kwargs)
