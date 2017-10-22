# -*- coding: utf-8 -*-
import zeep

from .utils import URLS


class Client:

    def __init__(self, usuario, senha, ambiente):
        self.usuario = usuario
        self.senha = senha
        self._ambiente = None
        self._url = None
        self.ambiente = ambiente
        self.cliente = zeep.Client(self.url)

    @property
    def ambiente(self):
        return self._ambiente

    @ambiente.setter
    def ambiente(self, value):
        """ Define o ambiente e a url de consultaa ser utilizado conforma o
        ambiente escolhido.

        :param: ambiente a ser utilizado durante as consultas
        :type: Int
        """
        self._ambiente = value

        try:
            self._url = URLS[self._ambiente]
        except KeyError:
            raise KeyError(
                'Ambiente inválido! Valor deve ser 1 para PRODUCAO e 2 '
                'para HOMOLOGACAO')

    @property
    def url(self):
        """ Retorna a URL do ambiente utilizado.

        :return: URL do ambiente utilizado
        :rtype: Str
        """
        return self._url

    def consulta_cep(self, cep):
        """ Retorna o endereço correspondente ao número de CEP informado.

        :param cep: CEP a ser consultado.
        :type cep: str
        :return: Dados do endereço do CEP consultado.
        :rtype: dict
        """
        return self.cliente.service.consultaCEP(cep)
