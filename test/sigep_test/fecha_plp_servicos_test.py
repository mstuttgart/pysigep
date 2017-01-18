# -*- coding: utf-8 -*-

from unittest import TestCase

from pysigep.sigep import fecha_plp_servicos


class TestFechaPlpServicos(TestCase):

    def test_send_plp_servicos(self):

        data = {
            'idPlpCliente': '123',
            'usuario': 'sigep',
            'senha': 'n5f9t8',
            'listaEtiquetas': [
                'PH18556091BR',
            ],
            'cartaoPostagem': '0123456789',
            'numero_contrato': '0123456789',
            'numero_diretoria': '36',
            'codigo_administrativo': '12345678',
            'nome_remetente': 'Empresa Ltda',
            'logradouro_remetente': 'Avenida Centra',
            'numero_remetente': '2370',
            'complemento_remetente': u'[sala 1205,12° andar]',
            'bairro_remetente': 'Centro',
            'cep_remetente': '70002900',
            'cidade_remetente': u'Brasília',
            'uf_remetente': 'PR',
            'telefone_remetente': '6112345008',
            'email_remetente': u'cli@mail.com.br',
            'objetos': [{
                'numero_etiqueta': 'PH18556091BR',
                'codigo_servico_postagem': '',
                'cubagem': '',
                'peso': '',
                'nome_destinatario': '',
                'telefone_destinatario': '',
                'celular_destinatario': '',
                'email_destinatario': '',
                'logradouro_destinatario': '',
                'complemento_destinatario': '',
                'numero_end_destinatario': '',
                'bairro_destinatario': '',
                'cidade_destinatario': '',
                'uf_destinatario': '',
                'cep_destinatario': '',
                'numero_nota_fiscal': '',
                'serie_nota_fiscal': '',
                'descricao_objeto': '',
                'valor_a_cobrar': '',
                'valor_declarado': '',
                'tipo_objeto': '',
                'dimensao_altura': '',
                'dimensao_largura': '',
                'dimensao_comprimento': '',
                'dimensao_diametro': '',
                'servicos_adicionais': [
                    '019', '001'
                ]
            }],
            'cartaoPostagem': '0123456789',
        }
        with self.assertRaises(Exception):
            fecha_plp_servicos(**data)

        data['ambiente'] = 1
        retorno = fecha_plp_servicos(**data)

        self.assertTrue(retorno != u'')
