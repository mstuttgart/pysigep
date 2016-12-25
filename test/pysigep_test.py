from unittest import TestCase
from pysigep import send, _url


class TestPySIGEP(TestCase):

    def test_send(self):
        xml_path = 'ConsultaCep.xml'
        xml_method = 'consultaCEPResponse'
        kw = {'cep': '83010140'}
        api = 'SIGEPWeb'
        url = _url(1, api)
        res = send(xml_path, xml_method, api, url, **kw)
        self.assertNotIn('mensagem_erro', res)
        self.assertEqual('Cruzeiro', res.bairro)
