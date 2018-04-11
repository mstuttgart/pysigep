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
HOMOG_CNPJ = '38.875.380/0001-80'

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
    'tipoDestinatario': {
        'regex': r'^\w{1}$',
        'msg_erro': 'Tipo de destinatario incorreto.',
    },
    'cnpj': {
        'regex': r'^\d{14}$',
        'msg_erro': 'CNPJ inválido.',
    },
    'etiqueta': {
        'regex': r'^[A-Z]{2}\d{8} BR$',
        'msg_erro': 'Etiqueta inválida. A etiqueta deve possuir 13 caracters e ser do formato: "AA00000000 BR"'
    }
}


def validar(key, string):
    """Realiza a validação de uma dado texto a partir da regex fornecida.

    Arguments:
        regex {str} -- Expressao regular para ser utilizada na validacao
        string {str} -- Texto a ser validado
        msg_erro {Str} -- Mensagem de erro

    Raises:
        ValueError -- Quando a string fornecida não coincide com sua expressão regular.
    """

    if not re.search(regex_map[key]['regex'], string):
        raise ValueError(regex_map[key]['msg_erro'])


def trim(string):
    """Remove pontuações da string, deixando apenas valores númericos.

    Arguments:
        string {str} -- String a ser formatada.

    Returns:
        str -- Nova string formatada.
    """

    return CARACTERES_NUMERICOS.sub('', string)
