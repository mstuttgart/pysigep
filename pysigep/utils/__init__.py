# -*- coding: utf-8 -*-
# © 2016 Alessandro Fernandes Martini, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from jinja2 import Environment, FileSystemLoader
import unicodedata
from lxml import etree
from lxml import objectify
from builtins import str as text

HOMOLOGACAO = 1
PRODUCAO = 2

URLS = {
    HOMOLOGACAO: {
        'CalcularFretePrazo': 'http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx?WSDL',  #noqa
        'SIGEPWeb': 'https://apphom.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl',  #noqa
        'BuscaEventos': 'http://webservice.correios.com.br/service/rastro'
    },
    PRODUCAO: {
        'CalcularFretePrazo': 'http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx?WSDL',  #noqa
        'SIGEPWeb': 'https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl',  #noqa
        'BuscaEventos': 'http://webservice.correios.com.br/service/rastro'
    },
}


def render_xml(path, template_name, usuario, validation_schema=None):
    env = Environment(loader=FileSystemLoader(path),
                      extensions=['jinja2.ext.with_'])
    template = env.get_template(template_name)
    xml = template.render(usuario)
    parser = etree.XMLParser(
        remove_blank_text=True,
        remove_comments=True,
        strip_cdata=False,
        schema=validation_schema
    )
    root = etree.fromstring(xml, parser=parser)
    return etree.tostring(root)


def sanitize_response(response):
    response = text(response)
    response = unicodedata.normalize('NFKD', response).encode('ascii',
                                                              'ignore')
    tree = etree.fromstring(response)
    # Remove namespaces inuteis na resposta
    for elem in tree.getiterator():
        if not hasattr(elem.tag, 'find'):
            continue
        i = elem.tag.find('}')
        if i >= 0:
            elem.tag = elem.tag[i+1:]
    objectify.deannotate(tree, cleanup_namespaces=True)
    return response, objectify.fromstring(etree.tostring(tree))


def _valida(metodo, api, kwargs):
    if api == 'SIGEPWeb':
        ambiente_nao_obrigatorio = ['cep_consulta',
                                    'digito_verificador_etiqueta']
        if metodo not in ambiente_nao_obrigatorio and 'ambiente' not in kwargs:
            raise Exception('O ambiente é obrigatório neste método')
