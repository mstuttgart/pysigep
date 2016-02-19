SIGEP Web - Correios
====================
[![Build Status](https://travis-ci.org/mstuttgart/python-sigep.svg?branch=develop)](https://travis-ci.org/mstuttgart/python-sigep)
[![Coverage Status](https://coveralls.io/repos/github/mstuttgart/python-sigep/badge.svg?branch=develop)](https://coveralls.io/github/mstuttgart/python-sigep?branch=develop)
[![Code Health](https://landscape.io/github/mstuttgart/python-sigep/develop/landscape.svg?style=flat)](https://landscape.io/github/mstuttgart/python-sigep/develop)
[![Maintenance](https://img.shields.io/maintenance/yes/2016.svg)](https://github.com/mstuttgart/python-sigep/tree/develop)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/kefir500/ghstats/master/LICENSE)

Implementação do sistema SIGEP Web em Python permitindo integração com Web Service do Correios. O Módulo funciona como uma interface de consulta para os métodos fornecidos pelo webservice.

## Recursos

- [ ] Consultar custo do frete e prazos para entrega dado um endereço.
- [ ] Realizar o rastreamento de uma mercadoria através do seu número de rastreamento.
- [x] Verificar *status* de um Cartão de Postagem
- [x] Obter dados do endereço a partir de seu respectivo CEP.
- [x] Verificar disponibilidade de um dado serviço.  
- [ ] Criação da pré-lista de postagem (PLP) e envio de seu XML para o webservice dos Correios.   
- [ ] Gerar etiquetas para postagem de mercadoria e posterior rastreamento. 
- [ ] Imprimir etiqueta da PLP em formato PDF.   
- [ ] Imprimir Chancela em formato PDF.

## Dependências

* python 2.7
* requests 

Instalação do requests: `sudo pip install requests`

## Como usar

<pre lang="python"><code>
from sigep.sigep.consulta_cep import RequestConsultaCEP
from sigep.sigep.disponibilidade_servico import RequestDisponibilidadeServico
from sigep.webservices.webservice_sigepweb import WebserviceSIGEP

LOGIN = 'sigep'
SENHA = 'n5f9t8'
COD_ADMIN = '08082650'
NUMERO_SERVICO = '40436'
CEP_ORIGEM = '99200-000'
CEP_DESTINO = '99200-000'

server = WebserviceSIGEPWeb(WebserviceSIGEPWeb.AMBIENTE_HOMOLOGACAO)

bcep = RequestConsultaCEP('37503-000')
response = server.request(bcep)

print response.rua.valor
print response.bairro.valor
print response.cidade.valor
print response.uf.valor
print response.complemento.valor
print response.complemento_2.valor

verif_disp = RequestDisponibilidadeServico(COD_ADMIN, NUMERO_SERVICO, 
CEP_ORIGEM, CEP_DESTINO, LOGIN, SENHA)
                                         
response = server.request(verif_disp)
print response.disponivel.valor

</code></pre>

## SigepWeb Docs
* [Manual SigepWeb](http://www.corporativo.correios.com.br/encomendas/sigepweb/doc/Manual_de_Implementacao_do_Web_Service_SIGEPWEB_Logistica_Reversa.pdf)
* [Manual Calculo Preço e Prazo](http://www.correios.com.br/para-voce/correios-de-a-a-z/pdf/calculador-remoto-de-precos-e-prazos/manual-de-implementacao-do-calculo-remoto-de-precos-e-prazos)
* [Manual Rastreamento](http://blog.correios.com.br/comercioeletronico/wp-content/uploads/2011/10/Guia-Tecnico-Rastreamento-XML-Cliente-Vers%C3%A3o-e-commerce-v-1-5.pdf)
