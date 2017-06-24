=======
PySIGEP
=======

.. image:: https://img.shields.io/travis/mstuttgart/pysigep.svg
        :target: https://travis-ci.org/mstuttgart/pysigep

.. image:: https://img.shields.io/pypi/v/pysigep.svg
        :target: https://pypi.python.org/pypi/pysigep

.. image:: https://img.shields.io/pypi/l/pysigep.svg
        :target: https://pypi.python.org/pypi/pysigep

.. image:: https://readthedocs.org/projects/pysigep/badge/?version=latest
        :target: https://pysigep.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

Interface python para uso dos serviços fornecidos pelo SIGEPWeb dos Correios.

O SIGEP WEB é um sistema com o propósito de preparar e gerenciar
as postagens de Clientes dos Correios. Seus principais atributos técnicos são:
facilidade e rapidez na preparação das postagens e gestão das informações sobre os objetos postados.


* Free software: MIT license
* Documentation: https://pysigep.readthedocs.io.


Features
--------

- [x] Verificar *status* de um Cartão de Postagem
- [x] Obter dados do endereço a partir de seu respectivo CEP.
- [x] Verificar disponibilidade de um dado serviço.
- [x] Gerar etiquetas para postagem de mercadoria.
- [x] Criação da pré-lista de postagem (PLP) e envio de seu XML para o webservice dos Correios.
- [ ] Imprimir etiqueta da PLP.
- [x] Imprimir Chancela.
- [ ] Rotinas de logística reversa.
- [ ] Calcula frete e prazo de entrega.


Instalação
----------

A versão atual **ainda esta em fase de desenvolvimento**, sendo que os recursos
disponiveis podem ser removidos sem aviso prévio. Portanto, não é recomendável
seu uso em ambiente de produção.

Como usar
---------

.. code-block:: python

    from pysigep.sigep import cep_consulta
    from pysigep.sigep import verifica_disponibilidade_servico

    # Executando a consulta de CEP

    cep = {'cep': '83010140'}
    consulta = cep_consulta(**cep)

    print consulta.bairro
    print consulta.cep
    print consulta.cidade
    print consulta.complemento
    print consulta.complemento2
    print consulta.end
    print consulta.id
    print consulta.uf

    # Verificando disponibilidade de serviço

    usuario = {
        'codAdministrativo': '08082650',
        'numeroServico': '40215',
        'cepOrigem': '70002900',
        'cepDestino': '81350120',
        'usuario': 'sigep',
        'senha': 'n5f9t8',
    }

    with self.assertRaises(Exception):
        print verifica_disponibilidade_servico(**usuario)


    # Solicitando etiquetas

    solicitacao = {
        'usuario': 'sigep',
        'senha': 'n5f9t8',
        'identificador': '34028316000103',
        'idServico': '104625',
        'qtdEtiquetas': '10',
    }
    with self.assertRaises(Exception):
        print solicita_etiquetas_com_dv(**solicitacao)

Créditos
--------

Copyright (C) 2016-2017 por Michell Stuttgart Faria
