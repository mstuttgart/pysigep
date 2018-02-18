import re


HOMOLOGACAO = 1
PRODUCAO = 2

URLS = {
    HOMOLOGACAO: 'https://apphom.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl',  # noqa
    PRODUCAO: 'https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl',  # noqa
}

HOMOG_USUARIO = 'sigep'
HOMOG_SENHA = 'n5f9t8'
HOMOG_CARTAO = '0067599079'
HOMOG_CODIGO_ADMIN = '17000190'
HOMOG_CONTRATO = '9992157880'

CARACTERES_NUMERICOS = re.compile(r'[^0-9]')

regex_map = {
    'codAdministrativo': {
        'regex': r'^\d{8}$',
        'msg_erro': 'Código Adminsitrativo deve ser formado apenas por números e conter 8 digitos.',
    },
    'numeroServico': {
        'regex': r'^\d{5}$',
        'msg_erro': 'Código do Serviço deve ser formado apenas por números e conter 5 digitos.',
    },
    'cep': {
        'regex': r'^\d{8}$',
        'msg_erro': 'CEP mal formatado. CEP deve conter 8 digitos.',
    },
    'numeroCartaoPostagem': {
        'regex': r'^\d{10}$',
        'msg_erro': 'Numero do cartão de postagem deve conter 10 digitos.',
    },
}


def validar(key, string):
    """Realiza a validação de uma dado texto a partir da regex fornecida.

    Arguments:
        regex {str} -- Expressao regular para ser utilizada na validacao
        string {str} -- Texto a ser validado
        msg_erro {Str} -- Mensagem de erro

    Raises:
        TypeError -- Quando o parametro string não é uma string.
        ValueError -- Quando a string fornecida não coincide com sua expressão regular.
    """
    if not isinstance(string, str):
        raise TypeError('parâmetro "string" deve do tipo str. '
                        'Tipo encontrado: %s' % type(string))

    if not re.search(regex_map[key]['regex'], string):
        raise ValueError(regex_map[key]['msg_erro'])


def trim(string):
    """Remove pontuações da string, deixando apenas valores númericos.

    Arguments:
        string {str} -- String a ser formatada.

    Raises:
        TypeError -- Quando o parâmetro string não é do tipo str

    Returns:
        str -- Nova string formatada.
    """

    if not isinstance(string, str):
        raise TypeError(
            'Parâmetro "string" deve ser do tipo str. Tipo encontrado: %s' % type(string))

    return CARACTERES_NUMERICOS.sub('', string)
