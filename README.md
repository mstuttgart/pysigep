SIGEP Web - Correios
====================
[![Build Status](https://travis-ci.org/mstuttgart/python-sigep.svg?branch=develop)](https://travis-ci.org/mstuttgart/python-sigep)
[![Coverage Status](https://coveralls.io/repos/github/mstuttgart/python-sigep/badge.svg?branch=develop)](https://coveralls.io/github/mstuttgart/python-sigep?branch=develop)
[![Code Health](https://landscape.io/github/mstuttgart/python-sigep/develop/landscape.svg?style=flat)](https://landscape.io/github/mstuttgart/python-sigep/develop)
[![Maintenance](https://img.shields.io/maintenance/yes/2016.svg)](https://github.com/mstuttgart/python-sigep/tree/develop)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/kefir500/ghstats/master/LICENSE)

Implementação do sistema SIGEP Web em Python permitindo integração com Web Service do Correios. O Módulo funciona como uma interface de consulta para os métodos fornecidos pelo webservice.

## Recursos

- [x] Consultar custo do frete e prazos para entrega dado um endereço.
- [ ] Realizar o rastreamento de uma mercadoria através do seu número de rastreamento.
- [x] Verificar *status* de um Cartão de Postagem
- [x] Obter dados do endereço a partir de seu respectivo CEP.
- [x] Verificar disponibilidade de um dado serviço.  
- [x] Gerar etiquetas para postagem de mercadoria e posterior rastreamento. 
- [ ] Criação da pré-lista de postagem (PLP) e envio de seu XML para o webservice dos Correios.   
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
from sigep.sigep.status_cartao_postagem import RequestStatusCartaoPostagem
from sigep.frete.consulta_frete import RequestCalcPrecoPrazo
from sigep.webservices.webservice_sigep import WebserviceSIGEP
from sigep.webservices.webservice_frete import WebserviceFrete
from sigep.sigep_exceptions import ErroValidacaoXML

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
print response.resposta

# Requisição para servico ConsultaStatusCartaoPostagem
req = RequestStatusCartaoPostagem(CARTAO_POSTAGEM, LOGIN, SENHA)

response = server.request(req)
print response.resposta

# Cliente para webservice de calculo de preço e prazo
server = WebserviceFrete()

# Requisição para o Servico CalcPrecoPrazo
req = RequestCalcPrecoPrazo('40436,40215', CEP_ORIGEM, '37503130', '2',
                            RequestCalcPrecoPrazo.FORMATO_CAIXA_PACOTE,
                            100.0, 100.0, 100.0, 0.0, False, 0.00, False)

try:
    # Executando a requisição
    resp = server.request(req)
except ErroValidacaoXML as exc:
    print exc.message

</code></pre>

## Executando os testes
Caso você deseje executar os testes, basta usar o comando abaixo (necessário estar conectado à internet):

```python setup.py test```

## Contribuindo
Encontrou algum erro? Quer adicionar alguma *feature* nova ao projeto? Faça um *fork* deste repositório e me envie um *Pull Request*. Contribuições sempre são bem vindas.

## SigepWeb Docs
* [Manual SigepWeb](http://www.corporativo.correios.com.br/encomendas/sigepweb/doc/Manual_de_Implementacao_do_Web_Service_SIGEPWEB_Logistica_Reversa.pdf)
* [Manual Calculo Preço e Prazo](http://www.correios.com.br/para-voce/correios-de-a-a-z/pdf/calculador-remoto-de-precos-e-prazos/manual-de-implementacao-do-calculo-remoto-de-precos-e-prazos)
* [Manual Rastreamento](http://blog.correios.com.br/comercioeletronico/wp-content/uploads/2011/10/Guia-Tecnico-Rastreamento-XML-Cliente-Vers%C3%A3o-e-commerce-v-1-5.pdf)
