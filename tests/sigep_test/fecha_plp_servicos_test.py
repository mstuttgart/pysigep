# -*- coding: utf-8 -*-

from unittest import TestCase

from lxml import etree
from pysigep.sigep import fecha_plp_servicos


class TestFechaPlpServicos(TestCase):

    def setUp(self):
        self.etiqueta_sem_dv = 'DL76023727BR'
        self.etiqueta_com_dv = 'DL760237272BR'
        self.data = {
            'idPlpCliente': '123',
            'usuario': 'sigep',
            'senha': 'n5f9t8',
            'listaEtiquetas': [
                self.etiqueta_sem_dv,
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
                'numero_etiqueta': self.etiqueta_com_dv,
                'codigo_servico_postagem': '',
                'cubagem': '',
                'peso': '100',
                'nome_destinatario': '',
                'telefone_destinatario': '',
                'celular_destinatario': '',
                'email_destinatario': '',
                'logradouro_destinatario': '',
                'complemento_destinatario': '',
                'numero_end_destinatario': '',
                'bairro_destinatario': '',
                'cidade_destinatario': '',
                'uf_destinatario': 'PR',
                'cep_destinatario': '81130000',
                'numero_nota_fiscal': '',
                'serie_nota_fiscal': '',
                'descricao_objeto': '',
                'valor_a_cobrar': '',
                'valor_declarado': '',
                'tipo_objeto': '002',
                'dimensao_altura': '28',
                'dimensao_largura': '11',
                'dimensao_comprimento': '16',
                'dimensao_diametro': '0',
                'servicos_adicionais': [
                    '019', '001'
                ]
            }],
            'cartaoPostagem': '0123456789',
        }

    def test_send_plp_servicos_precisa_definir_ambiente(self):
        with self.assertRaises(Exception):
            fecha_plp_servicos(**self.data)

    def test_send_plp_servicos(self):
        self.data['ambiente'] = 1
        retorno = fecha_plp_servicos(**self.data)
        self.assertTrue(retorno != u'')

    def test_send_plp_servicos_valida_xml_contra_xsd(self):
        self.data['ambiente'] = 1
        self.data['objetos'][0]['numero_etiqueta'] = self.etiqueta_sem_dv
        with self.assertRaises(etree.XMLSyntaxError):
            retorno = fecha_plp_servicos(**self.data)
