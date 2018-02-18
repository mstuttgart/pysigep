# -*- coding: utf-8 -*-
import zeep

from .utils import URLS, validar, trim


class SOAPClient:

    def __init__(self, usuario, senha, ambiente):
        """Inicializa atributos da classe SOAPClient

        Arguments:
            usuario {str} -- login de acesso do SIGEPWeb
            senha {str} -- senha de acesso do SIGEPWeb
            ambiente {int} -- Constante indicando ambiente a ser 
            utilizado para as consultas (Homologacao/Producao)
        """
        self.usuario = str(usuario)
        self.senha = str(senha)
        self._ambiente = None
        self._url = None
        self.ambiente = ambiente

        self.cliente = zeep.Client(self.url)

    @property
    def ambiente(self):
        return self._ambiente

    @ambiente.setter
    def ambiente(self, value):
        """Define o ambiente e a url de consulta a ser utilizado conforma o
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
        """Retorna a URL do ambiente utilizado.

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

        # Validamos cada ums dos parametros segundo a documentacao
        validar('cep', trim(cep))

        param = {
            'cep': cep
        }
        return self.cliente.service.consultaCEP(**param)

    def verifica_disponibilidade_servico(self,
                                         cod_administrativo,
                                         numero_servico,
                                         cep_origem,
                                         cep_destino):
        """Por meio desse método, pode ser verificado se um serviço que não
        possui abrangência nacional está disponível entre um CEP de Origem e
        de Destino.

        :param cod_administrativo: Código Administrativo do contrato do Cliente com os Correios.  # noqa
        :param numero_servico: Códigos dos serviços contratados. Ex: 40215, 81019
        :param cep_origem: CEP de Origem sem hífen
        :param cep_destino: CEP de Destino sem hífen
        :return: True para serviço disponível, False caso contrário.
        """

        # Validamos cada ums dos parametros segundo a documentacao
        validar('codAdministrativo', cod_administrativo)
        validar('numeroServico', numero_servico)
        validar('cep', trim(cep_origem))
        validar('cep', trim(cep_destino))

        params = {
            'codAdministrativo': cod_administrativo,
            'numeroServico': numero_servico,
            'cepOrigem': cep_origem,
            'cepDestino': cep_destino,
            'usuario': self.usuario,
            'senha': self.senha,
        }
        return self.cliente.service.verificaDisponibilidadeServico(**params)

    def get_status_cartao_postagem(self, numero_cartao_postagem):
        """Este método retorna o situação do cartão de postagem. É recomendada
        a pesquisa periódica para evitar tentativa de postagens com cartão
        suspenso, ocasionando a não aceitação dos objetos nos Correios.

        :param numero_cartao_postagem: Número do Cartão de Postagem vinculado ao contrato.
        :return: 'Normal' para cartão de postagem disponível, 'Cancelado' caso contrário.
        """

        validar('numeroCartaoPostagem', numero_cartao_postagem)

        params = {
            'numeroCartaoPostagem': numero_cartao_postagem,
            'usuario': self.usuario,
            'senha': self.senha,
        }
        return self.cliente.service.getStatusCartaoPostagem(**params)
