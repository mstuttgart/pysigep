SIGEP Web - Correios
====================
[![Build Status](https://travis-ci.org/mstuttgart/python-sigep.svg?branch=develop)](https://travis-ci.org/mstuttgart/python-sigep)
[![Coverage Status](https://coveralls.io/repos/github/mstuttgart/python-sigep/badge.svg?branch=develop)](https://coveralls.io/github/mstuttgart/python-sigep?branch=develop)
[![Code Health](https://landscape.io/github/mstuttgart/python-sigep/develop/landscape.svg?style=flat)](https://landscape.io/github/mstuttgart/python-sigep/develop)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/kefir500/ghstats/master/LICENSE)

Implementação do sistema SIGEP Web em Python permitindo integração com Web Service do Correios. O Módulo funciona como uma interface de consulta para os métodos fornecidos pelo webservice.

## Recursos

Esta API pode:

* TODO: Calcular preços e prazos de entrega da encomenda.

* TODO: Obter dados do endereço a partir de um dado CEP.

* TODO: Obter os dados de rastreamento das encomendas.

* TODO: Verificar se um tipo de serviço (Sedex, PAC, ...) é permitido entre dois endereços.  

* TODO: Gerar e enviar o XML da pre-lista de postagem (PLP) para o Correios.   

* TODO: Gerar novos números de etiquetas de postagem. 

* TODO: Criar e/ou verificar validade do dígito verificador das etiquetas (através do web service ou não).  

* TODO: Gerar o relatório da PLP no formato PDF.   

* TODO: Gerar as etiquetas de postagem no formato PDF.

## Requisitos

* python 2.7
* requests 

Instalação do requests: `sudo pip install requests`

## Como usar

<pre lang="python"><code>
from pysigep.sigepweb.consulta_cep import RequestConsultaCEP
from pysigep.webservices.webservice_sigepweb import WebserviceSIGEPWeb

LOGIN = 'sigep'
SENHA = 'n5f9t8'
CNPJ = '34028316000103'
CONTRATO = '9912208555'
CARTAO_POSTAGEM = '0057018901'
COD_ADMIN = '08082650'

server = WebserviceSIGEPWeb(WebserviceSIGEPWeb.AMBIENTE_HOMOLOGACAO)

bcep = RequestConsultaCEP('37503-000')
response = server.request(bcep)
print response.rua.valor
print response.cidade.valor
print response.bairro.valor

</code></pre>

## Contribuindo

1. Faça um fork
2. Crie sua branch para a funcionalidade (`git checkout -b nova-funcionalidade`)
3. Faça o commit suas modificações (`git commit -am 'Adiciona nova funcionalidade'`)
4. Faça o push para a branch (`git push origin nova-funcionalidade`)
5. Crie um novo Pull Request

