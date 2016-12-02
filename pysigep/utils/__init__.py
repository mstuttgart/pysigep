# -*- coding: utf-8 -*-
# © 2016 Alessandro Fernandes Martini, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from jinja2 import Environment, FileSystemLoader
import unicodedata
from lxml import etree
from lxml import objectify

HOMOLOGACAO = 1
PRODUCAO = 2

URLS = {
    HOMOLOGACAO: {
        'CalcularFretePrazo': 'http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx?WSDL',
        'SIGEPWeb': 'https://apphom.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl',
    },
    PRODUCAO: {
        'CalcularFretePrazo': 'http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx?WSDL',
        'SIGEPWeb': 'https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl',
    },
}


def render_xml(path, template_name, usuario):
    env = Environment(
        loader=FileSystemLoader(path), extensions=['jinja2.ext.with_']) 
    template = env.get_template(template_name)
    xml = template.render(usuario)
    return xml


def sanitize_response(response):
    response = unicode(response)
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
