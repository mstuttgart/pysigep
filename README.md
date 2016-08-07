SIGEP Web - Correios
====================

[![Build Status](https://travis-ci.org/mstuttgart/pysigep.svg?branch=develop)](https://travis-ci.org/mstuttgart/pysigep)
[![Coverage Status](https://coveralls.io/repos/github/mstuttgart/pysigep/badge.svg?branch=develop)](https://coveralls.io/github/mstuttgart/pysigep?branch=develop)
[![Code Health](https://landscape.io/github/mstuttgart/pysigep/develop/landscape.svg?style=flat)](https://landscape.io/github/mstuttgart/pysigep/develop)
[![PyPI](https://img.shields.io/pypi/status/pysigep.svg?maxAge=2592000)]()
[![PyPI](https://img.shields.io/pypi/v/pysigep.svg?maxAge=2592000)](https://pypi.python.org/pypi/pysigep)
[![PyPI](https://img.shields.io/pypi/pyversions/pysigep.svg?maxAge=2592000)]()
[![PyPI](https://img.shields.io/pypi/l/pysigep.svg)](https://github.com/mstuttgart/pysigep/blob/develop/LICENSE)

Implementação do sistema SIGEP Web em Python permitindo integração com Web Service do Correios. O Módulo funciona como uma interface de consulta para os métodos fornecidos pelo webservice. Também permite rastreamento de encomendas a partir da etiqueta de identificação e cálculo de frete.

## Recursos

- [x] Consultar custo do frete e prazos para entrega dado um endereço.
- [x] Verificar *status* de um Cartão de Postagem
- [x] Obter dados do endereço a partir de seu respectivo CEP.
- [x] Verificar disponibilidade de um dado serviço.  
- [x] Gerar etiquetas para postagem de mercadoria e posterior rastreamento. 
- [x] Criação da pré-lista de postagem (PLP) e envio de seu XML para o 
webservice dos Correios.   
- [ ] Imprimir etiqueta da PLP em formato PDF.   
- [ ] Imprimir Chancela em formato PDF.
- [ ] Rotinas de logística reversa.

## Instalação

A versão atual ainda esta em fase de desenvolvimento, sendo assim os recursos disponiveis podem ser removidos sem aviso prévio. Sendo assim, não é recomendável seu uso em ambiente de produção

```
pip install pysigep
```

## Dependências

* python 2.7 (suporte para python 3 em breve)
* requests 

Instalação do requests: `sudo pip install requests`

## Como usar

```python
# -*- coding: utf-8 -*-
from pysigep.sigep.consulta_cep import RequestConsultaCEP
from pysigep.sigep.disponibilidade_servico import RequestDisponibilidadeServico
from pysigep.sigep.status_cartao_postagem import RequestStatusCartaoPostagem
from pysigep.frete.consulta_frete import RequestCalcPrecoPrazo
from pysigep.webservices.webservice_sigep import WebserviceSIGEP
from pysigep.webservices.webservice_frete import WebserviceFrete

LOGIN = 'sigep'
SENHA = 'n5f9t8'
COD_ADMIN = '08082650'
NUMERO_SERVICO = '40436'
CEP_ORIGEM = '99200-000'
CEP_DESTINO = '99200-000'
CARTAO_POSTAGEM = '0057018901'

# Cliente do webservice do sistema sigep Correios
server = WebserviceSIGEP(WebserviceSIGEP.AMBIENTE_HOMOLOGACAO)

# Requisição para serviço ConsultaCEP
req = RequestConsultaCEP('37503-000')

# Executando a requisição
response = server.request(req)

print response.resposta['logradouro']
print response.resposta['bairro']
print response.resposta['cidade']
print response.resposta['uf']
print response.resposta['complemento']
print response.resposta['complemento_2']

# Requisição para serviço ConsultaDisponibilidadeServico
req = RequestDisponibilidadeServico(COD_ADMIN, NUMERO_SERVICO,
                                    CEP_ORIGEM, CEP_DESTINO,
                                    LOGIN, SENHA)

# Executando a requisição
response = server.request(req)
print response.resposta['disponibilidade']

# Requisição para servico ConsultaStatusCartaoPostagem
req = RequestStatusCartaoPostagem(CARTAO_POSTAGEM, LOGIN, SENHA)

response = server.request(req)
print response.resposta['status']

# Cliente para webservice de calculo de preço e prazo
server = WebserviceFrete()

# Requisição para o Servico CalcPrecoPrazo
req = RequestCalcPrecoPrazo('40436,40215', CEP_ORIGEM, '37503130', '2',
                            RequestCalcPrecoPrazo.FORMATO_CAIXA_PACOTE,
                            100.0, 100.0, 100.0, 0.0, False, 0.00, False)

# Executando a requisição
response = server.request(req)
print response.resposta['40436']['Valor']
print response.resposta['40436']['PrazoEntrega']
print response.resposta['40436']['ValorMaoPropria']
print response.resposta['40436']['ValorAvisoRecebimento']
print response.resposta['40436']['ValorValorDeclarado']
print response.resposta['40436']['EntregaDomiciliar']
print response.resposta['40436']['EntregaSabado']
print response.resposta['40436']['Erro']
print response.resposta['40436']['MsgErro']
print response.resposta['40436']['ValorSemAdicionais']
print response.resposta['40436']['obsFim']

```

## Contribuindo
Encontrou algum erro? Quer adicionar alguma *feature* nova ao projeto? Faça um *fork* deste repositório e me envie um *Pull Request*. Contribuições sempre são bem vindas.

#### To do

Lista de funcionalidade a serem implementadas [aqui](https://github.com/mstuttgart/python-sigep/issues/7).

#### Executando os testes
Caso você deseje executar os testes, basta usar o comando abaixo (necessário estar conectado à internet):

```python setup.py test```

## SigepWeb Docs
* [Manual SigepWeb](http://www.corporativo.correios.com.br/encomendas/sigepweb/doc/Manual_de_Implementacao_do_Web_Service_SIGEPWEB_Logistica_Reversa.pdf)
* [Manual Calculo Preço e Prazo](http://www.correios.com.br/para-voce/correios-de-a-a-z/pdf/calculador-remoto-de-precos-e-prazos/manual-de-implementacao-do-calculo-remoto-de-precos-e-prazos)
