==========
Utilização
==========

A versão atual **ainda esta em fase de desenvolvimento**, sendo que os recursos
disponiveis podem ser removidos sem aviso prévio. Portanto, não é recomendável
seu uso em ambiente de produção.

Em construção...

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