from unittest import TestCase, mock

from pysigep.client import SOAPClient
from pysigep.utils import URLS, HOMOLOGACAO, PRODUCAO
from pysigep.utils import (HOMOG_USUARIO,
                           HOMOG_SENHA,
                           HOMOG_CODIGO_ADMIN,
                           HOMOG_CARTAO,
                           HOMOG_CNPJ)


class TestSOAPClient(TestCase):

    def setUp(self):
        super(TestSOAPClient, self).setUp()

    def test_set_ambiente(self):

        self.cliente = SOAPClient(ambiente=HOMOLOGACAO,
                                  senha=HOMOG_SENHA,
                                  usuario=HOMOG_USUARIO)

        self.cliente.ambiente = PRODUCAO
        self.assertEqual(self.cliente.ambiente, PRODUCAO)
        self.assertEqual(self.cliente.url, URLS[PRODUCAO])

        self.cliente.ambiente = HOMOLOGACAO
        self.assertEqual(self.cliente.ambiente, HOMOLOGACAO)
        self.assertEqual(self.cliente.url, URLS[HOMOLOGACAO])

        with self.assertRaises(KeyError):
            self.cliente.ambiente = 3

    @mock.patch('zeep.Client')
    def test_consulta_cep(self, mk):

        class MockClass:
            def __init__(self, dictionary):
                for k, v in dictionary.items():
                    setattr(self, k, v)

        end_esperado = {
            'bairro': 'Santo Antônio',
            'cep': '37503130',
            'cidade': 'Itajubá',
            'complemento': None,
            'complemento2': '- até 214/215',
            'end': 'Rua Geraldino Campista',
            'id': 0,
            'uf': 'MG',
            'unidadesPostagem': [],
        }

        # Criamos o cliente SOAP
        cliente = SOAPClient(ambiente=HOMOLOGACAO,
                             senha=HOMOG_SENHA,
                             usuario=HOMOG_USUARIO)

        service_mk = mk.return_value.service

        # Criamos o mock para o valor de retorno
        service_mk.consultaCEP.return_value = MockClass(end_esperado)

        # Realizamos a consulta de CEP
        endereco = cliente.consulta_cep('37.503-130')

        self.assertEqual(endereco.bairro, 'Santo Antônio')
        self.assertEqual(endereco.cep, '37503130')
        self.assertEqual(endereco.cidade, 'Itajubá')
        self.assertEqual(endereco.complemento, None)
        self.assertEqual(endereco.complemento2, '- até 214/215')
        self.assertEqual(endereco.end, 'Rua Geraldino Campista')
        self.assertEqual(endereco.id, 0)
        self.assertEqual(endereco.uf, 'MG')
        self.assertEqual(endereco.unidadesPostagem, [])

        # Verifica se o metodo consultaCEP foi chamado com os parametros corretos
        service_mk.consultaCEP.assert_called_with(cep='37503130')

    @mock.patch('zeep.Client')
    def test_get_status_cartao_postagem(self, mk):

        params = {
            'numero_cartao_postagem': HOMOG_CARTAO,
        }

        # Sobrescrevemos o client para que o mock funcione
        cliente = SOAPClient(ambiente=HOMOLOGACAO,
                             senha=HOMOG_SENHA,
                             usuario=HOMOG_USUARIO)

        service = mk.return_value.service

        service.getStatusCartaoPostagem.return_value = 'Normal'
        ret = cliente.get_status_cartao_postagem(**params)
        self.assertEqual(ret, 'Normal')

        service.getStatusCartaoPostagem.return_value = 'Cancelado'
        ret = cliente.get_status_cartao_postagem(**params)
        self.assertEqual(ret, 'Cancelado')

    @mock.patch('zeep.Client')
    def test_verifica_disponibilidade_servico(self, mk):

        params = {
            'cod_administrativo': HOMOG_CODIGO_ADMIN,
            'numero_servico': '04162',
            'cep_origem': '70002900',
            'cep_destino': '70.002-900',
        }

        # Sobrescrevemos o client para que o mock funcione
        cliente = SOAPClient(ambiente=HOMOLOGACAO,
                             senha=HOMOG_SENHA,
                             usuario=HOMOG_USUARIO)

        service_mk = mk.return_value.service

        service_mk.verificaDisponibilidadeServico.return_value = True
        ret = cliente.verifica_disponibilidade_servico(**params)
        self.assertTrue(ret)

        service_mk.verificaDisponibilidadeServico.return_value = False
        ret = cliente.verifica_disponibilidade_servico(**params)
        self.assertFalse(ret)

        params = {
            'codAdministrativo': HOMOG_CODIGO_ADMIN,
            'numeroServico': '04162',
            'cepOrigem': '70002900',
            'cepDestino': '70002900',
            'usuario': HOMOG_USUARIO,
            'senha': HOMOG_SENHA,
        }

        service_mk.verificaDisponibilidadeServico.assert_called_with(**params)

    @mock.patch('zeep.Client')
    def test_solicita_etiquetas(self, mk):

        params = {
            'tipo_destinatario': 'C',
            'cnpj': HOMOG_CNPJ,
            'id_servico': 124849,
            'qtd_etiquetas': 2,
        }

        # Sobrescrevemos o client para que o mock funcione
        self.cliente = SOAPClient(ambiente=HOMOLOGACAO,
                                  senha=HOMOG_SENHA,
                                  usuario=HOMOG_USUARIO)

        service = mk.return_value.service

        service.solicitaEtiquetas.return_value = 'DL76023727 BR,DL76023728 BR'
        ret = self.cliente.solicita_etiquetas(**params)

        etiquetas = [
            'DL76023727 BR',
            'DL76023728 BR',
        ]

        self.assertListEqual(etiquetas, ret)

    @mock.patch('zeep.Client')
    def test_gera_digito_verificador_etiquetas(self, mk):
        params = {
            'etiquetas': ['DL76023727 BR', 'DL76023728 BR'],
        }

        # Sobrescrevemos o client para que o mock funcione
        self.cliente = SOAPClient(ambiente=HOMOLOGACAO,
                                  senha=HOMOG_SENHA,
                                  usuario=HOMOG_USUARIO)

        service = mk.return_value.service

        service.geraDigitoVerificadorEtiquetas.return_value = [2, 6]

        ret = self.cliente.gera_digito_verificador_etiquetas(**params)
        self.assertListEqual(ret, [2, 6])

        ret = self.cliente.gera_digito_verificador_etiquetas(**params,
                                                             offline=False)
        self.assertListEqual(ret, [2, 6])
