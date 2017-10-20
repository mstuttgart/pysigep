# -*- coding: utf-8 -*-
import zeep

from .utils import URLS


class Client:

    def __init__(self, usuario, senha, ambiente):
        self.usuario = usuario
        self.senha = senha

        try:
            self._url_ambiente = URLS[ambiente]
        except KeyError:
            raise KeyError(
                'Ambiente inválido! Valor deve ser 1 para PRODUCAO e 2 '
                'para HOMOLOGACAO')

        self.zeep_client = zeep.Client(self.url_ambiente)

    @property
    def url_ambiente(self):
        return self._url_ambiente

    def consulta_cep(self, cep):
        """ Retorna o endereço correspondente ao número de CEP informado.

        :param cep: CEP a ser consultado.
        :type cep: str
        :return: Dados do endereço do CEP consultado.
        :rtype: dict
        """
        return self.zeep_client.service.consultaCEP(cep)

    def set_ambiente(self, ambiente):
        """ Define o ambiente a ser utilizado nas consultas.

        :param ambiente: Flag fo ambiente a ser utilizado, i.e:
        utils.HOMOLOGACAO ou utils.PRODUCAO
        :type ambiente: integer
        """

        try:
            self._url_ambiente = URLS[ambiente]
        except KeyError:
            raise KeyError(
                'Ambiente inválido! Valor deve ser 1 para PRODUCAO e 2 para '
                'HOMOLOGACAO')
