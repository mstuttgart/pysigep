"""
PyCEPCorreios
~~~~~~~~~~~~~
PySIGEP é uma API para consumo dos serviços fornecido pelo SIGEPWeb dos
Correios.

   >>> from pysigep.client import Client
   >>> from pysigep.utils import HOMOLOGACAO, HOMOG_USUARIO, HOMOG_SENHA
   >>> cliente = Client(usuario=HOMOG_USUARIO, senha=HOMOG_SENHA,
        ...ambiente=HOMOLOGACAO)
   >>> endereco = cliente.consultar_cep('37503130')
   >>> endereco
   {
        'bairro': 'Santo Antônio',
        'cep': '37503130',
        'cidade': 'Itajubá',
        'end': 'Rua Geraldino Campista',
        'id': '0',
        'uf': 'MG',
        'complemento': '',
        'complemento2': '- até 214/215',
    }

Para outros metodos suportados, veja a
documentação em https://pysigep.readthedocs.io.
:copyright: 2016-2017 por Michell Stuttgart Faria
:license: MIT, veja o arquivo LICENSE para mais detalhes.
"""


from .__version__ import (__title__,  # noqa: F401
                          __description__,
                          __version__,
                          __author__,
                          __author_email__,
                          __maintainer__,
                          __maintainer_email__,
                          __url__,
                          __download_url__,
                          __copyright__,
                          __license__)
