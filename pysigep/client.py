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
        """ Define o ambiente e a url de consulta a ser utilizado conforma o
        ambiente escolhido.

        :param: ambiente a ser utilizado durante as consultas
        :type: Int
        """
        self._ambiente = value

        try:
            self._url = URLS[self._ambiente]
            self.cliente = zeep.Client(self.url)
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
        """ Este método retorna o endereço correspondente ao número de CEP
        informado.

        :param cep: Número do CEP sem hífen.
        :type cep: str
        :return: Dados do endereço do CEP consultado.
        :rtype: enderecoERP
        """
        param = {
            'cep': cep
        }
        return self.cliente.service.consultaCEP(**param)

    def verifica_disponibilidade_servico(self, cod_administrativo,
                                         numero_servico, cep_origem,
                                         cep_destino):
        """Por meio desse método, pode ser verificado se um serviço que não
        possui abrangência nacional está disponível entre um CEP de Origem e
        de Destino

        :param cod_administrativo: Código Administrativo do contrato do Cliente com os Correios.  # noqa
        :param numero_servico: Códigos dos serviços contratados. Ex: 40215, 81019  # noqa
        :param cep_origem: CEP de Origem sem hífen
        :param cep_destino: CEP de Destino sem hífen
        :return: True para serviço disponível, False caso contrário.
        """
        params = {
            'codAdministrativo': cod_administrativo,
            'numeroServico': numero_servico,
            'cepOrigem': cep_origem,
            'cepDestino': cep_destino,
            'usuario': self.usuario,
            'senha': self.senha,
        }
        return self.cliente.service.verificaDisponibilidadeServico(**params)
